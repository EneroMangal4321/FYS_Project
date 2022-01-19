import subprocess

correct_user = "enero"

# sudo apt-get install iptables-persistent
def rerouteRequest():
    output = subprocess.getoutput("iptables -t nat -A PREROUTING -i wlan0ap -p tcp --dport 80 -j DNAT  --to-destination  192.168.1.99:80")
    output1 = subprocess.getoutput("iptables -t nat -A PREROUTING -i wlan0ap -p tcp --dport 443 -j DNAT  --to-destination  192.168.1.99:80")
    save_output = subprocess.getoutput("sudo /etc/init.d/iptables-persistent save")
    print(output)
    print(output1)
    print(save_output)
    print("OK")

if __name__ == "__main__":
    rerouteRequest()