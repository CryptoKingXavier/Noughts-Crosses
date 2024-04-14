from typing import Any
from flask import Flask
from flask_cors import CORS
from secrets import token_hex
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect


def create_app() -> Flask:
    # Creating a Flask server object
    app: Flask = Flask(__name__)
    # Enable CSRF for the server endpoint
    csrf: CSRFProtect = CSRFProtect(app)

    app.secret_key = token_hex(16)

    # Enabling CORS for all routes
    CORS(app)

    # Configuring Talisman for additional security headers
    talisman = Talisman(app, content_security_policy={
        'default-src': "'self'",
        'script-src': "'self'",
        'style-src': "'self'",
        'img-src': "'self'",
        'font-src': "'self'",
        'frame-ancestors': "'none'",
        'base-uri': "'self'",
        'form-action': "'self'",
        'object-src': "'none'"
    })

    # Setting secure cookies
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

    @app.after_request
    def add_security_headers(response) -> Any:
        # Additional security headers
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Referrer-Policy'] = 'same-origin'
        return response

    from tic_tac_toe.main.routes import main
    app.register_blueprint(main)

    return app
