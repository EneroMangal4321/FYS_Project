import subprocess

correct_user = "enero"

def rerouteRequest():
    output = subprocess.getoutput("iptables -t nat -A PREROUTING -i wlan0ap -p tcp --dport 80 -j DNAT  --to-destination  192.168.1.99:80")
    save_output = subprocess.getoutput("insert save iptable rules")
    print(output)
    print(save_output)
    print("OK")

if __name__ == "__main__":
    rerouteRequest()