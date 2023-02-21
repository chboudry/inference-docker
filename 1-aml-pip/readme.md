## Commands

`cd .\1-aml-pip\`

`docker build . -t 1-aml-pip`

`docker run --rm -d -p 5001:5001/tcp 1-aml-pip:latest`

`
curl --location '127.0.0.1:5001/score' \
--header 'Content-Type: application/json' \
--data '{"data": [[1,2,3,4,5,6,7,8,9,10], [10,9,8,7,6,5,4,3,2,1]]}'
`

## Links
https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/online/custom-container/minimal/single-model

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-inference-server-http

https://hub.docker.com/_/microsoft-azureml-inference