from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def add() :
    data = request.get_json()
    try :
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        result = a + b
        return jsonify({'result': result})
    except:
        return jsonify({'error': 'please enter number correctly'}), 400
    
if __name__ == '__main__' :
    app.run(debug=True)