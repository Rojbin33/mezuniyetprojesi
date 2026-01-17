import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from config import Token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ===== SIKÇA SORULAN SORULAR =====
FAQ = {
    "alışveriş": "Alışveriş yapmak için, ilgilendiğiniz ürünü seçip "
                 "'Alışveriş Sepetine Ekle' butonuna tıklayın. "
                 "Ardından sepetinize giderek satın alma işlemini tamamlayın.",

    "siparişimin durumu": "Siparişinizin durumunu öğrenmek için hesabınıza giriş yapın "
                          "ve 'Siparişlerim' bölümüne gidin.",

    "sipariş iptal": "Siparişinizi iptal etmek için en kısa sürede müşteri hizmetlerimizle "
                     "iletişime geçin. Gönderilmeden önce yardımcı oluruz.",

    "hasarlı": "Hasarlı ürün aldıysanız hemen müşteri hizmetleriyle iletişime geçin "
               "ve hasarın fotoğraflarını paylaşın. Değişim veya iade yapılır.",

    "teknik destek": "Teknik destekle internet sitemizdeki telefon numarası üzerinden "
                     "ya da sohbet robotumuz aracılığıyla iletişime geçebilirsiniz.",

    "teslimat": "Evet, ödeme sayfasında teslimat yöntemini değiştirebilirsiniz. "
                "Uygun seçenekler orada listelenir."
}

# ===== BOT HAZIR =====
@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")

# ===== MESAJLARI DİNLE =====
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower()

    for key, answer in FAQ.items():
        if key in msg:
            await message.channel.send(answer)
            return

    await bot.process_commands(message)

# ===== /sss KOMUTU =====
@bot.command(name="sss")
async def sss(ctx):
    embed = discord.Embed(
        title="📌 Sıkça Sorulan Sorular",
        color=discord.Color.blue()
    )

    for soru in FAQ.keys():
        embed.add_field(name="❓", value=soru.capitalize(), inline=False)

    await ctx.send(embed=embed)

bot.run(Token)
