# app/services/action_handler.py

from app.actions.verify_contact_action import VerifyContactAction

class ActionHandleService:
    def __init__(self, prompt, from_number, db_session):
        self.from_number = from_number
        self.prompt = prompt
        self.db_session = db_session
        self.messages = []

    def handle_action(self, from_number):
        """
        Maneja la acción principal de verificar el contacto.
        """
        # Verificar si el usuario tiene un número de teléfono en la base de datos usando `VerifyContactAction`
        contacto = VerifyContactAction.verificar_contacto(from_number, self.db_session)
        
        # Puedes agregar más lógica aquí según lo que necesites
        return self.messages
