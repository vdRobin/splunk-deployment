@echo off
kubectl port-forward splunk-shc-test-search-head-0 8000:8000 -n siem > port-forward.log 2>&1