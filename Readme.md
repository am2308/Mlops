docker build -t mlflow-flask-app:0.1 .

docker run -d -p 5008:5008 --name=mlflow-flask-app mlflow-flask-app:0.1

curl -X POST -H "Content-Type: application/json" \
-d '[
    {"MedInc": 8.3252, "HouseAge": 41.0, "AveRooms": 6.984127, "AveBedrms": 1.023810, "Population": 322.0, "AveOccup": 2.555556, "Latitude": 37.88, "Longitude": -122.23},
    {"MedInc": 8.3014, "HouseAge": 21.0, "AveRooms": 6.238137, "AveBedrms": 0.971880, "Population": 2401.0, "AveOccup": 2.109842, "Latitude": 37.86, "Longitude": -122.22}
]' \
http://localhost:5008/predict

683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:1.2-1

curl -X POST https://jej8917rse.execute-api.us-east-1.amazonaws.com/prod/predict \
     -H "Content-Type: text/csv" \
     -d "2.8594,20.0,4.151458137347131,1.118532455315146,4818.0,4.532455315145814,33.76,-117.91"