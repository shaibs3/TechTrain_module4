## **Run as non root inside the container**

- **Task**: Create a non root container

1. **Apply the manifest**
   ```bash
   cd ../Ex4
   kubectl apply -f ./exercise4.yaml
   ```

2. **Exec into the pod**
   ```bash
   kubectl exec -it user-test-pod -- bash
   ```
3. **Check the user id running in the container and verify the user id is 1000**
   ```bash
    < find the command for checking the user id>
   ```
4. **What is the security concern related to the output of the previous command ?**
5. **Fix the security volnurability found in previous section by editing exercise5.yaml and reapplying the manifest:**
   ```bash
   kubectl apply -f ./exercise4.yaml --force
   ```
6. ** Exec again to the container and verify that the issue is now solved **
7. **Cleanup**
   ```bash
      kubectl delete -f ./exercise4.yaml
   ```