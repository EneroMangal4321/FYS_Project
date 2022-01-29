import subprocess


def rerouteRequest(user_ip):
    update_rules = subprocess.getoutput(f"sudo iptables -t nat -I PREROUTING -s {user_ip} -j ACCEPT")
    save_rules = subprocess.getoutput("sudo netfilter-persistent save")
    reload_iptable = subprocess.getoutput("sudo netfilter-persistent reload")
    print(update_rules)
    print(save_rules)
    print(reload_iptable)
    print("OK")

    # base_rule = "sudo iptables --table nat --append PREROUTING --protocol tcp --dport 443 --jump DNAT --to-destination 192.168.3.2:5000"
    # base_rule = "sudo iptables --table nat --append PREROUTING --protocol udp --dport 443 --jump DNAT --to-destination 192.168.3.2:5000"

    # base_rule = "sudo iptables --table nat --append PREROUTING --protocol tcp --dport 80 --jump DNAT --to-destination 192.168.3.2:5000"
    # base_rule = "sudo iptables --table nat --append PREROUTING --protocol udp --dport 80 --jump DNAT --to-destination 192.168.3.2:5000"

if __name__ == "__main__":
    rerouteRequest()