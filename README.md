# Setup

1. Run the following command within ubuntu
   ```bash
   [ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
   chmod +x ./kind
   sudo cp ./kind /usr/local/bin/kind
   rm -rf kind
   ```
2. Start exercising from [Ex1](./Ex1) folder
