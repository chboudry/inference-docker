# Inference in Docker container 

## Motivation
Targetted scenario is to deploy inference image to IOT edge through IOT Hub.

To suit this scenario, model and scoring script are baked into the image.

These examples are made for image size comparaison depending of the technoloy used.

## Docker container size

| IMAGE        | DESCRIPTION                                          |SIZE |
| -----------  | ---------------------------------------------------- |----------- |
| 1-aml-pip    | Azure Machine Learning inference HTTP server + pip   | 1.08 GB    |
| 2-aml-conda  | Azure Machine Learning inference HTTP server + conda | 2.73 GB    |
| 3-custom-pip | Flask server + pip                                   | 364 MB     |
| 4-onnx       | Flask server + ONNX runtime                          | 287 MB     |