@nightyScript(
    name="Auto Decline Calls",
    author="ogzl",
    description="Automatically declines incoming Discord calls",
    usage="Automatically runs in background"
)
def autoDeclineCalls():
    auto_decline_enabled = [True]
    
    @bot.command()
    async def testcall(ctx):
        await ctx.message.delete()
        showToast(
            text=f"Script active. Enabled: {auto_decline_enabled[0]}",
            type_="INFO",
            title="Status Check"
        )
    
    @bot.listen()
    async def on_socket_raw_receive(msg):
        if not auto_decline_enabled[0]:
            return
            
        try:
            import json
            
            # Only parse if it looks like JSON and contains CALL_CREATE
            if not isinstance(msg, str) or 'CALL_CREATE' not in msg:
                return
            
            showToast(
                text="CALL_CREATE detected!",
                type_="WARNING",
                title="Event Fired"
            )
            
            data = json.loads(msg)
            
            if data.get('t') != 'CALL_CREATE':
                return
            
            event_data = data.get('d', {})
            channel_id = event_data.get('channel_id')
            message_id = event_data.get('message_id')
            ringing = event_data.get('ringing', [])
            
            if channel_id:
                import aiohttp
                import asyncio
                headers = {"authorization": bot.http.token, "content-type": "application/json"}
                
                async with aiohttp.ClientSession() as session:
                    # Try up to 3 times with small delays
                    for attempt in range(3):
                        try:
                            # First stop the ringing
                            url1 = f"https://discord.com/api/v9/channels/{channel_id}/call/stop-ringing"
                            async with session.post(url1, headers=headers, json={}) as resp:
                                status1 = resp.status
                            
                            await asyncio.sleep(0.5)  # Small delay between requests
                            
                            # Then leave the call entirely
                            url2 = f"https://discord.com/api/v9/channels/{channel_id}/call"
                            async with session.delete(url2, headers=headers) as resp:
                                status2 = resp.status
                            
                            # If both succeeded, break out
                            if status1 in [200, 204] and status2 in [200, 204]:
                                showToast(
                                    text="Call declined successfully",
                                    type_="SUCCESS",
                                    title="Auto Decline"
                                )
                                break
                            elif status1 == 429 or status2 == 429:
                                # Rate limited, wait longer and retry
                                await asyncio.sleep(2)
                                continue
                            else:
                                showToast(
                                    text=f"Attempt {attempt+1}: {status1}, {status2}",
                                    type_="WARNING",
                                    title="Decline Status"
                                )
                                if attempt < 2:
                                    await asyncio.sleep(1)
                        except Exception as e:
                            if attempt < 2:
                                await asyncio.sleep(1)
                            else:
                                showToast(
                                    text=f"Failed after 3 attempts",
                                    type_="ERROR",
                                    title="Auto Decline"
                                )
                    
        except Exception as e:
            showToast(
                text=f"Error: {str(e)[:40]}",
                type_="ERROR",
                title="Script Error"
            )
    
    @bot.command()
    async def toggledecline(ctx):
        await ctx.message.delete()
        auto_decline_enabled[0] = not auto_decline_enabled[0]
        status = "enabled" if auto_decline_enabled[0] else "disabled"
        showToast(
            text=f"Auto-decline is now {status}",
            type_="SUCCESS",
            title="Auto Decline"
        )

autoDeclineCalls()
