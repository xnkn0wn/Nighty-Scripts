@nightyScript(
    name="Slowmode Notifier", 
    author="ogzl", 
    description="Sends a message to a channel when slowmode resets", 
    usage="Use (prefix)notify"
)
def slowmodeNotifier():
    running = {}

    @bot.command()
    async def notify(ctx, channel_id: int, *, message: str):
        await ctx.message.delete()
        channel = bot.get_channel(channel_id)
        if not channel:
            showToast(
                text="Invalid Channel ID", 
                type_="ERROR", 
                title="Channel Not Found"
            )
            return
        
        if channel_id in running:
            showToast(
                text="Notifier already running for this channel", 
                type_="ERROR", 
                title="Duplicate Command"
            )
            return

        running[channel_id] = True
        slowmode_delay = channel.slowmode_delay
        
        if slowmode_delay == 0:
            await channel.send(message)
        else:
            def check(msg):
                return msg.channel.id == channel.id and msg.author.id == bot.user.id
            
            while running[channel_id]:
                await channel.send(message)
                try:
                    await bot.wait_for('message', check=check, timeout=slowmode_delay + 1)
                except asyncio.TimeoutError:
                    continue
        
        del running[channel_id]

    @bot.command()
    async def stopnotify(ctx, channel_id: int):
        if channel_id in running:
            running[channel_id] = False
            showToast(
                text="Notifier stopped", 
                type_="SUCCESS", 
                title="Stopped"
            )
        else:
            showToast(
                text="No notifier running for this channel", 
                type_="ERROR", 
                title="Not Found"
            )

slowmodeNotifier()
