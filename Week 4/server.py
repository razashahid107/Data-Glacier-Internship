from crypt import methods
import flask 



app = flask.Flask(__name__, template_folder='templates')  


@app.route('/', methods=['GET'])
def handler():
    return 'Hello' 

if __name__ == '__main__' :
    app.run(debug=True)
