import os
import logging
from app import create_app
from logging.handlers import RotatingFileHandler

app = create_app()

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(level=logging.INFO)
    handler = RotatingFileHandler(
        "logs/server.log", maxBytes=100000, backupCount=3)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    app.logger.info("Server started")

    try:
        app.run(host="0.0.0.0", port=5000, debug=True,
                ssl_context=('./app/certificates/cert.pem', './app/certificates/key.pem'))
    except KeyboardInterrupt:
        app.logger.info("Server stopped after user termination")
