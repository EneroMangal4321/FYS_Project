import subprocess

correct_user = "enero"

def check_loggedin():
    user = str(input("Enter your name. "))
    print(user)

    if user != correct_user:
        while user != correct_user:
            user = str(input("Enter your name. "))
            print(user)

            if user == correct_user:
                return rerouteRequest()

    elif user == correct_user:
        return rerouteRequest()

def rerouteRequest():
    output = subprocess.getoutput("iptables -t nat -A PREROUTING -i wlan0ap -p tcp --dport 80 -j DNAT  --to-destination  192.168.1.99:80")
    save_output = subprocess.getoutput("insert save iptable rules")
    print(output)
    print(save_output)
    print("OK")

if __name__ == "__main__":
    check_loggedin()