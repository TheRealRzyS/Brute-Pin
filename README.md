Brute-Force 4-Digit PIN via HTTP
This repository contains a multithreaded Python script that attempts to brute-force a 4-digit PIN by sending HTTP requests to a target server. The script is optimized for efficiency, error handling, and maintainability.

Features
- Multithreading: Uses concurrent requests to significantly speed up brute-force attempts.
- Graceful Exit: Stops execution immediately when the correct PIN is found.
- Robust Error Handling: Prevents crashes from connection failures, timeouts, and invalid responses.
- Command-Line Arguments: Allows dynamic IP and port selection instead of hardcoded values.

Installation
1. Clone the repository:
git clone https://github.com/yourusername/repo-name.git
cd repo-name

2. Install dependencies: 
pip install -r requirements.txt

Usage
Run the script with the target IP and port:
python brute_force.py <target_ip> <target_port>

Example:
python brute_force.py 192.168.1.10 8080


Notes
- The script assumes the server expects a GET request in the format: http://<IP>:<PORT>/pin?pin=XXXX
- If the target requires a POST request, modifications will be necessary.
- Rate-limiting defenses on the target may affect performance.


Legal Disclaimer:
This tool is intended for educational and authorized penetration testing only. Unauthorized use on systems you do not own or have explicit permission to test is illegal.
