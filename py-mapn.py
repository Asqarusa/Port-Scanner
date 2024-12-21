import nmap

def nmap_scan(target, ports):
    try:
        # Initialize the scanner
        scanner = nmap.PortScanner()
        print(f"Scanning {target} on ports {ports}...\n")

        # Perform the scan
        scanner.scan(target, ports)

        # Check if the target is up
        if scanner.all_hosts():
            for host in scanner.all_hosts():
                print(f"Host: {host} ({scanner[host].hostname()})")
                print(f"State: {scanner[host].state()}")

                # Display open ports and their services
                if 'tcp' in scanner[host]:
                    for port in scanner[host]['tcp']:
                        state = scanner[host]['tcp'][port]['state']
                        name = scanner[host]['tcp'][port]['name']
                        print(f"Port: {port}\tState: {state}\tService: {name}")
                print("\n")
        else:
            print("No hosts found. Ensure the target is reachable.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    target_ports = input("Enter the port range (e.g., 20-80): ")
    nmap_scan(target_ip, target_ports)
