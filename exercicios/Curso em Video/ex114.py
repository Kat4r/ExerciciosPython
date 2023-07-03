import urllib.request

url = 'https://www.facebook.com/'
try:
    with urllib.request.urlopen("https://www.facebook.com/") as site:
        print(f"O site {url} está acessivel")

except Exception:
    print(f"o site não está acessivel")


