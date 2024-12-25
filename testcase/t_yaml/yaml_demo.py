import yaml
from utils.YamlUtil import YamlReader
# 读取单个内容
# with open("./data.yml", "r", encoding='utf-8') as f:
#     r = yaml.safe_load(f)
#     print (r)

# 读取多个内容
# with open("./data.yml", "r", encoding='utf-8') as f:
#     r = yaml.safe_load_all(f)  #要用all方法读取多个
#     for i in r:
#         print(i)

res = YamlReader("./data.yml").data_all()
print(res)
