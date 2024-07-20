# iTieProbe
Testing of vulnerabilities in IoT devices in the Provisioning Phase

<img src="https://github.com/iotsecurelab/iTieProbe/blob/main/images/setup.jpg" width="500px">


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

- Credential Leakage (V1), Token Validity (V3), Spooky (V4), Injected Token (V6)
```
sudo ./itieprobe/device1/[<vulnerability directory>]/<code.py> file1.pcapng 
```

- Purported IoT (V6)

```
First, run the evil twin and then run the DHCP configuration and use the monitor_mode bash script of utilities
to bring the Wi-Fi adapter in monitor mode.
cd itieprobe/device1/purported
sudo bash evil_twin.sh [AP-SSID] [AP-MAC] [Channel] [Wi-Fi mon interface]
sudo bash configure_dhcp.sh [DHCP-server-IP] [netmask]
```

- Replaced Token (V5)
```
sudo ./itieprobe/device1/[<vulnerability directory>]/<code.py> file1.pcapng file2.pcapng
```
