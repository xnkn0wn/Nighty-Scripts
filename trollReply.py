import random
import asyncio

@nightyScript(
    name="Troll Reply", 
    author="ogzl", 
    description="Troll a user and roast them with funny responses", 
    usage="Use .trollreply <userid>"
)
def trollReply():
    roasts = [
        "Did you just say that? Was that even a real sentence?",
        "Wow, that was as useful as a screen door on a submarine.",
        "Are you always this clueless or is today a special day?",
        "Oh, you must be a limited edition, because there’s only one like you—and that’s enough.",
        "Was that a joke? Because the punchline was missed, my friend.",
        "You're the human version of a participation trophy.",
        "Do you want to hear a secret? Everyone is secretly wondering what goes on in your mind.",
        "Your IQ is so low, even Google can’t find it.",
        "Is that your final answer, or do you need more time to process?",
        "You're like a cloud. When you disappear, it's a beautiful day.",
        "Is your drama class auditioning for the lead role in 'I’m Always Right'?",
        "Your brain must be a pretty lonely place, huh?",
        "You remind me of a software update—always popping up at the worst time.",
        "If I had a dollar for every time you said something stupid, I’d be rich.",
        "You're not stupid; you just have bad luck thinking.",
        "Your parents must be so proud... of your ability to fail spectacularly.",
        "I’m not saying you’re dumb, but your brain is like a mobile hotspot... everyone’s disconnected.",
        "You have the same amount of common sense as a rocking chair.",
        "If I had a dollar for every time you’ve been wrong, I could retire early.",
        "Your humor is so dry, even a desert would say 'take it easy'.",
        "You must be the human equivalent of a broken pencil: pointless.",
        "There’s an entire generation of people who think you’re a role model for bad decisions.",
        "You’ve got a face for radio and a voice for silent movies.",
        "You couldn't pour water out of a boot if the instructions were on the heel.",
        "You know, your charm could kill. It's a good thing you're not dangerous.",
        "I’m not saying you’re slow, but the tortoise just passed you and waved.",
        "Your social skills are as effective as a screen door on a submarine.",
        "I can't even begin to explain how wrong you are, but I’ll try: you’re utterly lost.",
        "Did it hurt? When you fell from the top of the genius tree and hit every branch on the way down?",
        "If I had a nickel for every time you said something that made no sense, I’d have enough for a spaceship to get away from you.",
        "I'm not saying you're a genius, but if I were you, I'd be very afraid of any form of electricity.",
        "Your brain has more cracks than my phone screen.",
        "You bring so little to the table, even the crumbs are embarrassed to be seen with you.",
        "You could win an award for the most unnecessary comment.",
        "How does it feel to be the human version of a WiFi signal that never works?",
        "You should wear a sign that says 'No Refunds' because that’s the only thing worth offering you.",
        "Your ideas are like expired milk—putrid and not welcome here.",
        "If your brain was made of dynamite, it wouldn’t be enough to blow your hat off.",
        "You're like a participation trophy—nobody cares, but they feel obligated to give it to you.",
        "Is your brain on vacation? I can’t find it anywhere.",
        "You couldn't fight your way out of a paper bag, let alone a conversation.",
        "You remind me of a cloud. You’re everywhere, but you never do anything useful.",
        "You'd be the last person I’d call for help, but the first person I’d call for an entertainment disaster.",
        "Do you ever think before you speak? No? I didn’t think so.",
        "I’d explain it to you, but I’m still waiting for my IQ to drop enough to relate.",
        "Are you just trolling me, or is this your best version of reality?",
        "I’m pretty sure even a broken clock is more accurate than anything that comes out of your mouth.",
        "If there was an award for confusion, you'd win it every time.",
        "I’ve heard smarter things from a potato.",
        "You're a genius... in the same way a paper airplane is a fighter jet.",
        "You really need a new hobby. Preferably one where you can’t harm others with your opinions.",
        "It's cute how you try so hard to seem relevant, but you're as out of place as a fish in a desert.",
        "Your logic is like a labyrinth; nobody’s ever going to find their way out.",
        "Have you ever heard of self-awareness? You might want to try it sometime.",
        "You’re like the silent alarm at the bank – completely useless.",
        "If only you were as good at thinking as you are at making no sense.",
        "Your argument is like a broken pencil – pointless.",
        "When you speak, it’s like watching a car crash in slow motion – you don’t want to look, but you can’t help it.",
        "You make a great case for why some people should never be allowed to talk.",
        "You're not stupid. You're just... aggressively average.",
        "You could be a great comedian if the world was deaf and blind.",
        "You're so clueless, you make the average person look like Einstein.",
        "Are you sure you're not the one who needs help? Your thoughts seem to get stuck halfway.",
        "It’s adorable how confident you are in your completely misguided opinions.",
        "You’re like a fire drill—unwanted, unnecessary, and everyone’s just waiting for it to end.",
        "Your ideas are like unwashed socks—stale, smelly, and no one wants to be near them.",
        "I’d give you some advice, but I’m pretty sure you wouldn’t follow it even if it was life-changing.",
        "You’re the reason people have trust issues.",
        "If you were any dumber, I’d need a helmet just to be in the same room as you.",
        "You're so unoriginal, even plagiarism wouldn’t want to take credit for you.",
        "You're like a cracked phone screen—no matter how many times you touch it, you just don’t work properly.",
        "You must have an incredible talent for saying the dumbest thing at the worst time.",
        "I could listen to you talk for hours, but I’d prefer a root canal instead.",
        "Are you sure your brain’s not on vacation? Because it’s not doing any work right now.",
        "You’ve got the intellect of a potato. Not even the smartest potato.",
        "I don’t know who needs to hear this, but it’s not you.",
        "The fact that you're allowed to have opinions is more offensive than anything you’ve ever said.",
        "You’re not the sharpest tool in the shed... You’re more like a dull spoon.",
        "Your brain is like a treasure chest—nothing inside, but people still look.",
        "You’re the human embodiment of a pop-up ad.",
        "Congratulations, you've successfully convinced me that words can hurt.",
        "If you were any more useless, you'd be a negative asset."
    ]
    comeback_lines = {
        "hello": "Is that the best you can come up with? Try harder!",
        "good": "I didn’t know ‘good’ could sound so boring.",
        "bye": "Goodbye? Are you leaving because you're scared of my roast?",
        "lol": "Haha, yeah, real funny. Keep laughing, though it’s cute.",
        "yes": "Wow, you said 'yes'. That’s deep. I’m really impressed.",
        "no": "No? What’s that supposed to mean? Are you sure about that?",
        "brb": "Yeah, I’ll be here waiting. But I bet you won’t bring anything interesting when you return.",
        "okay": "Oh wow, 'okay'. What a groundbreaking statement!",
        "thanks": "Thanks? Is that your way of asking for more roasts? You just made it worse.",
        "why": "Why? Now that’s a real question, but I’m sure you won’t like the answer.",
        "help": "Help? From you? I’m honestly scared of what you might try to 'help' with.",
        "sorry": "Sorry? You should be! That last message was a disaster.",
        "haha": "Haha, you're just making it worse with your laughter, my friend.",
        "please": "Please? That’s cute. But no, I’m not giving you any mercy."
    }
    @bot.command()
    async def trollreply(ctx, user_id: int):
        await ctx.message.delete()
        user = await bot.fetch_user(user_id)

        if not user:
            await ctx.send("I couldn't find that user, are you sure you typed the ID correctly?")
            return
        def check(message):
            return message.author.id == user_id
        while True:
            try:
                message = await bot.wait_for('message', check=check, timeout=60.0)
                roast_message = random.choice(roasts)  
                for keyword, comeback in comeback_lines.items():
                    if keyword.lower() in message.content.lower():
                        roast_message = comeback
                        break  
                await message.channel.send(f"{user.display_name}, {roast_message}")
                await message.add_reaction("😂")
                await message.add_reaction("💀")
                await message.add_reaction("🤡")
                await message.add_reaction("☠️")
            
            except asyncio.TimeoutError:
                break 

trollReply()
