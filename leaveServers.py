@nightyScript(
    name="Leave Servers",
    author="ogzl",
    description="Leaves all servers except whitelisted ones",
    usage="Use (prefix)leaveall"
)
def leaveAllServers():
    os.makedirs(f'{getScriptsPath()}/scriptData', exist_ok=True)
    script_config_path = f"{getScriptsPath()}/scriptData/leaveAllServers.json"
    
    def updateSetting(key, value):
        json.dump({**(json.load(open(script_config_path, 'r', encoding="utf-8", errors="ignore")) if os.path.exists(script_config_path) else {}), key: value}, open(script_config_path, 'w', encoding="utf-8", errors="ignore"), indent=2)

    def getSetting(key=None):
        return (lambda p: (settings := json.load(open(p, 'r', encoding="utf-8", errors="ignore"))) and settings.get(key) if key else settings)(script_config_path) if os.path.exists(script_config_path) else (None if key else {})

    def updateSelectedServers(selected: list):
        updateSetting("whitelisted_servers", selected)

    async def leaveServers():
        left_count = 0
        for guild in bot.guilds:
            if str(guild.id) not in las_whitelisted.selected_items:
                await guild.leave()
                left_count += 1
                await asyncio.sleep(2)
        return left_count

    servers_select_list = [{"id": "select_server", "title": "Select server(s)"}]
    for server in bot.guilds:
        server_row = {"id": str(server.id), "title": server.name, "iconUrl": "https://cdn.discordapp.com/embed/avatars/0.png"}
        if server.icon:
            server_row = {"id": str(server.id), "title": server.name, "iconUrl": server.icon.url}
        servers_select_list.append(server_row)

    # whitelist part
    las_tab = Tab(name='Leave servers', title="Leave all servers", icon="clean")
    las_container = las_tab.create_container(type="rows")
    las_card = las_container.create_card(height="full", width="full", gap=3)
    las_card.create_ui_element(UI.Text,
        content="Whitelisted servers",
        size="base",
        weight="bold",
        color="#FFFFFF",
        align="left"
    )
    las_whitelisted = las_card.create_ui_element(UI.Select, label="Select server(s)", full_width=True, selected_items=getSetting("whitelisted_servers"), disabled_items=['select_server'], mode="multiple", items=servers_select_list, onChange=updateSelectedServers)
    las_card.create_ui_element(UI.Button, label='Leave all servers', disabled=False, full_width=True, color="danger", onClick=leaveServers)

    @bot.command(name="leaveall", description="Leave all servers.")
    async def leaveall(ctx):
        await ctx.message.delete()
        left_count = await leaveServers()
        showToast(
            text=f"Left {left_count} servers", 
            type_="SUCCESS", 
            title="Leave Servers"
        )

    las_tab.render()

leaveAllServers()
