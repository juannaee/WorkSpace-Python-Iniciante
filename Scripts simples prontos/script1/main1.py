import os


def ping_google_dns():
    os.system("ping -t 8.8.8.8")


if __name__ == "__main__":
    ping_google_dns()
