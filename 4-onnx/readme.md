## Transform a sklearn model to onnx 

pip install onnx skl2onnx onnxmltools scikit-learn joblib numpy

python

import numpy
import joblib
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
from skl2onnx import get_latest_tested_opset_version
from onnxmltools.utils import save_model

target_opset = get_latest_tested_opset_version()

model_path =  "./sklearn_regression_model.pkl"
model = joblib.load(model_path)
onnx_clf = convert_sklearn(
    model,
    "gbdt_model",
    initial_types=[("input", FloatTensorType([None, 1]))],
    target_opset={"": target_opset, "ai.onnx.ml": 1}
)
save_model(onnx_clf, "model.onnx")

https://medium.com/@liamwr17/stop-pickling-your-ml-models-use-onnx-instead-983cd4561e3a