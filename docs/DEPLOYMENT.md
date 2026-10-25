# Production Deployment Guide

Deploying SynthEval with Kubernetes:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: syntheval-api
spec:
  replicas: 3
```
