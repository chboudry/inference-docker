## Commands 

`cd .\4-onnx\`

`docker build . -t "4-onnx"`

`docker run --rm -d -p 5001:5001/tcp 4-onnx:latest`

```
curl --location '127.0.0.1:5001/score' \
--header 'Content-Type: application/json' \
--data '{"data": [[1,2,3,4,5,6,7,8,9,10], [10,9,8,7,6,5,4,3,2,1]]}'
```

## Transform sklearn model pkl to onnx 

```
pip install onnx skl2onnx onnxmltools scikit-learn joblib numpy

python

import numpy
import joblib
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import Int64TensorType
from skl2onnx import get_latest_tested_opset_version
from onnxmltools.utils import save_model

target_opset = get_latest_tested_opset_version()

model_path =  "./sklearn_regression_model.pkl"
model = joblib.load(model_path)
onnx_clf = convert_sklearn(
    model,
    "gbdt_model",
    initial_types=[("input", Int64TensorType([None, 10]))],
    target_opset={"": target_opset, "ai.onnx.ml": 1}
)
save_model(onnx_clf, "model.onnx")
```

https://medium.com/@liamwr17/stop-pickling-your-ml-models-use-onnx-instead-983cd4561e3a

https://github.com/onnx/tutorials

    