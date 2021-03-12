'''
    初始化apnic数据
    sqllite
'''



apnic_url = "http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest"


def get_apnic_data():
    '''
        获取apnic
    '''
    f = urlopen(apnic_url)
    while True:
        line = f.readline()
        if line == b"":
            return b""
        yield line
