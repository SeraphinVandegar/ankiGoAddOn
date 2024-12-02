from flask import Flask

from routes.routes import initRoutes

# Run the app
if __name__ == '__main__':
    app = Flask(__name__)
    initRoutes(app)
    app.run(debug=True)

