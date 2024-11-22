## 3. **Create a Deployment and Check the Number of Running Pods**

- **Task**: Create a deployment with a specified number of replicas (e.g., 3 replicas).

- **Instructions**:
    - Create a deployment YAML file with a simple web app (e.g., using `nginx` or `httpd`).
    - Apply the deployment using `kubectl apply`.

- **Next Steps**:
    - **Check the number of running pods**: Use `kubectl get pods` and `kubectl get deployment` to check how many pods are running and verify that the deployment is scaling correctly.
