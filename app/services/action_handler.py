# app/services/action_handler.py
import logging

from app.actions.name_action import NameAction
from app.actions.verify_contact_action import VerifyContactAction


class ActionHandleService:
    def __init__(self, user_id, prompt, db_session):
        """
        Inicializa el servicio con los datos del usuario y el contexto del prompt.
        """
        self.user_id = user_id
        self.prompt = prompt
        self.messages = []
        self.db_session = db_session  # Se añade la sesión de la base de datos como parámetro

    def handle_action(self):
        """
        Maneja las acciones basadas en el prompt del usuario.
        """
        logging.info("Iniciando handle_actions con prompt: %s", self.prompt)

        # Verificar si el usuario tiene un número de teléfono en la base de datos
        contacto = VerifyContactAction().verificar_contacto(self.user_id)

        # Procesar el nombre del contacto
        name_action = NameAction(contacto, self.prompt)
        name_message = name_action.process_name()
        if name_message:
            self.messages.append(name_message)
        
        return self.messages