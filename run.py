import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    os.system("python update.py")
    app.run(host="0.0.0.0", port=5000, debug=True,
            ssl_context=('./app/certificates/cert.pem', './app/certificates/key.pem'))
