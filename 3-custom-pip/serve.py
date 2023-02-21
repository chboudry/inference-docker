#import pickle
import joblib
from flask import Flask, request

model_file = "sklearn_regression_model.pkl"

#with open(model_file, "rb") as f:
#    model = pickle.load(f)

# deserialize the model file back into a sklearn model
model = joblib.load(model_file)

app = Flask(__name__)

@app.route("/score", methods=["POST"])
def predict():
    data = request.json
    result = model.predict(data)
    return result.tolist()

if __name__ == "__main__":
    app.run()
