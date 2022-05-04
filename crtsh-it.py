import argparse
import re
import requests
import time

BANNER = """
 ██████╗██████╗ ████████╗███████╗██╗  ██╗      ██╗████████╗
██╔════╝██╔══██╗╚══██╔══╝██╔════╝██║  ██║      ██║╚══██╔══╝
██║     ██████╔╝   ██║   ███████╗███████║█████╗██║   ██║   
██║     ██╔══██╗   ██║   ╚════██║██╔══██║╚════╝██║   ██║   
╚██████╗██║  ██║   ██║   ███████║██║  ██║      ██║   ██║   
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝      ╚═╝   ╚═╝   
"""
# It's pronounced SEARCH IT!

IS_URL = re.compile(r"^\S[-a-zA-Z0-9@:%._\+*~#=]{1,256}\.[a-zA-Z0-9()]*\b[a-zA-Z0-9()@:%_+.~#?&=]*\S$")

print(BANNER)

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", required=True, help="Domain name to query to crt.sh.", type=str)
parser.add_argument("-r", "--resolve", required=False, help="Attempt to resolve discovered domains through Cloudflare DNS over HTTPS.", action="store_true")
parser.add_argument("-v", "--verbose", required=False, help="Verbose output.", action="store_true")
parser.add_argument("-q", "--quiet", required=False, help="Prints successes and mandatory errors.", action="store_true")

args = parser.parse_args()

if args.quiet and args.verbose:
    print("Quiet and verbose flag cannot be used at the same time.")
    exit(1)

elif not re.match(IS_URL, args.domain):
    print("Please input a valid domain name.")
    exit(1)

def main():
    if not args.quiet:
        print(f"[.] Searching crt.sh for certificate logs for the domain: {args.domain} . . ." )

    resp = requests.get(f"https://crt.sh/?q={args.domain}&output=json")

    if resp.status_code == 502:
        count = 0
        while count != 3 and resp.status_code == 502: 
            if count == 3:
                print("[-] Error connecting to crt.sh, site may be down.")
                exit(1)
            
            if not args.quiet:
                print("[!] Error 502 bad gateway, trying again!")
            time.sleep(1)
            resp = requests.get(f"https://crt.sh/?q={args.domain}&output=json")
            count += 1
            
    entries = resp.json()


    names = [entry["name_value"] for entry in entries]

    identities = [[i for i in name.split("\n")] for name in names]
            
    domains = []
    for identity in identities:
        for domain in identity:
            if re.match(IS_URL, domain):
                domains.append(domain)

            
    domains = sorted(list(set(domains)))

    for domain in domains:
        if args.quiet:
            print(f"{domain}")
        else:
            print(f"[+] {domain}")
        
        
    if args.resolve:
        print("\n[.] Resolving acquired domains . . .")
        for domain in domains:
            resp = requests.get(f"https://1.1.1.1/dns-query?name={domain}", headers={"Accept": "application/dns-json"}).json()
            match int(resp["Status"]):
                case 0:
                    if args.quiet:
                        print(f"{domain}")
                    else:
                        print(f"[+] {domain}")
                    try:
                        for answer in resp["Answer"]:
                            print("\t" + answer['data'])
                    except:
                        if not args.quiet:
                            print("\t No answer")
                case 1:
                    if args.verbose:
                        print(f"[!] Format error: {domain}")
                    if args.quiet:
                        pass
                case 2:
                    if not args.quiet:
                        print(f"[!] Server failure: {domain}")
                case 3:
                    if args.verbose:
                        print(f"[-] {domain}")
                    if args.quiet:
                        pass
                case 4:
                    if args.verbose:
                        print(f"[!] Not implemented: {domain}")
                    if args.quiet:
                        pass
                case 5:
                    if args.verbose:
                        print(f"[!] Query refused: {domain}")
                    if args.quiet:
                        pass

if __name__ == '__main__':
    main()
    

