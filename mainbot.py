import discord
#from dotenv import load_dotenv
import os
import praw
import random
from discord.ext import commands,tasks
from random import choice
from itertools import cycle

#load_dotenv('.env')

#pwd = os.getenv('PASSWORD')

colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

client = commands.Bot(command_prefix="_")

#pwdfile = open("./pwd.txt")

#pwd = pwdfile.read(100)

#tokenfile = open("token.txt")

#token = tokenfile.read(100) 

status = ['_help','Trying to play music','Chillin', 'Searching wikipedia', 'Created By Joe Mama']

#online & status
@client.event
async def on_ready():
    change_status.start()
    print("Bot is online!")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

#ping 
@client.command(name='ping', help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'Latency: {round(client.latency *1000)}ms')

#hi
@client.command(name='hello',aliases=['hi','sup','how you doin'],help='this command returns a random welcome message')
async def hello(ctx):
    responses = ['***grumble*** Why did you wake me up?']
    await ctx.send(choice(responses))

#bye
@client.command(name='bye',aliases=['byee','tata','goodbye'],help='this command returns a random goodbye message')
async def die(ctx):
    responses = ["leavin so early?"]
    await ctx.send(choice(responses))

#college home page
@client.command(name='SAKEC', aliases = ['sakec'], help= 'this command returns the home page of SAKEC website')
async def home(ctx):
    await ctx.send(f"{ctx.author.mention}, https://www.shahandanchor.com/home/")

#college notice
@client.command(name='notice', help= 'this command returns the notice board site of SAKEC')
async def notice(ctx):
    await ctx.send(f"{ctx.author.mention}, https://www.shahandanchor.com/home/announcements-and-notices/")

#logout
@client.command(aliases=['disconnect','close','stopbot'])
async def logout(ctx):
    await ctx.send(f"{ctx.author.mention},I'm logging out :wave: ")
    await client.logout()

#logout error
@logout.error
async def logout_error(ctx,error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send(f"Error")
    else:
        raise error

#Reddit PRAW Library

reddit=praw.Reddit(client_id="fktd-wODc_b3v0KX5rwnDQ",client_secret="tSVe2DIcypnaT-1J7p6fdaKdKr3VOA",username="Effective_Collar1783",password= "reddit1107" ,user_agent="MultiBot",check_for_async=False)

#MEMES COMMAND

@client.command(name='meme', aliases = ["mem", "maymay"], help='Displays Meme')
async def meme(ctx):
    sbrdmemes = ("memes", "funny")
    subreddit= reddit.subreddit(random.choice(sbrdmemes))
    all_subs=[]

    hot=subreddit.hot(limit=100)
    for submission in hot:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    upvotes=random_sub.score
    comments=random_sub.num_comments
    mainlink=random_sub.permalink
    url=random_sub.url

    em=discord.Embed(url=f"https://www.reddit.com{mainlink}",title=name,color = random.choice(colors))
    em.set_footer(text=f"⬆️ {upvotes} | 💬 {comments}")
    em.set_image(url=url)
    await ctx.send(embed=em) 


#NEWS COMMAND

@client.command(name='news',help='Displays News')
async def news(ctx):
    subreddit=reddit.subreddit("InNews")
    all_subs=[]

    hot=subreddit.hot(limit=100)
    for submission in hot:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    upvotes=random_sub.score
    comments=random_sub.num_comments
    mainlink=random_sub.permalink
    url=random_sub.url

    em=discord.Embed(url=f"https://www.reddit.com{mainlink}",title=name,color = random.choice(colors))
    em.set_footer(text=f"⬆️ {upvotes} | 💬 {comments}")
    em.set_image(url=url)
    await ctx.send(embed=em)

#FACTS COMMAND

@client.command(name='facts',help='Displays Facts')
async def facts(ctx):
    subreddit=reddit.subreddit("facts")
    all_subs=[]

    top=subreddit.top(limit=100)
    for submission in top:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    upvotes=random_sub.score
    comments=random_sub.num_comments
    mainlink=random_sub.permalink
    url=random_sub.url

    em=discord.Embed(url=f"https://www.reddit.com{mainlink}",title=name,color = random.choice(colors))
    em.set_footer(text=f"⬆️ {upvotes} | 💬 {comments}")
    em.set_image(url=url)
    await ctx.send(embed=em)

#AWW COMMAND

@client.command(name='aww', aliases = ["cute", "kawai"], help='Displays awwie posts')
async def meme(ctx):
    subreddit= reddit.subreddit("aww")
    all_subs=[]

    hot=subreddit.hot(limit=100)
    for submission in hot:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    upvotes=random_sub.score
    comments=random_sub.num_comments
    mainlink=random_sub.permalink
    url=random_sub.url

    em=discord.Embed(url=f"https://www.reddit.com{mainlink}",title=name,color = random.choice(colors))
    em.set_footer(text=f"⬆️ {upvotes} | 💬 {comments}")
    em.set_image(url=url)
    await ctx.send(embed=em) 


#JOKES COMMAND

@client.command(name='joke', aliases = ["jokes", "jk"], help='Tells a dad joke')
async def joke(ctx):
    #sbrdjokes = ()
    subreddit= reddit.subreddit("dadjokes")
    all_subs=[]

    hot=subreddit.hot(limit=100)
    for submission in hot:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    upvotes=random_sub.score
    comments=random_sub.num_comments
    mainlink=random_sub.permalink
    url=random_sub.url

    em=discord.Embed(url=f"https://www.reddit.com{mainlink}",title=name, color = random.choice(colors))
    em.set_footer(text=f"⬆️ {upvotes} | 💬 {comments}")
    em.set_image(url=url)
    await ctx.send(embed=em)

#ADULT COMMANDS

@client.command(name='tharki',help='Displays Explicit Content 🔞🔞')
async def tharki(ctx):
    sbrdnsfw = ("holdthemoan", "NSFW_HTML5", "iWantToFuckHer", "PassionX", "RealGirls")
    subreddit= reddit.subreddit(random.choice(sbrdnsfw))
    all_subs=[]

    new=subreddit.new(limit=100)
    for submission in new:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    upvotes=random_sub.score
    comments=random_sub.num_comments
    mainlink=random_sub.permalink
    url=random_sub.url

    em=discord.Embed(url=f"https://www.reddit.com{mainlink}",title=name,color = random.choice(colors))
    em.set_footer(text=f"⬆️ {upvotes} | 💬 {comments}")
    em.set_image(url=url)
    await ctx.send(embed=em)

#HOLUP COMMAND

@client.command(name='holup',help='Displays Holup Memes')
async def holup(ctx):
    subreddit=reddit.subreddit("holup")
    all_subs=[]

    hot=subreddit.hot(limit=100)
    for submission in hot:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    upvotes=random_sub.score
    comments=random_sub.num_comments
    mainlink=random_sub.permalink
    url=random_sub.url

    em=discord.Embed(url=f"https://www.reddit.com{mainlink}",title=name,color = random.choice(colors))
    em.set_footer(text=f"⬆️ {upvotes} | 💬 {comments}")
    em.set_image(url=url)
    await ctx.send(embed=em)

    
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('E:\\VSC PROGRAMS\\DISCORD BOT\\Multi BOT\\cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("ODkxOTc2MDg0MzgyNDI5MTk1.Gu3joW.__1VyRBqtQU4Jlcwkb5ox2AUIyH9fnTbcDlpjg")