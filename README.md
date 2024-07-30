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
- (ISC-DHCP Software)
```
sudo apt-get install isc-dhcp-server
```

## Run

- Credential Leakage (V1) - In Credential Leakage, the exploitation code returns the sniffed credential from the pcap. The Script does no require the Wi-Fi adapter and the IoT device for the execution.
```
sudo ./itieprobe/device1/[<credential-leakage>]/<code.py> file1.pcapng 
```
- Purported IoT (V2)

```
cd itieprobe/device1/purported
sudo bash evil_twin.sh [AP-SSID] [AP-MAC] [Channel] [Wi-Fi mon interface]
sudo bash configure_dhcp.sh [DHCP-server-IP] [netmask]
```
- Token Validity (V3) - In V3, the IoT device needs to be in the AP pairing mode, i.e., its Access Point should be UP. The script aspects the Wi-Fi adapter is configured in monitor mode. Otherwise, the exploitation will not inject the packets on the channel but prints the output on the terminal.
  
```
sudo ./itieprobe/device1/[<vulnerability directory>]/<code.py> file1.pcapng 
```

- Spooky (V4) - Similar to V3, the script expects the IoT device and the Wi-Fi adapter to run the exploit.
```
sudo ./itieprobe/device1/[<vulnerability directory>]/<code.py> file1.pcapng 
```

- Replaced Token (V5) - In V5, assuming the attacker already had its authentication token. After running the script, it injects the crafted packet with the replaced legitimate token in the pcap for the exploitation.
```
sudo ./itieprobe/device1/[<vulnerability directory>]/<code.py> file1.pcapng file2.pcapng
```
- Injected Token (V6) - In V6, similar to V5, the script inject the attacker Home-AP credential.
```
sudo ./itieprobe/device1/[<vulnerability directory>]/<code.py> file1.pcapng 
```
- Note: For V3-V6 exploitation, it is assumed that the Wi-Fi adapter and the device specific settings and the correct device is available to the attacker (tester). Otherwise the injected packets will only be printed on the terminal.
