import random

@nightyScript(
    name="Joke Bot", 
    author="ogzl", 
    description="Bot that tells random jokes", 
    usage="Use (prefix)joke to get a random joke"
)
def jokeBot():
    @bot.command()
    async def joke(ctx):
        await ctx.message.delete()
        jokes = [
            "Why don't skeletons fight each other? They don't have the guts.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "I used to play piano by ear, but now I use my hands.",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "I asked my dog what's two minus two. He said nothing.",
            "I told my computer I needed a break, and it froze.",
            "Why don’t oysters share their pearls? Because they’re shellfish.",
            "I have a fear of speed bumps, but I am slowly getting over it.",
            "Why do cows wear bells? Because their horns don’t work.",
            "I tried to catch some fog earlier. I mist.",
            "Why don’t skeletons fight each other? They don’t have the guts.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "I used to play piano by ear, but now I use my hands.",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "I asked my dog what's two minus two. He said nothing.",
            "I told my computer I needed a break, and it froze.",
            "Why don’t oysters share their pearls? Because they’re shellfish.",
            "I have a fear of speed bumps, but I am slowly getting over it.",
            "Why do cows wear bells? Because their horns don’t work.",
            "I walked into a bar... and then I realized it was a construction site.",
            "Why don’t skeletons ever fight each other? They don’t have the guts.",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
            "Why don’t eggs tell jokes? They’d crack each other up.",
            "What’s orange and sounds like a parrot? A carrot.",
            "What’s a skeleton’s least favorite room? The living room.",
            "Why did the coffee file a police report? It got mugged.",
            "What do you get when you cross a snowman and a vampire? Frostbite.",
            "What do you call fake spaghetti? An impasta.",
            "What do you call cheese that isn’t yours? Nacho cheese.",
            "I’m reading a book on anti-gravity. It’s impossible to put down.",
            "I’ve started investing in stocks: beef, chicken, and vegetable. One day I hope to be a bouillonaire.",
            "How do you organize a space party? You planet.",
            "What do you get when you cross a snowman and a dog? Frostbite.",
            "I told my wife she should embrace her mistakes. She gave me a hug.",
            "I’m on a whiskey diet. I’ve lost three days already.",
            "I walked into a bar… and then I realized it was a construction site.",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "I only know 25 letters of the alphabet. I don’t know y.",
            "I used to be a baker, but I couldn't make enough dough.",
            "I once got into a fight with a broken pencil. It was pointless.",
            "I can’t believe I got fired from the calendar factory. All I did was take a day off.",
            "I’m writing a book on reverse psychology. Don’t buy it.",
            "Why don’t some couples go to the gym? Because some relationships don’t work out.",
            "Why do cows have hooves instead of feet? Because they lactose.",
            "What did the grape do when it got stepped on? Nothing but let out a little wine.",
            "I went to buy some camo pants, but couldn’t find any.",
            "I used to be a baker, but I couldn’t make enough dough.",
            "I don’t trust stairs because they’re always up to something.",
            "How does Moses make his coffee? He brews it.",
            "Why did the chicken join a band? Because it had drumsticks!",
            "Why did the banana go to the doctor? Because it wasn’t peeling well.",
            "What did the tomato say to the other tomato? You’re ketchup.",
            "I went to a seafood disco last night… and pulled a mussel.",
            "What do you call a bear with no teeth? A gummy bear.",
            "I tried to start a hot air balloon business, but it never took off.",
            "What do you call a cow with no legs? Ground beef.",
            "I got a job as a human cannonball. The pay is lousy, but the benefits are great.",
            "I wasn’t originally going to get a brain transplant, but then I changed my mind.",
            "I’m trying to lose weight, but it’s not working. I guess I’ll just have to ketchup later.",
            "What do you call a snowman with a six-pack? An abdominal snowman.",
            "I got a reversible jacket for Christmas. I can’t wait to see how it turns out.",
            "How do you make holy water? You boil the hell out of it.",
            "What do you call a fish wearing a bowtie? Sofishticated.",
            "What did one wall say to the other? “I’ll meet you at the corner.”",
            "I couldn’t figure out why I got fired from the calendar factory. All I did was take a day off.",
            "Why did the gym close down? It just didn’t work out.",
            "What did the grape say when it got stepped on? Nothing, but it let out a little wine."
        ]
        selected_joke = random.choice(jokes)
        await ctx.send(f"{selected_joke}")
        showToast(
            text="Nice Joke! HaHa", 
            type_="SUCCESS", 
            title="Joke Sent"
        )

jokeBot()
