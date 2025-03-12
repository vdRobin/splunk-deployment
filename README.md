# splunk-deployment
📌 SIEM Deployment with Splunk, Kubernetes and Helm

## 📖 Description
This project sets up a **SIEM (Security Information and Event Management)** system using **Splunk**, deployed on **Kubernetes (OVH cluster)** with **Helm**. The goal is to collect, analyze, and detect security threats from firewall logs (Fortinet & Checkpoint).  

## 🛠 Tools & Technologies Used  
- **Kubernetes (OVH)** – Managed Kubernetes cluster  
- **Helm** – Package manager for Kubernetes  
- **Docker** – Containerization  
- **Splunk** – Log collection and analysis  
- **Python** – Automation scripts for log generation and incident management

## ⚙️ Installation  

### 1️⃣ Prerequisites  
Ensure you have the following installed on your system:
- [Helm](https://helm.sh/docs/intro/install/)  
- [Docker](https://www.docker.com/get-started)  
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

### 2️⃣ Switching to OVH Managed Kubernetes Cluster

Since we are using OVH Managed Kubernetes, we need to connect to the cluster. To do that download the kubeconfig.yaml file and put it in the .kube file in your local user. After that if you are on windows, execute this commands:

```bash
kubectl config view
$env:KUBECONFIG="C:\Users\user\.kube\kubeconfig.yml"
```

## 🗃️ Project Summary

### 1️⃣ Kubernetes Cluster Setup  
- Initially deployed on **Minikube**, later migrated to **OVH Managed Kubernetes**.  

### 2️⃣ Deploying Splunk on Kubernetes  
- Installed the **Splunk Operator** and configured **Persistent Volume Claims (PVCs)** for data storage.  
- Ensured **Custom Resource Definitions (CRDs)** were updated for proper Splunk deployment.  
- Installed **Splunk Enterprise** and configured clustering (indexers, search heads, and cluster manager).  

### 3️⃣ Managing Access & Secrets  
- Retrieved and managed Splunk admin credentials.  
- Restricted Splunk Operator's cluster-wide access for better security.  

### 4️⃣ Generating Security Logs  
- Developed a **Python script** to simulate security logs from **Fortinet** and **Checkpoint**.  
- Containerized the script using **Docker** and deployed it on Kubernetes using **Helm**.  

### 5️⃣ Debugging & Monitoring  
- Used **port-forwarding** and **logs analysis** for troubleshooting deployment issues.  
- Automated port-forwarding via a background script for easier debugging.

