@nightyScript(
    name="Message Deleter", 
    author="@ogzl", 
    description="Auto Deletes Messages", 
    usage="Automatically Deletes Your Messages After X Seconds"
)
def AutoMessageDeleter():

    @bot.listen()
    async def on_message(message):
        if message.author != bot.user:
            return
        await asyncio.sleep(5)
        try:
            await message.delete()
        except:
            pass

        showToast(
            f"Message Deleted in {getChannelInfo(message.channel)}",
            type_="SUCCESS",
            title="Auto Delete"
        )


AutoMessageDeleter()
