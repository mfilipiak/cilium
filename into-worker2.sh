#!/bin/bash

# kubectl get pod -n kube-system -l k8s-app=cilium -o wide | grep kind-worker2 | awk '{print $1}' | xargs -I {} kubectl exec -it -n kube-system {} -c cilium-agent -- /bin/bash
kubectl exec -it -n kube-system -c cilium-agent $(kubectl get pod -n kube-system -l k8s-app=cilium -o wide | grep kind-worker2 | awk '{print $1}') -- /bin/bash