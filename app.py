from flask import Flask, request
render_template
import pickle

app = Flask(__name__)

# Loadthe trained model
with open("model.pkl", "rb") as
file:
  model = pickle.load(file)

@app.route("/")
def home():
  return
render_template("index.html")

@app.route("/predict",
methods=["POST"])
def predict():
  symptoms = [
int(request.form["fever"]),
    
int(request.form["cough"]),
    
int(request.form["fatigue"]),
    
int request.form["headache"]),
    
int request.form["sore_throat"]),
    
int request.form["breathing_difficulty"])
  ]

   prediction = 
model.predict([symptoms])[0]

   return render_template(
      "index.html",
       prediction=prediction
   )

if __name__=="__main__":
  app.run(debug=True)

    
