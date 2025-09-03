import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
from dotenv import load_dotenv

# โหลดค่าใน .env ก่อน
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"🤖 บอท {bot.user} ออนไลน์แล้ว!")

# คำสั่งปกติ


@bot.command()
async def ping(ctx):
    await ctx.send("pong! 🏓")


@bot.command()
async def hello(ctx):
    await ctx.send(f"สวัสดี {ctx.author.mention} 👋")

# ตอบกลับข้อความผู้ใช้


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    if "แนวข้อสอบ" in content:
        await message.channel.send("📚 หาแนวข้อสอบได้จากเว็บมหาวิทยาลัยหรือกลุ่มติวออนไลน์")

    elif "certificate digital" in content or "cert" in content:
        embed = discord.Embed(
            title="📜 แหล่ง Certificate Digital", color=discord.Color.green())
        embed.add_field(
            name="TDGA", value="https://e-learning.dga.or.th/", inline=False)
        embed.add_field(name="CHULA MOOC",
                        value="https://mooc.chula.ac.th/course/2", inline=False)
        embed.add_field(name="Coursera",
                        value="https://www.coursera.org/", inline=False)
        embed.add_field(
            name="WPM", value="การวัดระดับ WPM(words per minute)", inline=False)
        await message.channel.send(embed=embed)

    elif "บอท" in content:
        await message.channel.send("🙋‍♂️ เรียกผมหรือครับ?")

    await bot.process_commands(message)

# รันบอทบน Replit ตลอดเวลา
keep_alive()
bot.run(TOKEN)
