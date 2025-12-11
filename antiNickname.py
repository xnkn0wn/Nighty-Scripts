@nightyScript(
    name="Anti Nick", 
    author="ogzl", 
    description="Changes Nick Back To Set Nick Globally", 
    usage="Enable/Disable"
)
def antinick():
    custom_nickname = "☆™"  #Nick here

    @bot.listen()
    async def on_member_update(before, after):
        if before.nick != after.nick:
            if after.nick != custom_nickname:
                try:
                    await after.edit(nick=custom_nickname)
                    showToast(
                        text=f"Nickname reverted to {custom_nickname} in {after.guild.name}",
                        type_="SUCCESS",
                        title="Nickname Change"
                    )
                except discord.Forbidden:
                    showToast(
                        text=f"Missing permissions to change nickname in {after.guild.name}.",
                        type_="ERROR",
                        title="Error"
                    )
                except Exception as e:
                    showToast(
                        text=f"An error occurred in {after.guild.name}: {str(e)}",
                        type_="ERROR",
                        title="Error"
                    )
antinick()
