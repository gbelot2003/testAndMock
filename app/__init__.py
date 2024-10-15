from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from app.actions.chromadb_action import ChromaDBAction
from app.actions.embedding_processing_action import EmbeddingProcessingAction
from app.actions.pdf_processing_action import PDFProcessingService

db = SQLAlchemy()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    # Importar modelos
    from .models import Contact, Address

    # Lista de rutas de archivos PDF
    pdf_paths = [
        "files/encomiendas.pdf",
        # Agrega más rutas de archivos PDF aquí
    ]

    # Procesar cada PDF al iniciar la aplicación
    for pdf_path in pdf_paths:
        try:
            text = PDFProcessingService().extract_text_from_pdf(pdf_path)
            chunks = PDFProcessingService().split_text_into_chunks(text)
            chunks_with_embeddings = [(chunk, EmbeddingProcessingAction().get_embedding_for_chunk(chunk)) for chunk in chunks]
            ChromaDBAction().store_chunks_in_chromadb(chunks_with_embeddings, pdf_path)
        except Exception as e:
            print(f"Error procesando el PDF {pdf_path}: {e}")

    # Registro de rutas
    from . import routes
    app.register_blueprint(routes.bp)

    return app