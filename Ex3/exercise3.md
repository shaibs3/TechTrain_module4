## **Fix a failed running pod**

- **Task**: Create a failed  pod

1. **Apply the manifest**
   ```bash
   cd ../Ex3
   docker build . -t debug-app:latest -f ./App/Dockerfile
   kind load docker-image debug-app:latest
   kubectl apply -f ./exercise3.yaml
   ```

2. **Check the pod's status, is it in a running state?**
   ```bash
   kubectl get pods 
   ```
3. **View the pod's logs**
   ```bash
    kubectl logs debug-app
   ```
4. **Based on the pod's logs, try to fix the error by editing the exercise3.yaml file. after editing the file run the following:**
   ```bash
    kubectl apply -f ./exercise3.yaml --force
   ```
5. **Check the pod's status again and verify that the pod is running**
6. **Check the pod's logs and verify the output is now valid**
5. **Cleanup**
   ```bash
      kubectl delete -f ./exercise3.yaml
   ```