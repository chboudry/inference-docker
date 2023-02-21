#import pickle
import joblib
import onnxruntime as ort
import numpy as np

from flask import Flask, request

model_file = "./model.onnx"

sess = ort.InferenceSession(model_file)

app = Flask(__name__)

@app.route("/score", methods=["POST"])
def predict():
    data = onnxruntime.OrtValue.ortvalue_from_numpy(request.json)
    return sess.run(
        ["Y"], data
    )

if __name__ == "__main__":
    app.run()
