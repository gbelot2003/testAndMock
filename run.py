import os
from app import create_app, db
from app.models import Conversation

app = create_app(config_name='development')

def create_database():

    with app.app_context():
        db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')
        if not os.path.exists(db_path):
            db.create_all()
            print(f"Base de datos creada en {db_path}")
        else:
            print(f"Base de datos ya existe en {db_path}")

if __name__ == '__main__':
    create_database()
    app.run()