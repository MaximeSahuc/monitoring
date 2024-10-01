from flask import *
data=[]

app = Flask(__name__)

@app.route("/status", methods=['GET'])
def api():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,port=8081)