# app/services/action_handler.py

from app.actions.verify_contact_action import VerifyContactAction


class ActionHandleService:
    def __init__(self, prompt,  from_number):
        self.from_number = from_number
        self.prompt = prompt
        self.messages = []


    def handle_action(self):
        # Verificar si el usuario tiene un número de teléfono en la base de datos
        contacto = VerifyContactAction().verificar_contacto(self.from_number)

        
        return self.messages
