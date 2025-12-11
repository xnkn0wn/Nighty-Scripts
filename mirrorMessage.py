@nightyScript(
        name="Mirror Messages", 
        author="ogzl", 
        description="Mirrors messages & attachments from one channel/server to another", 
        usage="Automatically mirrors messages across servers"
)
def mirrorMessages():
    source_channel_id = 412414141241  # source
    target_channel_id = 14124141241414  # destination

    @bot.event
    async def on_message(message):
        if message.channel.id != source_channel_id:
            return
        if message.author.id == bot.user.id:
            return  

        target_channel = bot.get_channel(target_channel_id)
        if not target_channel:
            return

        content = f"**{message.author}:**"
        
        if message.content:
            content += f"\n{message.content}"

        if message.attachments:
            for attachment in message.attachments:
                size_kb = round(attachment.size / 1024, 1)
                content += f"\n📎 `{attachment.filename}` ({size_kb} KB)\n{attachment.url}"

        await target_channel.send(content)

mirrorMessages()
