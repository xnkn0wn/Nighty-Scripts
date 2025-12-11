@nightyScript(
    name="Message Deleter", 
    author="@ca0k", 
    description="Auto Deletes Your Messages", 
    usage="Automatically Deletes Your Messages After X Seconds"
)
def AutoMessageDeleter():
    os.makedirs(f'{getScriptsPath()}/scriptData', exist_ok=True)
    script_config_path = f"{getScriptsPath()}/scriptData/autoMessageDeleter.json"
    
    def updateSetting(key, value):
        json.dump({**(json.load(open(script_config_path, 'r', encoding="utf-8", errors="ignore")) if os.path.exists(script_config_path) else {}), key: value}, open(script_config_path, 'w', encoding="utf-8", errors="ignore"), indent=2)

    def getSetting(key=None):
        return (lambda p: (settings := json.load(open(p, 'r', encoding="utf-8", errors="ignore"))) and settings.get(key) if key else settings)(script_config_path) if os.path.exists(script_config_path) else (None if key else {})

    def updateInputState(input, invalid=False, error_message=None):
        input.invalid = invalid
        input.error_message = error_message

    def setDeleteDelay(value):
        if value.isdigit():
            updateInputState(md_input, False, None)
            updateSetting("delete_after", int(value))
        else:
            updateInputState(md_input, True, "Invalid number.")

    def setDeleteState(checked):
        updateSetting("state", checked)

    md_tab = Tab(name='Message Deleter', title="Auto delete messages", icon="trash")
    md_container = md_tab.create_container(type="rows")
    md_card = md_container.create_card(height="full", width="full", gap=3)
    md_toggle = md_card.create_ui_element(UI.Toggle, label="Auto Delete", onChange=setDeleteState, checked=getSetting("state") if getSetting("state") else False)
    md_input = md_card.create_ui_element(UI.Input, label="Delete after", required=True, onInput=setDeleteDelay, placeholder=str(getSetting("delete_after")))

    @bot.listen()
    async def on_message(message):
        if message.author == bot.user and getSetting("state") and getSetting("delete_after"):
            try:
                await asyncio.sleep(getSetting("delete_after"))
                await message.delete()
                showToast(
                    text=f"Message Deleted in {message.channel}",
                    type_="SUCCESS",
                    title="Auto Delete"
                )
            except:
                pass
    
    md_tab.render()

AutoMessageDeleter()
