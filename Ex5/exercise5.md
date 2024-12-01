## 2. **Create a Failed Pod on Purpose**

- **Task**: Create a deployment 

1. **Apply the manifest**
   ```bash
   cd ./Ex3
   kubectl apply -f ./exercise5.md
   ```
2. **Check the status of the deployment**
   ```bash
   kubectl get deployment hello-world-deployment
   ```

3. **Check the pods status, how many pods are there?**
   ```bash
   kubectl get pods 
   ```
4. **Describe the deployment**
   ```bash
      kubectl describe deployment hello-world-deployment
   ```
5. **Scale out the deployment**
   ```bash
    kubectl scale deployment hello-world-deployment --replicas=5
   ```
6. **Check the pods status and verify that there are indeed 5 pods for the deployment**
7. **Describe the deployment again and verify the scaled event is in the event section**
7. **Cleanup**
   ```bash
      kubectl delete -f ./exercise4.yaml
   ```