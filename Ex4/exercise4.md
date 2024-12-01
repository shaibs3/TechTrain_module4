## **Fix a failed running pod**

- **Task**: Create a pod

1. **Apply the manifest**
   ```bash
   cd ./Ex4
   docker build -t debug-app:latest -f ./App
   kind load docker-image debug-app:latest
   kubectl apply -f ./exercise4.md
   ```

2. **Check the pod's status, is it in a running state?**
   ```bash
   kubectl get pods 
   ```
3. **View the pod's logs**
   ```bash
    kubectl logs debug-app
   ```
4. **Based on the pod's logs, try to fix the error by editing the exercise4.yaml file. after editing the file run the following:**
   ```bash
    kubectl apply -f ./broken.yaml --force
   ```
5. **Cleanup**
   ```bash
      kubectl delete -f ./exercise3.md
   ```