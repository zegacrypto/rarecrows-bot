import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CallbackContext, CallbackQueryHandler 

# Configurar logging
logging.basicConfig(level=logging.INFO) 

# Token de tu bot
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '8332445670:AAFt3E4bmGSAaegKAFiAqLBBoe566MOGkOQ')
async def welcome_message(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("🎮 JUGAR en Telegram", url="https://t.me/rarecrows_bot?start=ref_65990447765414")],
        [InlineKeyboardButton("🌐 JUGAR en Web", url="https://beta.rarecrows.io?ref=65990447765414")],
        [InlineKeyboardButton("📚 Guía Rápida", callback_data="quick_guide")],
        [InlineKeyboardButton("🛡️ Tips Defensa", callback_data="defense_tips")],
        [InlineKeyboardButton("📜 Reglas Grupo", callback_data="rules")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = """
¡🌾 **Bienvenido/a a Rarecrows!** 🙌 

**🔥 NOVEDAD IMPORTANTE:**
¡Ahora **GANAS RECOMPENSAS** solo por participar en el chat de la comunidad! 🎁 

**🎯 Juego exclusivo de colección:**
• Cultiva y defiende tu granja
• Colecciona espantapájaros únicos
• Chat activo = Recompensas en juego 

🔗 **Tus enlaces con bonus:**
¡Ventajas extras al empezar! 

👇 **Explora las opciones:**
    """
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown') 

async def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == "quick_guide":
        guide_text = """
**📖 GUÍA BÁSICA OFICIAL - RARECROWS** 

🌱 **SISTEMA DE CULTIVOS:**
• Cultivos básicos con diferentes tiempos
• Sistema de rotación de cultivos
• Mejoras de eficiencia disponibles 

⚡ **MECÁNICAS PRINCIPALES:**
• Colecciona espantapájaros únicos
• Desbloquea logros especiales
• Participa en eventos exclusivos 

🎮 **PROGRESIÓN:**
• Comienza con cultivos simples
• Desbloquea nuevas áreas
• Colecciona todos los rarecrows
        """
        await query.edit_message_text(guide_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ Volver", callback_data="back_to_welcome")]
        ]))
    
    elif query.data == "defense_tips":
        defense_text = """
**🛡️ SISTEMA DE DEFENSA - RARECROWS** 

⚠️ **AMENAZAS:**
• **Cuervos**: Atacan tus cultivos regularmente
• **Duendes**: Roban tus recursos periódicamente 

🔒 **PROTECCIÓN:**
• **Espantapájaros**: Tu principal defensa
• Cada rarecrow ofrece protección única
• Colócalos estratégicamente en tu granja 

🛠️ **ESTRATEGIAS:**
• Revisa defensas frecuentemente
• Mejora tus espantapájaros
• Diversifica tu colección defensiva
        """
        await query.edit_message_text(defense_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ Volver", callback_data="back_to_welcome")]
        ]))
    
    elif query.data == "rules":
        rules_text = """
**📜 REGLAS DE LA COMUNIDAD RARECROWS** 

✅ **PERMITIDO:**
• Compartir experiencias y progreso en el juego
• Hacer preguntas sobre mecánicas de Rarecrows
• Compartir tips y estrategias verificadas
• Ayudar a nuevos jugadores 

❌ **PROHIBIDO:**
• Spam o publicidad no relacionada con el juego
• Lenguaje ofensivo, discriminación o toxicidad
• Compartir enlaces de referido de otras personas 

🌟 **OBJETIVO:**
Crear una comunidad positiva y colaborativa
        """
        await query.edit_message_text(rules_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ Volver", callback_data="back_to_welcome")]
        ]))
    
    elif query.data == "back_to_welcome":
        keyboard = [
            [InlineKeyboardButton("🎮 JUGAR en Telegram", url="https://t.me/rarecrows_bot?start=ref_65990447765414")],
            [InlineKeyboardButton("🌐 JUGAR en Web", url="https://beta.rarecrows.io?ref=65990447765414")],
            [InlineKeyboardButton("📚 Guía Rápida", callback_data="quick_guide")],
            [InlineKeyboardButton("🛡️ Tips Defensa", callback_data="defense_tips")],
            [InlineKeyboardButton("📜 Reglas Grupo", callback_data="rules")]
        ]
        welcome_text = """
¡🌾 **Bienvenido/a a Rarecrows!** 🙌 

**🔥 NOVEDAD IMPORTANTE:**
¡Ahora **GANAS RECOMPENSAS** solo por participar en el chat de la comunidad! 🎁 

**🎯 Juego exclusivo de colección:**
• Cultiva y defiende tu granja
• Colecciona espantapájaros únicos
• Chat activo = Recompensas en juego 

🔗 **Tus enlaces con bonus:**
¡Ventajas extras al empezar! 

👇 **Explora las opciones:**
        """
        await query.edit_message_text(welcome_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown') 

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_message))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Rarecrows Asistente ESP - ACTIVO 24/7!")
    application.run_polling() 

if __name__ == '__main__':
    main()
