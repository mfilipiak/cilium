#! /bin/bash

for n in $(kind get nodes)
do
    docker cp plugins/cilium-cni/cilium-cni $n:/opt/cni/bin/cilium-cni
    docker exec $n chmod +x /opt/cni/bin/cilium-cni

done

for p in $(kubectl get pods -n kube-system -l "app.kubernetes.io/name=cilium-agent" --no-headers | awk '{print $1}')
do
    kubectl delete -n kube-system pod/$p
done