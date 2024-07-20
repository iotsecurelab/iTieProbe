# iTieProbe
Testing of vulnerabilities in IoT devices in the Provisioning Phase


**Features:**

- Wi-Fi Pairing modes
- 2.4Ghz
- Supports all WiFi devices
- Provisioning state
- Interactive testing
  
## Building

- Install dependencies (Scapy)
```
sudo apt install python-pip
pip install scapy
```
- (Aircrack-ng)
```
- sudo apt-get install -y aircrack-ng
```

## Run

- Replaced Token (V5)
```
sudo ./itieprobe/replace_token_v5/exploitation_code_v5.py replay_v5.pcapng 
```
