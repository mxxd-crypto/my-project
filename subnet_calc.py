import ipaddress

def calculate_subnet(ip_input):
    try:
        # The strict=False flag allows the user to input a host IP (like 192.168.1.5/24)
        # instead of just the network address (192.168.1.0/24)
        network = ipaddress.ip_network(ip_input, strict=False)
        
        print("\n" + "="*40)
        print(f" NETWORK REPORT: {ip_input}")
        print("="*40)
        print(f"Network Address:   {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Netmask:           {network.netmask}")
        print(f"Total Usable Hosts: {network.num_addresses - 2}")
        print(f"Address Type:      {'Private' if network.is_private else 'Public'}")
        print("-" * 40)
        
    except ValueError:
        print("\nERROR: Invalid IP address or CIDR notation.")
        print("Usage Example: 192.168.1.0/24")

# Terminal Entry Point
if __name__ == "__main__":
    user_input = input("Enter IP/CIDR: ")
    calculate_subnet(user_input)