# app/services/openai_service.py

from app.repos.conversation_repo import ConversacionRepo
from app.services.system_message import SystemMessage

class OpenAIService:

    def __init__(self):
        pass

    def handle_request(self, prompt, from_number):
        # Definir el prompt del usuario
        try:
            # Imprimir el prompt del usuario
            print(f"Usuario: {prompt}")
            
            respuesta_modelo = SystemMessage().handle_request(prompt, from_number)

            # Guardar la conversión del modelo en la base de datos
            ConversacionRepo().crear_conversacion(prompt, respuesta_modelo, from_number)

            # Imprimir la respuesta generada por el modelo
            print(f"GPT: {respuesta_modelo}")

            return {"status": "success", "response": respuesta_modelo}
        except Exception as e:
            return {"status": "error", "response": str(e)}