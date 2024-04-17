from flask import Flask
from flask_cors import CORS
from app.models import db
from app.routes import routes_blueprint

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uav_database.db'
app.register_blueprint(routes_blueprint)

# Set up the database
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
