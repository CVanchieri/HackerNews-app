# imports.
from .models import DB
from flask import jsonify

# function for app.
def create_app():
    app = Flask(__name__)
    # set the DQL to postgress connection.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///db.sqlite'
    DB.init_app(app)
    

# landing page route.
    @app.route('/')
    def root():
        DB.create_all()

        return ("This will be our 'landing' page, list top 10 saltiest users.")


# user search route.
    @app.route('/user', methods=['POST'])
    #@app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        #name = name or request.values['by']

        return ("This will be a 'user' page , lists their comments and saltiness.")






# return/complete the 'app'.
    return app