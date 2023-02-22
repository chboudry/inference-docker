import joblib
import json
from flask import Flask, request

model_file = "sklearn_regression_model.pkl"

# deserialize the model file back into a sklearn model
model = joblib.load(model_file)

app = Flask(__name__)

@app.route("/score", methods=["POST"])
def predict():
    raw_data = json.loads(request.data)
    data = raw_data.get("data",None)
    result = model.predict(data)
    return result.tolist()

if __name__ == "__main__":
    app.run()