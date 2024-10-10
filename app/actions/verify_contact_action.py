# app/actions/verify_contact_action.py

from app.repos.contact_repo import ContactRepo

class VerifyContactAction:
    @staticmethod
    def verificar_contacto(user_id, db_session):
        """
        Verifica si el usuario tiene un número de teléfono en la base de datos.
        Si no existe, crea un nuevo contacto con el número de teléfono.
        
        Args:
            user_id (str): Número de teléfono del usuario.

        Returns:
            contacto (Contact): Objeto Contact con la información del contacto.
        """
        print("Verificando contacto...")
        # Verificar si el usuario tiene un número de teléfono en la base de datos
        contacto = ContactRepo.obtener_contacto_por_telefono(telefono=user_id, db_session=db_session)


        if not contacto:
            # Si no existe, crear un nuevo contacto con el número de teléfono
            print("Creando contacto nuevo...")
            contacto = ContactRepo.crear_contacto(telefono=user_id, db_session=db_session)


        return contacto
