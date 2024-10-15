from flask import Blueprint, jsonify, request, render_template
from app.services.openai_service import OpenAIService
from app import db
from app.models.contact_model import Contact
from app.repos.contact_repo import ContactRepo

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/message', methods=['POST'])
def simulate_twilio():
    data = request.json
    message_body = data.get('message', 'Este es un mensaje simulado desde Twilio')
    from_number = data.get('from_number', '+14155551234')

    response = OpenAIService().handle_request(message_body, from_number)

    return jsonify(response)

# Ruta para crear un nuevo contacto
@bp.route('/api/contactos', methods=['POST'])
def crear_contacto():
    data = request.json
    nombre = data.get('nombre')
    telefono = data.get('telefono')
    direccion = data.get('direccion')
    email = data.get('email')
    
    nuevo_contacto = ContactRepo.crear_contacto(db.session, telefono, nombre, direccion, email)
    return jsonify({
        "id": nuevo_contacto.id,
        "nombre": nuevo_contacto.nombre,
        "telefono": nuevo_contacto.telefono,
        "direccion": nuevo_contacto.direccion,
        "email": nuevo_contacto.email
    }), 201

# Ruta para obtener un contacto por su número de teléfono
@bp.route('/api/contactos/<string:telefono>', methods=['GET'])
def obtener_contacto(telefono):
    contacto = ContactRepo.obtener_contacto_por_telefono(db.session, telefono)
    if contacto:
        return jsonify({
            "id": contacto.id,
            "nombre": contacto.nombre,
            "telefono": contacto.telefono,
            "direccion": contacto.direccion,
            "email": contacto.email
        }), 200
    else:
        return jsonify({"error": "Contacto no encontrado"}), 404

# Ruta para obtener todos los contactos
@bp.route('/api/contactos', methods=['GET'])
def obtener_todos_contactos():
    contactos = ContactRepo.obtener_todos_contactos(db.session)
    return jsonify([
        {
            "id": contacto.id,
            "nombre": contacto.nombre,
            "telefono": contacto.telefono,
            "direccion": contacto.direccion,
            "email": contacto.email
        } for contacto in contactos
    ]), 200

# Ruta para actualizar un contacto por su ID (solo los campos enviados)
@bp.route('/api/contactos/<int:contacto_id>', methods=['PUT'])
def actualizar_contacto(contacto_id):
    data = request.json
    nombre = data.get('nombre')
    telefono = data.get('telefono')
    direccion = data.get('direccion')
    email = data.get('email')
    
    contacto_actualizado = ContactRepo.actualizar_contacto(db.session, contacto_id, nombre, telefono, direccion, email)
    if contacto_actualizado:
        return jsonify({
            "id": contacto_actualizado.id,
            "nombre": contacto_actualizado.nombre,
            "telefono": contacto_actualizado.telefono,
            "direccion": contacto_actualizado.direccion,
            "email": contacto_actualizado.email
        }), 200
    else:
        return jsonify({"error": "Contacto no encontrado"}), 404

# Ruta para agregar o actualizar la dirección de un contacto
@bp.route('/api/contactos/<int:contacto_id>/direccion', methods=['PUT'])
def actualizar_direccion_contacto(contacto_id):
    data = request.json
    nueva_direccion = data.get('direccion')

    if not nueva_direccion:
        return jsonify({"error": "La dirección no puede estar vacía"}), 400

    contacto_actualizado = ContactRepo.agregar_direccion(db.session, contacto_id, nueva_direccion)
    if contacto_actualizado:
        return jsonify({
            "id": contacto_actualizado.id,
            "nombre": contacto_actualizado.nombre,
            "direccion": contacto_actualizado.direccion
        }), 200
    else:
        return jsonify({"error": "Contacto no encontrado"}), 404