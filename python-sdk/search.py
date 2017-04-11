#-*- coding: utf-8 -*-

#将需要识别的图片和集合对比

#------------------------------------------------------------------------------
#准备阶段
API_KEY = "feI5hwgMw9zQKaDmDCjq1SFdVZynhy38"
API_SECRET = "y8NTlkYNLJQOmGErZzGUnegmUZROER0r"
#国际版的服务器地址
api_server_international = 'https://api-us.faceplusplus.com/facepp/v3/'
# 导入系统库并定义辅助函数
from pprint import pformat
def print_result(hit, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(v): encode(k) for (v, k) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hit
    result = encode(result)
    print '\n'.join("  " + i for i in pformat(result, width=75).split('\n'))
#导入SDK中的API类
from facepp import API, File
#创建一个API对象
api = API(API_KEY, API_SECRET)

#-----------------------------------------------------------------------------
# 本地图片的地址
face_search = './gtl.jpeg'
# 对待比对的图片进行检测
Face = {}
res = api.detect(image_file=File(face_search))
print_result("face_search", res)
Face['face_search'] = res["faces"][0]["face_token"]
#搜索相似脸
search_result = api.search(face_token=res["faces"][0]["face_token"], outer_id='face')
# 输出结果
print_result('对比结果', search_result)


