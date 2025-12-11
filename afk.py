@nightyScript(
    name="Offline Replier",
    author="@ogzl",
    description="Auto-reply to DMs when offline & log messages to a webhook",
    usage="toggle on/off"
)
def showDMAndGuildToast():
    import aiohttp
    import datetime
    import asyncio  # ✅ Needed for sleep

    replied_users = set()
    custom_reply = "💤 Currently Offline Right Now 💤 , I'll be back shortly! {mention}"
    reply_delay = 0
    delete_after_minutes = 25  # 🕒 Delete auto-reply after X minutes

    # 👉 Replace this with your webhook URL
    WEBHOOK_URL = ""

    async def log_to_webhook(author, content, channel_id, message_id):
        """Send DM info to webhook with a quick jump link"""
        async with aiohttp.ClientSession() as session:
            jump_url = f"https://discord.com/channels/@me/{channel_id}/{message_id}"
            embed = {
                "author": {
                    "name": f"{author}  (@{author.name})",
                    "icon_url": str(author.display_avatar.url)
                },
                "title": "📥 New Offline DM",
                "description": f"[**Jump to DM**]({jump_url})",
                "color": 0x00BFFF,
                "fields": [
                    {"name": "Sender Tag", "value": f"`{author}`", "inline": True},
                    {"name": "User ID", "value": f"`{author.id}`", "inline": True},
                    {"name": "Message", "value": content[:1900] or "*No text*", "inline": False},
                ],
                "footer": {
                    "text": f"Received • {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}"
                }
            }
            await session.post(WEBHOOK_URL, json={"embeds": [embed]})

    @bot.listen('on_message')
    async def showMessage(message):
        if message.author == bot.user:
            return
        if not message.content:
            return
        if isinstance(message.channel, discord.DMChannel):
            # Log every DM to the webhook (with jump link)
            await log_to_webhook(message.author, message.content, message.channel.id, message.id)

            # Auto-reply only once per user
            user_channel_key = (message.channel.id, message.author.id)
            if user_channel_key not in replied_users:
                formatted_reply = custom_reply.format(mention=bot.user.mention)
                sent_msg = await message.channel.send(formatted_reply)
                showToast(
                    text=f"Offline Message Sent to {message.author.name}",
                    type_="SUCCESS",
                    title="Auto-reply Sent"
                )
                replied_users.add(user_channel_key)

                # 🕒 Wait X minutes, then delete the auto-reply
                await asyncio.sleep(delete_after_minutes * 60)
                try:
                    await sent_msg.delete()
                except Exception as e:
                    print(f"Failed to delete auto-reply: {e}")

showDMAndGuildToast()
