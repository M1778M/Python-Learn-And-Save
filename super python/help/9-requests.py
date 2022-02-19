import requests

def are(url):
    are=input("Do You Want Get Codes From Url?[/Y/n]::")
    if are=="y":
        print(url.text)
    elif are=="Y":
        print(url.text)
    else:
        pass
def main():
    url=input("Enter Url::")
    if "https://" in url:
        requests.get(url)
        are()
    elif "http://" in url:
        requests.get(url)
        are()
    else:
        print("url notfound!")
        exit()


if __name__ == '__main__':
    main()
