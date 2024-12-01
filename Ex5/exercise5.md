## **Create a deployment **

- **Task**: Create a deployment

1. **Apply the manifest**
   ```bash
   cd ../Ex5
   kubectl apply -f ./exercise5.yaml
   ```
2. **Check the status of the deployment**
   ```bash
   kubectl get deployment hello-world-deployment
   ```

3. **Check the pods status, how many pods are there?**
   ```bash
   kubectl get pods 
   ```
4. **Describe the deployment and view the events section at the bottom. This section shows you the actions done by the deployment**
   ```bash
      kubectl describe deployment hello-world-deployment
   ```
5. **Scale out the deployment to 5 replicas by editing the relevant field in the exercise5.yaml file**
   ```bash
    <Run the kubectl apply command to apply the change>
   ```
6. **Check the pods status and verify that there are indeed 5 pods for the deployment**
7. **Describe the deployment again and verify the scaled event is in the event section**
7. **Cleanup**
   ```bash
      kubectl delete -f ./exercise5.yaml
   ```