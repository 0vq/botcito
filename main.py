import discord
import os

# Configuración de los intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'¡Hemos iniciado sesión como {client.user}!')

@client.event
async def on_message(message):
    # No queremos que el bot se responda a sí mismo
    if message.author == client.user:
        return

    if message.content.startswith('!hola'):
        await message.channel.send('¡Hola! Soy un bot.')

# Obtenemos el token desde una variable de entorno
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN:
    client.run(TOKEN)
else:
    print("Error: No se encontró el token. Asegúrate de configurar la variable de entorno DISCORD_TOKEN.")
