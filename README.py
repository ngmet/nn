import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('$hello'):
        await message.channel.send(f'Привет Я бот  я покажу   тибе примери что делали с бутулками вот комади 1 $heh 2 $tam {client.user}!')
    elif message.content.startswith('$heh'):
        await message.channel.send(f'Общее количество пластика, загрязняющего океан, оценивается в более чем 25 миллионов тонн. Ранее считалось, что в океан попадает от четырех до двенадцати миллионов тонн пластика ежегодно. Согласно новым оценкам, этот показатель составляет не более 0,5 миллиона тонн{client.user}!')
    elif message.content.startswith('$tam'):
        await message.channel.send(f'https://youtube.com/shorts/kyBtnMHK9Fs?si=CPKCjEkMnLwIyrsb{client.user}!')


client.run("MTE1Mjk2MjA2MTYzNTE3ODYwNg.GSlDeG.iQbcTbauSOAwwCVnQH6csx69v0fSxm9oHOFSCo")
