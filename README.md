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
cd itieprobe/device1/credential_leakage
sudo python credential_leakage_v1.py check_legitimate.pcapng
or
sudo ./itieprobe/device1/credential_leakage/credential_leakage_v1.py check_legitimate.pcapng 
```
- Purported IoT (V2)

```
cd itieprobe/device1/purported
sudo bash evil_twin.sh [AP-SSID] [AP-MAC] [Channel] [Wi-Fi mon interface]
sudo bash configure_dhcp.sh [DHCP-server-IP] [netmask]
```
- Token Validity (V3) - In V3, the IoT device needs to be in the AP pairing mode, i.e., its Access Point should be UP. The script aspects the Wi-Fi adapter is configured in monitor mode. Otherwise, the exploitation will not inject the packets on the channel but prints the output on the terminal.
  
```
cd itieprobe/device1/tok-valid/
sudo python exploitattion_codev3 tok-valid.pcapng
or
sudo ./itieprobe/device1/tok-valid/exploitation_codev3.py tok-valid.pcapng 
```

- Spooky (V4) - Similar to V3, the script expects the IoT device and the Wi-Fi adapter to run the exploit.
```
cd itieprobe/device1/spooky
sudo python exploitattion_code_v4.py spooky.pcapng
or
sudo ./itieprobe/device1/spooky/exploitattion_code_v4.py spooky.pcapng 
```

- Replaced Token (V5) - In V5, assuming the attacker already had its authentication token. After running the script, it injects the crafted packet with the replaced legitimate token in the pcap for the exploitation.

```
cd itieprobe/device1/replaced-token/
sudo exploitattion_code_v5.py replace_v5.pcapng legitimate_v5.pcapng
or
sudo ./itieprobe/device1/replaced-token/exploitation_code_v5.py replaced_v5.pcapng legitimate_v5.pcapng
```
- Injected Token (V6) - In V6, similar to V5, the script inject the attacker Home-AP credential.
```
cd itieprobe/device1/injected-token
sudo python exploitation_v6.py injected_v6.py
or
sudo ./itieprobe/device1/injected-token/exploitation_v6.py injected_v6.pcapng 
```
- Note: For V3-V6 exploitation, it is assumed that the Wi-Fi adapter and the device specific settings and the correct device is available to the attacker (tester). Otherwise the injected packets will only be printed on the terminal.
