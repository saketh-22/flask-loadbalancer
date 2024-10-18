# CloudBalancer
## Load Balancing for Cloud Applications
**Technologies:** Microsoft Azure, Docker, Python, Flask API

### Overview
CloudBalancer is a load balancing solution designed for cloud applications, leveraging Microsoft Azure's Virtual Machines (VMs) and Docker. This project aims to reduce response times and optimize resource utilization based on real-time performance metrics.

### Features
- **Load Balancing:** Implements Round Robin, Weighted Round Robin, and Load-Based strategies to efficiently distribute HTTP requests across multiple backend servers.
- **Automated VM Management:** Utilizes PowerShell scripts to automate the setup and configuration of Azure VMs, significantly reducing manual efforts.
- **Scalability:** Capable of managing up to 100 simultaneous HTTP requests, ensuring efficient overlay network formation and enhancing the scalability of Azure VMs.

### Getting Started

#### Prerequisites
- Microsoft Azure account
- Docker installed
- Python 3.x
- Flask library
- Requests library

#### Installation
1. Clone the repository:

    ```bash
    git clone <GitHub Link>
    cd flask-loadbalancer
    ```

2. Set up your Azure VMs and configure them as needed. Make sure to replace `<ip_addr1>` and `<ip_addr2>` in the code with the actual IP addresses of your backend servers.

3. **Note:** There is no Dockerfile provided in the repository. You may need to create one if you wish to containerize this application.

4. Build and run the Docker container (if you create a Dockerfile):

    ```bash
    docker build -t cloudbalancer .
    docker run -e LB=rr -p 5000:4000 cloudbalancer
    ```

5. Access the application at localhost

### Usage

- To use Round Robin load balancing, set the environment variable `LB` to `rr`. This method alternates requests between two servers:
    - `http://<ip_addr1>:8080`
    - `http://<ip_addr2>:8080`
  
- For Weighted Round Robin, set `LB` to `wrr`. This method uses weights to determine the number of requests sent to each server (e.g., server 1 might receive 5 requests for every 3 requests sent to server 2).

- For Load-Based balancing, set `LB` to `load`. This method routes requests to the server with the lower CPU load:
    - The load for each server can be accessed at the `/load` endpoint.

### Code Explanation

The application utilizes Flask to create a simple web server that handles load balancing based on the specified method:

- **Round Robin (rr):** Alternates requests between `server1` and `server2`.
- **Weighted Round Robin (wrr):** Distributes requests based on predefined weights.
- **Load-Based (load):** Directs requests to the server with the lower CPU load, with the load details available at the `/load` endpoint.



