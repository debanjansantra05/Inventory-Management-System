from flask import Flask
from config import Config
from database import init_db
from routes.auth import auth_bp
from routes.inventory import inv_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize DB
init_db()

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(inv_bp)

if __name__ == "__main__":
    app.run(debug=True)