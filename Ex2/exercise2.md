## 2. **Create a Failed Pod on Purpose**

- **Task**: Create a pod  with non existing image.

1. **Apply the manifest**
   ```bash
   cd ./Ex2
   kubectl apply -f ./exercise2.md
   ```
2. **Check the pod status**
   ```bash
   kubectl get pods 
   ```
3. **Describe the pod and observe the pod's events section to understand the container's failure reason**
   ```bash
      kubectl describe pod <pod_name>
   ```
4. Fix the issue by fixing the yaml file and running:
   ```bash
      kubectl apply -f ./exercise2.md
   ```
5. **Cleanup**
   ```bash
      kubectl delete -f ./exercise1.md
   ```