# Import calls
import os
import random 
import discord 
# Pulls classes from imports
from discord.ext import commands 
from discord.ext.commands import bot 
from dotenv import load_dotenv

# Calls class to initiatie loading of ENV file (explained why next)
load_dotenv()

# Loads toke for the bot generated in the Discord dev portal (pulled from ENV file so it is not public in the source code)
TOKEN = os.getenv('DISCORD_TOKEN')

# Set the prefix for bot commands
bot = commands.Bot(command_prefix='!')

# Calls command when a user joins the Discord channel
@bot.event
async def on_ready():
    print(f'{bot.user} welcome muthafucka!')

# Calls command to DM the same user from above
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Yo {member.name}, this is Beetlejuice! From Howard Stern Show! Type C! for commands!')

# When someone uses the !Quote command, randomly send a quote from the list below    
@bot.command(name = 'Quote')
async def juice_quote(ctx):
    beet_quotes = [
        "I don' shit on myself no more you black skinny fat fuck.",
        "I don' know nuffin'. I don' wanna know nuffin.'",
        "Gotta wake up in the mornin' and eat coffee, bruvah.",
        "Goo for you pal.",
        "I don't pay too much to get fucked!",
        "The whole bitch suck my dick.",
        "When I'm drinkin'? Yeah. When I'm drinkin'? Nah!",
        "I'm about hundred feet tall.",
        "Next day, the muthafucka was dead!",
        "I weigh almost six hundred pounds!",
        "I'm a comic, man!",
        "Probably 'cause yous a piece of shit.",
        "Cost me at least fuckin' two thousand dollars, five-five hundred grand.",
        "I own whores.",
        "I'm a muthafuckin' pimp.",
        "Yea, I got to fuck your wife too cause she looks like Batman. On a fuckin' stick.",
        "Howard Stern? I just hang 'em like a little bird, flip 'em over and just lay 'em hangin'. Let a little monkey, get a little banana shoots...walk down the streets...like a banana!",
        "A cuppa times",
        "Ah, look at this piece of shit!",
        "Nuttin' new bruvah! Jus' chillin'!",
        "I smack his ass like a bitch!",
        "You ain't fuckin' uhm, uhm...what you call dat shit? The Hulk, muthafucka!"
        "Aye I sit back an' get laid bruvah",
        "I'm in the game, baby!",
        "I got at least about five-fifty grand.",
        "Oh, they goin' pay me! Who's tha one with tha tattoo!",
    ]
    
    response = random.choice(beet_quotes)
    await ctx.send(response)

# When someone uses the !Beet command randomly send one the messages below   
@bot.command(name = 'Beet')
async def response(ctx):
    beet_response = [
        "Yo, this is Beetlejuice! From Howard Stern Show! Type !C for commands!",
        "I don't know what this shit is! Type !C for commands!",
        "What do you mean Sean? Type !C for commands!",
        "Fuck you ya asshole. Type !C for commands!",
        "Who, me? Type !C for commands!"
    ]

    response = random.choice(beet_response)
    await ctx.send(response)

# When someone uses the !Spellred command send the text below
@bot.command(name = 'Spellred')
async def red(ctx):
    red = ('L-E-T-E-R!')
    await ctx.send(red)

# When someone uses the !Carro command send the text below
@bot.command(name = 'Carrot')
async def carrot(ctx):
    carrot = ("Carrot? I think is uh...I think is uh...I think it's a carrot. Uh... I don' know about carrots. I don' know nothin' 'bout 'dat.")
    await ctx.send(carrot)

# When someone uses the !1-1 command send the text below
@bot.command(name = '1-1')
async def math(ctx):
    math = ('Equals? 35.')
    await ctx.send(math)

# When someone uses the !1-1 command send the text below
@bot.command(name = 'C')
async def c(ctx):
    C = "See below for commmands!:\nType !Quote for some Beetlejuice quotes ya dickhead!\nType !Spellred to have me spell red ya jerkoff!\nType !Carrot to have me tell you some carrot facts ya piece a shit!\nType !1-1 and I'll do some maths!\nType !Coke and I'll send ya a nice pic bitch!"
    await ctx.send(C)


# When someone uses the !Coke command send the picture
@bot.command(name = 'Coke')
async def coke(ctx):
    await ctx.send(file=discord.File('Pictures/coke.jpg')) 
 
# Runs the bot's token        
bot.run(TOKEN)

 