from flask import *

data = []
 
app = Flask()

@app.route("/status", methods=['GET'])
def api():
    return jsonify(data)

app.run()   