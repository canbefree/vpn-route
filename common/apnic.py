'''
    Apnic
'''
import re
import time
from urllib.request import urlopen
import os


def request_apinc_context():
    '''
        获取ip地址信息
    '''
    f = urlopen(
            url="http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest")
    while True:
        line = f.readline()
        if line == b"":
            return b""
        yield line

def genarate_ipinfo_from_file(file):
    if os.path.exists(file) == True:
        with open(file,"r") as f:
            while True:
                line = f.readline()
                if line == "":
                    break
                res = get_apnic_ipinfo(line)
                print(res)

def dowload_apinc():
    '''
        备份当前ip数据
    '''
    t = time.strftime("%Y%m%d", time.localtime())
    file = "./data/apnic_ip/" + t + ".log"

    gen = request_apinc_context()
    with open(file, "w+") as f:
        while True:
            line = next(gen)
            if line == b"":
                break
            f.write(bytes.decode(line))




def get_apnic_ipinfo(line: str,short_country:str="cn") -> tuple:
    '''
        @param line str
    '''
    pattern = r"apnic\|{}\|ipv4\|[0-9\.]+\|[0-9]+\|[0-9]+\|allocated".format(
        short_country)
    regx = re.compile(pattern, re.IGNORECASE)
    res = regx.match(line)
    ipinfo = ()
    if res is not None:
        row = res .group()
        items = row.split('|')
        ip = items[3]
        num_ip = int(items[4])

        imask = 0xffffffff ^ (num_ip-1)
        # convert to string
        imask = hex(imask)[2:]
        mask = [0]*4
        mask[0] = imask[0:2]
        mask[1] = imask[2:4]
        mask[2] = imask[4:6]
        mask[3] = imask[6:8]

        # convert str to int
        mask = [int(i, 16) for i in mask]
        mask = "%d.%d.%d.%d" % tuple(mask)
        return (ip,mask)
    return ipinfo
