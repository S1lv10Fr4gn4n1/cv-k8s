#!/bin/sh

# Delete Kong ingress controller and load balancer on cloud provider
kubectl delete -f https://bit.ly/k4k8s

# all k8s project + kong plugins
kubectl delete -f .