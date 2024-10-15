# app/actions/name_action.py
from ..extractors.name_extractor import NombreExtractor
from ..repos.contact_repo import ContactRepo
import logging

class NameAction:
    def __init__(self, db_session, contacto, prompt):
        self.contacto = contacto
        self.prompt = prompt
        self.db_session = db_session

    def process_name(self):
        message = None
        # Si el contacto tiene un nombre, usarlo en la conversación
        if self.contacto.nombre:
            print(f"El usuario se llama y llamalo {self.contacto.nombre}.")
            message = {"role": "assistant", "content": f"El usuario se llama y llamalo {self.contacto.nombre}."}
        else:
            extraerNombre = NombreExtractor().extraer_nombre(self.prompt)  
            print(f"El contacto es {self.contacto}")
            # grabar nombre en base de datos
            if extraerNombre:
                ContactRepo().actualizar_contacto(self.db_session, self.contacto.id, nombre=extraerNombre)
                message = {"role": "assistant", "content": f"El usuario se llama y llamalo {extraerNombre}."}
            else:
                message = {"role": "system", "content": "pregunte al usuario en que le podemos ayudar y cual es su nombre para mejor servicio."}
        return message