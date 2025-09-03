import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True  # ต้องเปิดไว้ถึงจะอ่านข้อความได้
bot = commands.Bot(command_prefix="!", intents=intents)
load_dotenv()  # โหลดค่าใน .env

TOKEN = ("TOKEN")


@bot.event
async def on_ready():
    print(f"บอท {bot.user} ออนไลน์แล้ว!")

# ==========================
# 🔹 คำสั่งปกติ
# ==========================


@bot.command()
async def ping(ctx):
    await ctx.send("pong! 🏓")


@bot.command()
async def hello(ctx):
    await ctx.send(f"สวัสดี {ctx.author.mention} 👋")

# ==========================
# 📌 ตอบกลับข้อความผู้ใช้
# ==========================


@bot.event
async def on_message(message):
    # กันไม่ให้บอทตอบตัวเอง
    if message.author == bot.user:
        return

    content = message.content.lower()

    if "แนวข้อสอบ" in content:
        await message.channel.send("หาแนวข้อสอบได้จากเว็บมหาวิทยาลัย" +
                                   "หรือกลุ่มติวออนไลน์")

    elif "certificate digital" in content or "cert" in content:
        await message.channel.send("[TDGA]" +
                                   "(https://e-learning.dga.or.th/), " +
                                   "[CHULA MOOC]" +
                                   "(https://mooc.chula.ac.th/course/2), " +
                                   "[Coursera]" +
                                   "(https://www.coursera.org/)" +
                                   "การวัดระดับ WPM(words per minute), ")

    elif "บอท" in content:
        await message.channel.send("🙋‍♂️ เรียกผมหรือครับ?")

    # สำคัญ: ต้องมีบรรทัดนี้ เพื่อให้คำสั่ง prefix (!...) ยังทำงาน
    await bot.process_commands(message)


# ทำให้บอทรันตลอดเวลา (สำหรับ Replit)
keep_alive()

# รันบอทด้วย TOKEN ที่ซ่อนอยู่ใน Secrets ของ Replit
bot.run(os.getenv(TOKEN))
