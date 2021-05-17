#!/bin/sh

# generate RSA public/private and assigned to kong-consumers.yaml Secrect
python3 _rsa-generator.py

# Kong ingress controller
kubectl apply -f https://bit.ly/k4k8s

# all k8s project + kong plugins
kubectl apply -f .

# generate a valid jwt using public/private RSA
python3 _jwt-generator.py