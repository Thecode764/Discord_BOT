import discord
from discord.ext import commands
import time
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():

    await bot.change_presence(status=discord.Status.do_not_disturb)
    print('----------------------------------')
    print('bot runned')
    print('bot name: ' + bot.user.name)
    print('bot id: ' + str(bot.user.id))
    print('bot status: ' + str(bot.status))
    print('----------------------------------')
@bot.command()
async def Ale(ctx):
    await ctx.message.reply("""دومین گیووای ساخت وبسایت شما :tada:
                            برای شرکت پیام رو لایک کنید
                            معتبر تا: پنجشنبه
                            و پیشنیاز ها:
                            نداشتن وی آی پی
                            و وقتی این وبسایت ساخته شد از بقیه آن روی وی آی پی هم می تونه این کار رو بکنه
                            مورد اول کافیه
                            Power By: Discord.py""")
bot.run("MTE1ODQ0MTIwNDg0MTcxNzc5MQ.Gxn120.qq7XVkzt3ARokHVVbaZ-DTLHJbdtwd4J4LhHuc")
