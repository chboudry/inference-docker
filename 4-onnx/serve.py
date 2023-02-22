import onnxruntime
import json
import numpy as np
from flask import Flask, request

model_file = "model.onnx"
session = onnxruntime.InferenceSession(model_file)

app = Flask(__name__)

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


@app.route("/score", methods=["POST"])
def predict():
    raw_data = json.loads(request.data)
    data = raw_data.get("data",None)
    result = session.run(None, {"input":data})
    return json.dumps(result, cls=NumpyEncoder)

if __name__ == "__main__":
    app.run()


#def test():
#    print(rawdata)
#    raw_data = json.loads(rawdata)
#    print(raw_data)
#    data = raw_data.get("data",None)
#    print(data)
#    return session.run(None, {"input":data})

#json.dumps(result)