
from urllib.request import urlopen
import re
'''
    初始化apnic数据
    sqllite
'''


APNIC_URL = "http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest"


def get_apnic_data(url = APNIC_URL):
    '''
        获取apnic
    '''
    f = urlopen(url)
    while True:
        line = f.readline()
        ip_info = get_apnic_ipinfo(line)
        if len(ip_info) == 0:
            continue
        yield ip_info


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




