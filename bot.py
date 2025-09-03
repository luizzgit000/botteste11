import discord
from discord.ext import commands
import os
import asyncio

TOKEN_FILE = "token.txt"

# Função para obter ou criar token
def get_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            return f.read().strip()
    else:
        token = input("Digite o token do bot (será salvo para próximas vezes): ")
        with open(TOKEN_FILE, "w") as f:
            f.write(token)
        return token

# Função para editar token
def edit_token():
    token = input("Digite o novo token do bot: ")
    with open(TOKEN_FILE, "w") as f:
        f.write(token)
    print("Token atualizado com sucesso! Reinicie o script para usar o novo token.")
    return token

# Configurações do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Função para enviar mensagem interativa
async def enviar_mensagem():
    await bot.wait_until_ready()
    try:
        guild_id = int(input("Digite o ID do servidor: "))
        guild = bot.get_guild(guild_id)
        if not guild:
            print("Servidor não encontrado ou o bot não está nele!")
            return
        
        channel_id = int(input("Digite o ID do canal: "))
        channel = guild.get_channel(channel_id)
        if not channel:
            print("Canal não encontrado!")
            return
        
        mensagem = input("Digite a mensagem que quer enviar: ")
        await channel.send(mensagem)
        print(f"Mensagem enviada para {channel.name} ✅\n")
    except ValueError:
        print("ID inválido! Digite apenas números.\n")
    except Exception as e:
        print(f"Ocorreu um erro: {e}\n")

# Menu principal
async def main_menu():
    await bot.wait_until_ready()
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Enviar mensagem")
        print("2. Editar token")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            await enviar_mensagem()
        elif escolha == "2":
            edit_token()
        elif escolha == "3":
            print("Saindo...")
            await bot.close()
            break
        else:
            print("Opção inválida!")

# Pega o token (salvo ou novo)
token = get_token()

# Executa o bot
bot.loop.create_task(main_menu())
bot.run(token)
