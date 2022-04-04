from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
from chat import predict,predict2
app = Flask(__name__)

# route principale
@app.route("/")
def index_get():
    return render_template("base.html")

# route isen
@app.route("/predictisen", methods=['GET', 'POST'])
def predictisen():
    text = request.get_json().get("message")
    response = predict(text)
    message = {"answer":response}
    return jsonify(message)

# route IA Microsoft
@app.route("/predictiamic", methods=['GET', 'POST'])
def predictiamic():
    text = request.get_json().get("message")
    response = predict2(text)
    message = {"answer":response}
    return jsonify(message)

app.run(debug=True)
# if __name__ == "__main__":
#     app.run(debug=True)
    


