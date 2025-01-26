import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    #don't react to messages from bot itself
    if message.author == client.user:
        return
    
    if message.content.startswith('$test'):
        await message.channel.send("chris rey smells like blue cheese")

with open("token.txt", 'r') as file:
    token = file.read()

client.run(token)