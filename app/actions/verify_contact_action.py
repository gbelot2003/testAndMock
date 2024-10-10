

from app.repos.contact_repo import ContactRepo

class VerifyContactAction:
    @staticmethod
    def __init__(self):
        pass

    @staticmethod
    def verificar_contacto(user_id):
        print("Verificando contacto...")
        # Verificar si el usuario tiene un número de teléfono en la base de datos
        contacto = ContactRepo.obtener_contacto_por_telefono(user_id)

        if not contacto:
            # Si no existe, crear un nuevo contacto con el número de teléfono
            contacto = ContactRepo.crear_contacto(telefono=user_id)

        return contacto