import time
from urllib.request import urlopen


def GetApincFileContext():
    f = urlopen(
        url="http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest")
    while True:
        line = f.readline()
        if line == b"":
            return b""
        yield line


def BackupApincFile():
    t = time.strftime("%Y%m%d", time.localtime())
    file = "./data/apnic_ip/" + t + ".log"

    gen = GetApincFileContext()
    with open(file, "w+") as f:
        while True:
            line = next(gen)
            if line == b"":
                break
            f.write(bytes.decode(line))

def FetchIpData():
    gen = GetApincFileContext()
    while True:
        line = next(gen)
        line = bytes.decode(line)
        if line == "":
            break
            