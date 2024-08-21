import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True  # Activer les événements liés aux salons vocaux

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')

@bot.event
async def on_voice_state_update(member, before, after):
    # Vérifie si le membre a rejoint un salon vocal
    if before.channel is None and after.channel is not None:
        # Si le membre rejoint le salon "⚠Urgent⚠"
        if after.channel.name == "⚠Urgent⚠":
            channel = discord.utils.get(member.guild.text_channels, name='le-salon-des-notifs')  # Remplacer par le nom de votre salon texte
            if channel:
                await channel.send(f'@everyone {member.name} a rejoint le salon vocal ⚠Urgent⚠ !')
        
        # Si le membre rejoint le salon "💼 Work"
        elif after.channel.name == "💼 Work":
            channel = discord.utils.get(member.guild.text_channels, name='le-salon-des-notifs')  # Remplacer par le nom de votre salon texte
            if channel:
                await channel.send(f'{member.name} travaille dans le salon vocal 💼 Work.')

# Remplacez 'your_token_here' par votre token de bot
bot.run('le truc')
