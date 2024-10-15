# app/repos/chromadb_repo.py

from app.actions.chromadb_action import ChromaDBAction
from app.actions.embedding_processing_action import EmbeddingProcessingAction

class ChromaDBRepo:
    def __init__(self, chromadb_action=None):
        self.chromadb_action = chromadb_action or ChromaDBAction()

    def buscar_fragmentos_relevantes(self, prompt):
        # Obtener el embedding del prompt
        query_embedding = EmbeddingProcessingAction().get_embedding_for_chunk(prompt)
        if not query_embedding:
            raise ValueError("No se pudo generar el embedding para el prompt.")

        # Buscar en ChromaDB los fragmentos más relevantes
        try:
            relevant_chunks = self.chromadb_action.search_in_chromadb(query_embedding)
        except Exception as e:
            print(f"Error al buscar en ChromaDB: {e}")
            return {
                "role": "system",
                "content": "Hubo un error al buscar en la base de datos."
            }

        # Incluir los fragmentos relevantes en el prompt
        if not relevant_chunks:
            return {
                "role": "system",
                "content": "No se encontró información relevante en la base de datos."
            }

        relevant_info = "\n".join(str(chunk) for chunk in relevant_chunks)
        return {
            "role": "system",
            "content": f"Información relevante encontrada:\n{relevant_info}"
        }
