
from .models import 

# fucntion to create app.
def create_app():
    app = Flask(__name__)
    # set the DQL to postgress connection.
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

    DB.init_app(app)
    

# landing page.
    @app.route('/')
    def root():

    return











# return/complete the 'app'.
    return app