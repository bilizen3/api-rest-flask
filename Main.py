from flask import Flask,jsonify,request,json
from Person  import Person

app= Flask(__name__)

carlos=Person("Carlos",30)
bill=Person("Bill",40)
@app.route("/getPerson",methods=["GET"])
def getMessage():
    return json.dumps(carlos.__dict__)

@app.route("/postName",methods=["POST"])
def name():
    return json.dumps(request.json)

@app.route("/postMano",methods=["POST"])
def mano():
    return jsonify(request.json)

if __name__=="__main__":
    app.run()
