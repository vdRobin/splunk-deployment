# splunk-deployment
📌 SIEM Deployment with Splunk, Kubernetes and Helm

## 📖 Description
This project sets up a **SIEM (Security Information and Event Management)** system using **Splunk**, deployed on **Kubernetes (Minikube)** with **Helm**. The goal is to collect, analyze, and detect security threats from firewall logs (Fortinet & Checkpoint).  

## 🛠 Tools & Technologies Used  
- **Kubernetes (Minikube)** – Local Kubernetes cluster  
- **Helm** – Package manager for Kubernetes  
- **Docker** – Containerization  
- **Splunk** – Log collection and analysis  
- **Python** – Automation scripts for log generation and incident management

## ⚙️ Installation  

### 1️⃣ Prerequisites  
Ensure you have the following installed on your system:  
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)  
- [Helm](https://helm.sh/docs/intro/install/)  
- [Docker](https://www.docker.com/get-started)  
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)  

### 2️⃣ Start Minikube  
```bash
minikube start
```