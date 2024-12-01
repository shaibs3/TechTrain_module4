## 1. **Create a Hello World Application in a Pod**

**setup**
   ```bash
   git clone https://github.com/shaibs3/TechTrain_module4.git
   kind create cluster
   ```

- **Task**: Create a pod that runs a simple "Hello World" application. The pod should output "Hello World" every 5 seconds.
1.  **Apply the manifest**  
    ```bash
    cd ./Ex1
    kubectl apply -f ./exercise1.md
    ```
2. **Find the pod name**
   ```bash
   kubectl get pods 
   ```
2. **Read the logs**:
   ```bash
      kubectl logs <pod_name from step>
   ```
3. **Describe the pod and observe the pod's events section to understand the container's creation flow**
   ```bash
      kubectl describe pod <pod_name>
   ```
4. **Cleanup**
   ```bash
      kubectl delete -f ./exercise1.yaml
   ```