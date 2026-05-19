#!/bin/bash

echo "Construyendo imagen Docker..."

docker build -t geo-app .

echo "Ejecutando contenedor..."

docker run --name samplerunning geo-app
