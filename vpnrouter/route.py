

# from common.apnic import GetApincFileContext
# import re

# class VpnRouter():
    
#     def __init__(self,short_country,file):
#         self.short_country = short_country
#         self.file = file

#     def run(self):
#         if self.file == None:
#             pass
#         print(self.short_country)
#         print(self.file)
#         self._get_route()

#     def _get_route(self):
#         gen = GetApincFileContext()
#         while True:
#             line = next(gen)
#             line = bytes.decode(line)
#             if line == "":
#                 break
#             get_ip_data(line,self.short_country)


# def get_ip_data(line,short_country):
#     pattern = r"apnic\|{}\|ipv4\|[0-9\.]+\|[0-9]+\|[0-9]+\|allocated".format(short_country)
#     regx = re.compile(pattern,re.IGNORECASE)
#     data = regx.match(line)
#     if data != None:
#         print(data)