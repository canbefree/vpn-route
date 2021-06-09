import socket


def get_ip(domain):
    myaddr = socket.getaddrinfo(domain, 'http')
    return (myaddr[0][4][0])

def get_ip_list(domain):  # 获取域名解析出的IP列表
    ip_list = []
    try:
        addrs = socket.getaddrinfo(domain, None)
        for item in addrs:
            if item[4][0] not in ip_list:
                ip_list.append(item[4][0])
    except Exception as e:
            pass
    return ip_list

def get_domain_apnic_txt(domain):
    ip = get_ip(domain=domain)


