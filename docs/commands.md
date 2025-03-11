# 📜 Command History  

This file contains all the commands used during the project setup and deployment.  

## 🛠 Environment Setup  
### Install and Check Dependencies  
```bash
helm version            
minikube status          
kubectl version --short   
```

## 🚀 Start Minikube and Kubernetes Cluster

```bash
minikube start
kubectl create namespace siem
kubectl config set-context --current --namespace=siem
```

## Deploy Splunk using Helm

```bash
helm repo add splunk https://splunk.github.io/splunk-operator/
helm repo update
helm show values splunk/splunk-operator
helm install splunk splunk/splunk-operator --namespace=siem -f .\helm\splunk\values.yaml
```

### How to see which port is exposed


```bash
kubectl get svc -n siem 
kubectl port-forward svc/splunk-operator-controller-manager-service 8088:80 -n siem
```

## Change of plans

I decide to use OVH Managed Kubernetes Cluster

I'm on windows so I write this command to connect to the cluster:

```bash
kubectl config view
$env:KUBECONFIG="C:\Users\user\.kube\kubeconfig.yml"
```

I add splunk operator in my Helm repository and update it

```bash
helm repo add splunk https://splunk.github.io/splunk-operator/
helm repo update
```


In the following [documentation](https://splunk.github.io/splunk-operator/Helm.html), they says that upgrading to latest version using Helm chart will not upgrade CRDs. To do this we need to do the following commands:

```bash
git clone https://github.com/splunk/splunk-operator.git splunk-new-operator
cd ../splunk-new-operator
git checkout release/2.7.0
kubectl apply -f config/crd/bases/
```

Now we need to see if CRDs are updated:

```bash
kubectl get crds | Select-String "splunk"
```

Now we can see configurable values for the chart:

```bash
helm show values splunk/splunk-operator
```

I need to made a Persistent Volume Claim to store data:
```bash
cd ../splunk-deployment
kubectl apply -f splunk-pvc.yaml
```

we verify if the PVC is created and bound:
```bash
kubectl get pvc -n siem
```
I see that a PVC was already made by OVH.

I need now to configure the Splunk Operator deployments:

```bash

helm install splunk-operator-test -f ./helm/splunk/new_values.yaml --set installCRDs=true splunk/splunk-operator -n siem
```


To find all deployed release use the following command : 

```bash
helm list -n siem
```

By default the Splunk Operator has a cluster-wide access. Let's upgrade to modify that


```bash
helm upgrade --set splunkOperator.clusterWideAccess=false --set installCRDs=true splunk-operator-test splunk/splunk-operator -n siem
```

### Now we need to install Splunk Enterprise


```bash
helm show values splunk/splunk-enterprise
helm install -f ./helm/splunk-enterprise/new_values.yaml --set installCRDs=true --set splunk-operator.enabled=false splunk-enterprise splunk/splunk-enterprise -n siem
kubectl get pods -n siem
kubectl get indexerclusters.enterprise.splunk.com -n siem
helm upgrade --install splunk-enterprise splunk/splunk-enterprise -f ./helm/splunk-enterprise/new_values.yaml --set installCRDs=true --set splunk-operator.enabled=false -n siem
```

I had a problem, indexer doesn't show up in the pods list, I don't know why. Grok found that If the chart uses clusterManager instead of clusterMaster, update your new_values.yaml can fix the problem. That action fixed the problem, maybe the indexer needed the clusterManager.


Now everything is okay, so we need to verify:

```bash
kubectl get clustermanager,searchheadcluster,indexercluster -n siem
```





