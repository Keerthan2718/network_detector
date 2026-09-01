# 🔎 Network Detective

A Python-based **security-oriented network investigation tool** that collects information about your own machine and local network, exposes the collected functionality through a **FastAPI backend**, and generates a summary from the collected data.

## 🚀 Features

* 🖥️ Detect system hostname
* 🌐 Detect IPv4 address
* 📡 Detect subnet mask
* 🚪 Detect default gateway
* 🔍 Detect configured DNS server
* 📋 Read the ARP table
* 🔓 Identify listening TCP ports
* 🆔 Display the PID associated with listening ports
* 🔗 Test TCP connections to a target
* 💾 Save collected network information as JSON
* 📊 Generate a network summary
* ⚡ Expose network information through REST API endpoints

## 🛠️ Technologies Used

* Python
* `socket`
* `subprocess`
* `ipaddress`
* JSON / file handling
* Exception handling
* FastAPI
* Uvicorn
* Git & GitHub

## 📁 Project Structure

```text
network_detective/
│
├── main.py          # CLI application
├── network.py       # Network information
├── ports.py         # Port investigation and connection testing
├── system.py        # System information
├── api.py           # FastAPI backend
├── summary.py       # Network data analysis
└── network.json     # Collected network data
```

## ▶️ Running the CLI

Run:

```bash
python main.py
```

The tool collects information from the local machine and saves the results to:

```text
network.json
```

## 📊 Generate Network Summary

After running `main.py`, run:

```bash
python summary.py
```

Example:

```text
==============================
       NETWORK SUMMARY
==============================

Hostname: MY-PC
IPv4 Address: 192.168.1.10
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.1.1

Devices discovered: 7

Open/listening ports:
135
445
5000

## ⚡ Running the API

Start the FastAPI server:

```bash
uvicorn api:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## 🔌 API Endpoints

### `GET /`

Checks whether the API is running.

```text
GET /
```

### `GET /system`

Returns system information.

```text
GET /system
```

Example response:

```json
{
    "hostname": "MY-PC",
    
}
```

### `GET /network`

Returns network configuration information.

```text
GET /network
```

Example:

```json
{
    "subnet_mask": "255.255.255.0",
    "default_gateway": "192.168.1.1"
}
```

### `GET /ports`

Returns listening ports.

```text
GET /ports
```

Example:

```json
{
    "listening_ports": [
        {
            "port": "135",
            "pid": "1234",
            "protocol": "TCP"
        }
    ]
}
```

### `GET /test-connection`

Tests whether a TCP connection can be established.

Example:

```text
GET /test-connection?target=127.0.0.1&port=135
```

Example response:

```json
{
    "target": "127.0.0.1",
    "port": 135,
    "status": "OPEN"
}
```

## 🧠 What I Learned

This project was built to develop practical understanding of both **Python programming and networking**.

### Python

* Functions
* Modules
* Dictionaries and lists
* Loops
* Exception handling
* File handling
* JSON parsing
* Working with operating-system commands

### Networking

* IPv4 addresses
* Subnet masks
* Default gateways
* DNS
* ARP
* MAC addresses
* TCP
* Ports
* Listening services
* Process IDs

### Backend Development

* FastAPI
* REST API endpoints
* HTTP GET requests
* JSON responses
* Uvicorn
* Separating application logic into modules

## 🎯 Future Improvements

Planned improvements include:

* Better handling of multiple network adapters
* More reliable ARP parsing
* UDP port detection
* Service identification from PIDs
* Improved error handling and input validation
* Automated network reports
* Authentication for the API
* AI-assisted security analysis
* Detection of potentially unusual network exposure

## 👨‍💻 Project Goal

The goal of Network Detective is to combine **Python, networking, cybersecurity, backend development, and eventually AI** into one practical project.

Rather than learning these topics independently, the project progressively connects them into a single security-oriented application.
