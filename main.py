from flask import Flask

from routes.routes import initRoutes
from routes.userRoutes import initUserRoutes

# Run the app
if __name__ == '__main__':
    app = Flask(__name__)
    initUserRoutes(app)
    app.run(debug=True)

