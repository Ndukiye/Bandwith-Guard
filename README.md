# Bandwidth Guardian
A lightweight CLI tool for monitoring network bandwidth usage on Ubuntu Linux.



## Features
- Tracks daily bandwidth consumption
- Runs as a systemd background service
- Allows you set and manage data plan and balance
- Allows you set and manage data usage limit
- Tracks network speed mbps



## Installation
1. Install Python dependencies:
```bash
   pip3 install -r requirements.txt
```
   
2. Edit `bandwidth-guardian.service`:
   - Replace `YOUR_USERNAME` with your Ubuntu username
   - Update paths to match your project location

3. Install and start the service:
```bash
   sudo cp bandwidth-guardian.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable --now bandwidth-guardian
```

4. Verify it's running:
```bash
   sudo systemctl status bandwidth-guardian
```



## Usage
Run the CLI menu:
```bash
python3 main.py
```
**Menu Options:**
- **Option 1:** View current bandwidth usage, speed, and plan details
- **Option 2:** Configure data plan and usage limit
- **Option 3:** Exit

**Note:** The monitoring service runs independently in the background. The CLI just reads and displays the data it collects.



## Technical Stack
 - Python3
 - psutil library (for network I/O monitoring)
 - rich library (for terminal UI)
 - Systemd (for service management)
 - JSON (for data persistence)

