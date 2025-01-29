from flask import Flask
from app import app

# Add any production-specific middleware here if needed
# For example, if you're behind a proxy:
# from werkzeug.middleware.proxy_fix import ProxyFix
# app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    # Note: In production, this block won't be called
    # as Gunicorn will import the 'app' variable directly
    import sys
    from werkzeug.serving import run_simple

    
    # Start both servers
    run_simple('0.0.0.0', 5000, app, use_reloader=True)
    run_simple('0.0.0.0', 5001, app, use_reloader=True)