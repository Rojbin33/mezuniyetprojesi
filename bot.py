import discord
from discord.ext import commands
from config import Token

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

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

# ===== ANAHTAR KELİMELER =====
TEKNIK_KELIMELER = ["site", "ödeme", "hata", "giriş", "çöküyor"]
SATIS_KELIMELER = ["ürün", "kargo", "iade", "fiyat", "stok"]

# ===== SAHTE VERİTABANI =====
def save_to_db(message, department):
    print(f"[KAYIT] {message.author} | {department} | {message.content}")

# ===== BOT HAZIR =====
@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")

# ===== MESAJ İŞLEME =====
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower()

    # SSS
    for key, answer in FAQ.items():
        if key in msg:
            await message.channel.send(answer)
            return

    # Teknik
    for kelime in TEKNIK_KELIMELER:
        if kelime in msg:
            await message.channel.send("🔧 Teknik destek ekibine yönlendirildiniz.")
            save_to_db(message, "Teknik Destek")
            return

    # Satış
    for kelime in SATIS_KELIMELER:
        if kelime in msg:
            await message.channel.send("🛒 Satış departmanına yönlendirildiniz.")
            save_to_db(message, "Satış Departmanı")
            return

    await message.channel.send("Talebiniz alınmıştır.")
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

# ===== SESLİ DESTEK KOMUTU =====
@bot.command(name="ses")
async def ses(ctx):
    if not ctx.author.voice:
        await ctx.send("❌ Bir ses kanalında olmalısın.")
        return

    channel = ctx.author.voice.channel
    await channel.connect()

    await ctx.send(
        "🎙️ **Sesli destek modu aktif!**\n"
        "Konuşmalar ileride yazıya çevrilerek analiz edilebilir şekilde tasarlanmıştır."
    )



bot.run(Token)
