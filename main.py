# /usr/bin/env python

from email.policy import default
import optparse
from vpnrouter import vpnroute


Parse = optparse.OptionParser()


def init_option():
    Parse.add_option("-s", "--short-country", default="cn", help="short countrynames")
    Parse.add_option("-f", "--file", help="file with apnic data ")


if __name__ == "__main__":
    init_option()
    (options, args) = Parse.parse_args()
    print(options,args)
    app = vpnroute.VpnRouter(options.short_country,options.file)
    app.run()
