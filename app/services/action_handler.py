# app/services/action_handler.py

from app.actions.conversation_history_action import ConversationHistoryAction
from app.actions.name_action import NameAction
from app.actions.verify_contact_action import VerifyContactAction
from app.repos.chromadb_repo import ChromaDBRepo

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
        try:
            contacto = VerifyContactAction.verificar_contacto(from_number, self.db_session)
            print(f"Contacto verificado: {contacto}")
        except Exception as e:
            print(f"Error al verificar el número de tel Opportuno: {e}")
            contacto = None

        # Buscar historial de conversación
        conversation_history_action = ConversationHistoryAction()
        chat_history_messages = conversation_history_action.compilar_conversacion(self.from_number)
        self.messages.extend(chat_history_messages)

        # Buscar fragmentos relevantes en ChromaDB
        chromadb_repo = ChromaDBRepo()
        relevant_chunks = chromadb_repo.buscar_fragmentos_relevantes(self.prompt)
        if relevant_chunks:
            self.messages.append(relevant_chunks)

        # Procesar el nombre del contacto
        name_action = NameAction(db_session = self.db_session, contacto = contacto, prompt= self.prompt)
        name_message = name_action.process_name()
        if name_message:
            self.messages.append(name_message)

        # Puedes agregar más lógica aquí según lo que necesites
        return self.messages
