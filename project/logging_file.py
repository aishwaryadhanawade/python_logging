from project import app
from api.view import logg

app.register_blueprint(logg)

if __name__=='__main__':
    app.run(debug=True)