import ctypes, sys

import optparse
import os 
# from vpnrouter.route import VpnRouter

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    Parse = optparse.OptionParser()
    Parse.add_option("-s", "--short-country", default="cn", help="short countrynames")
    Parse.add_option("-f", "--file", help="file with apnic data ")
    Parse.add_option("-a", "--action", help="enable/disable",default="enable")
    (options, args) = Parse.parse_args()
    if options.action == "enable":
        enable_vpn()
    else:
        print("stop")


def enable_vpn():
    ## 启动VPN
    result = os.popen("rasdial vpn")
    print(result.read())
    ## 获取当前路由
    

    

if is_admin():
    main()
else:
    if sys.version_info[0] == 3:
    	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable,__file__, None, 1)
    main()



