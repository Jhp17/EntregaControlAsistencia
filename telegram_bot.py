import os
from datetime import datetime
import requests

from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
API_URL = "http://127.0.0.1:8000"

# Estados de conversación
ESPERANDO_IDENTIFICACION = 1
ESPERANDO_NOMBRE = 2
ESPERANDO_ASIGNATURA = 3
ESPERANDO_ESTADO = 4


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()

    await update.message.reply_text(
        "👋 ¡Hola! Soy el bot de Control de Asistencias.\n\n"
        "Usa /asistencia para registrar una asistencia."
    )


async def asistencia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    context.user_data["paso"] = ESPERANDO_IDENTIFICACION

    await update.message.reply_text(
        "📝 Vamos a registrar tu asistencia.\n\n"
        "👤 Escribe tu número de identificación:"
    )


async def recibir_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    texto = update.message.text.strip()
    paso = context.user_data.get("paso")

    if paso == ESPERANDO_IDENTIFICACION:
        context.user_data["identificacion"] = texto
        context.user_data["paso"] = ESPERANDO_NOMBRE

        await update.message.reply_text(
            "✅ Identificación recibida.\n\n"
            "👤 Ahora escribe tu nombre completo:"
        )

    elif paso == ESPERANDO_NOMBRE:
        context.user_data["nombre"] = texto
        context.user_data["paso"] = ESPERANDO_ASIGNATURA

        await update.message.reply_text(
            "✅ Nombre recibido.\n\n"
            "📚 Escribe el nombre de la asignatura:"
        )

    elif paso == ESPERANDO_ASIGNATURA:
        context.user_data["asignatura"] = texto
        context.user_data["paso"] = ESPERANDO_ESTADO

        teclado = [
            ["🟢 PRESENTE"],
            ["🟡 TARDE"],
            ["🔴 AUSENTE"]
        ]

        await update.message.reply_text(
            "📋 Selecciona tu estado:",
            reply_markup=ReplyKeyboardMarkup(
                teclado,
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

    elif paso == ESPERANDO_ESTADO:
        estado = texto.upper()

        if "PRESENTE" in estado:
            estado = "PRESENTE"
        elif "TARDE" in estado:
            estado = "TARDE"
        elif "AUSENTE" in estado:
            estado = "AUSENTE"
        else:
            await update.message.reply_text(
                "❌ Estado no válido.\n\n"
                "Selecciona PRESENTE, TARDE o AUSENTE."
            )
            return

        ahora = datetime.now()

        datos = {
            "id": int(ahora.timestamp()),
            "identificacion": context.user_data["identificacion"],
            "nombre": context.user_data["nombre"],
            "asignatura": context.user_data["asignatura"],
            "fecha": ahora.strftime("%Y-%m-%d"),
            "hora": ahora.strftime("%H:%M:%S"),
            "estado": estado
        }

        try:
            respuesta = requests.post(
                f"{API_URL}/asistencia/",
                json=datos,
                timeout=10
            )

            if respuesta.status_code in [200, 201]:
                await update.message.reply_text(
                    "✅ ¡Asistencia registrada correctamente!\n\n"
                    f"👤 Nombre: {datos['nombre']}\n"
                    f"🪪 Identificación: {datos['identificacion']}\n"
                    f"📚 Asignatura: {datos['asignatura']}\n"
                    f"📅 Fecha: {datos['fecha']}\n"
                    f"🕐 Hora: {datos['hora']}\n"
                    f"📋 Estado: {datos['estado']}"
                )

                context.user_data.clear()

            else:
                await update.message.reply_text(
                    "❌ No se pudo registrar la asistencia.\n\n"
                    f"Error de la API: {respuesta.status_code}\n"
                    f"{respuesta.text}"
                )

        except requests.exceptions.RequestException as error:
            await update.message.reply_text(
                "❌ No se pudo conectar con la API.\n\n"
                "Verifica que FastAPI esté ejecutándose."
            )

            print(f"Error de conexión: {error}")


def main():
    if not TOKEN:
        print("❌ No se encontró TELEGRAM_TOKEN en el archivo .env")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("asistencia", asistencia))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        recibir_mensaje
    ))

    print("🤖 Bot de Telegram iniciado...")
    app.run_polling()


if __name__ == "__main__":
    main()