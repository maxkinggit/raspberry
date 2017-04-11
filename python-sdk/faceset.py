#-*- coding: utf-8 -*-

#把已知人脸添加到人脸集合中

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

# 创建一个Faceset用来存储FaceToken
ret = api.faceset.create(outer_id='face')
# 本地图片的地址
face_one = './gtl2.jpeg'
face_two = './demo.jpeg'
# 对图片进行检测
Face = {}
res = api.detect(image_file=File(face_one))
print_result("person_one", res)
Face['person_one'] = res["faces"][0]["face_token"]
res = api.detect(image_file=File(face_two))
print_result("person_two", res)
Face['person_two'] = res["faces"][0]["face_token"]
# 将得到的FaceToken存进Faceset里面
api.faceset.addface(outer_id='face', face_tokens=Face.itervalues())

