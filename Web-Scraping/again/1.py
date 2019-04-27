from geoip2 import database
import  socket

# 获取本机计算机名称
hostname = socket.gethostname()
# 获取本机ip
ip = socket.gethostbyname(hostname)
reader=database.Reader('./GeoLite2-City.mmdb')
response=reader.city(ip)
print("地区：{}({})".format(response.continent.names["es"],response.continent.names["zh-CN"]))

print("国家：{}({}) ，简称:{}".format(response.country.name, response.country.names["zh-CN"], response.country.iso_code))

print("洲／省：{}({})".format(response.subdivisions.most_specific.name,response.subdivisions.most_specific.names["zh-CN"]))

print("城市：{}({})".format(response.city.name,  response.city.names["zh-CN"]))

print("经度：{}，纬度{}".format(response.location.longitude,response.location.latitude))
