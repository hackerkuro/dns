import sys
import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None

# コマンドライン引数が正しく指定されているかチェック
if len(sys.argv) == 2 and sys.argv[1] == "-h":
    print("sample: python dns.py <domain>")
    sys.exit(0)
elif len(sys.argv) != 2:
    print("Invalid number of arguments.")
    print("Usage: python script.py <domain>")
    sys.exit(1)

# コマンドライン引数からドメイン名を取得
domain = sys.argv[1]

# IPアドレスを取得して表示
ip_address = get_ip_address(domain)
if ip_address:
    print(f"The IP address of {domain} is: {ip_address}")