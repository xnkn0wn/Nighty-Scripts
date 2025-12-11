@nightyScript(
    name="Channel Message Relay", 
    author="ogzl", 
    description="Relays messages from multiple channels to one or multiple target channels with source channel information.", 
    usage="Configure the source and target channel IDs."
)
def channelMessageRelay():
    CHANNEL_MAPPING = {
        525225252525252525: 5252525252525252523,  # Source:Target
    }

    @bot.listen()
    async def on_message(message):
        if message.channel.id in CHANNEL_MAPPING and message.author.id == bot.user.id:
            target_channel_id = CHANNEL_MAPPING[message.channel.id]
            target_channel = bot.get_channel(target_channel_id)

            if target_channel:
                await target_channel.send(
                    f"**[{message.channel.name}] {message.author.display_name}:** {message.content}"
                )
channelMessageRelay()
