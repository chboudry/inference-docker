## Commands

`cd .\3-custom-pip\`

`docker build . -t "3-custom-pip`

`docker run --rm -d -p 5001:5001/tcp 3-custom-pip:latest`

`
curl --location '127.0.0.1:5001/score' \
--header 'Content-Type: application/json' \
--data '{"data": [[1,2,3,4,5,6,7,8,9,10], [10,9,8,7,6,5,4,3,2,1]]}'
`

https://www.youtube.com/watch?v=CHttwWGdWK4

https://github.com/boxkite-ml/boxkite/tree/master/examples/kubeflow-mlflow/app