import os
from openai import OpenAI
from dotenv import load_dotenv

from app.services.action_handler import ActionHandleService

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SystemMessage:
    def handle_request(self, prompt, user_id):
        try:
            # Definir el prompt del usuario
            messages = []

            # Crear una instancia de ActionHandleService
            action_handle_service = ActionHandleService(user_id, prompt)
            messages = action_handle_service.handle_action()

            # Agregar el mensaje actual del usuario
            messages.append({"role": "user", "content": prompt})

            # Enviar los mensajes a la API de OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", messages=messages, max_tokens=550, temperature=0.1  # type: ignore
            )

            # Obtener la respuesta generada por el modelo
            respuesta_modelo = response.choices[0].message.content.strip()  # type: ignore

            return respuesta_modelo
        except Exception as e:
            raise Exception(f"Error en la API de OpenAI: {str(e)}")