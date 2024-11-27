
---

## 5. **Scaling a Deployment and Verifying Pod Changes**

- **Task**: Scale the deployment up and down, and observe the changes in the number of pods.

- **Instructions**:
    - Scale the deployment to 5 replicas using `kubectl scale deployment <deployment_name> --replicas=5`.

- **Next Steps**:
    - **Check the number of pods**: Use `kubectl get pods` to verify the scaling operation. Check the running pods before and after scaling.
    - **Explain what happens during scaling**: Discuss how Kubernetes manages pod replication and distribution.
