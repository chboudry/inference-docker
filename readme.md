# Inference in Docker container 

## Motivation
Targetted scenario is to deploy inference image to IOT edge through IOT Hub.

To suit this scenario, model and scoring script are baked into the image.

These examples are made for image size comparaison depending of the technoloy used.

## Docker container size

| IMAGE        | SIZE |
| -----------  | ----------- |
| 1-aml-pip    | 1.08 GB     |
| 2-aml-conda  | 2.73 GB     |
| 3-custom-pip | 1.15 GB     |
| 4-onnx       |             |