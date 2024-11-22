# Tech Train Installation Instructions

## 1. Create a New Devbox
1. Go to [https://devbox.microsoft.com/](https://devbox.microsoft.com/)
2. Press the "New dev box" button
    - Choose a name for the dev box and select one of the dev box pool machines
    - Wait for the dev box to start

## 2. Ubuntu Install and Configuration
1. Open PowerShell command line
    - Run: `wsl --update`
2. Download the Ubuntu app from the Microsoft Store
3. Open the Ubuntu app, you will be asked to enter a username and password
4. Run the command: `sudo apt update`
5. Run the command: `sudo apt install net-tools -y`

## 3. Docker Desktop Install
1. Download [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Install Docker (Verify the "Use WSL 2" checkbox is checked)

## 4. Kubectl Install
1. Run PowerShell as admin and run the command:
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```
2. Run PowerShell as admin and run the command:
   ```powershell
   choco install kubernetes-cli
   ```
3. Verify the installation by running the command:
   ```powershell
   kubectl version --client
   ```
5. Run the following command:
    ```powershell
    cd ~; mkdir .kube; cd .kube; New-Item config -type file
    ```
6. Run the following command within ubuntu
   ```bash
   [ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
   chmod +x ./kind
   sudo cp ./kind /usr/local/bin/kind
   rm -rf kind
   ```
