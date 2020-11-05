import   requests,hashlib
from  configs.cfg import  host
from   pprint import  pprint

URL = f'{host}/api/loginS'  #登录URL
#登录
class  userLogin:
    # 登录密码MD5加密
    def  get_md5(self,pwd):
        md5=hashlib.md5()   #创建一个hash  md5对象
        md5.update(pwd.encode('utf-8'))  #对指定字符串进行转码，加密（每次使用update之前都要重新定义：md5=hashlib.md5()）
        return  md5.hexdigest()  #返回加密结果,16进制

    '''
    登录接口
    url:：http://121.41.14.39:9097/api/loginS
    请求方式：POST
    请求消息体：{
                "username": "20154084",
                "password": "e10adc3949ba59abbe56e057f20f883e"
                }Username ：用户名  password ：md5 加密后的密码。
    响应消息（成功）：
    {
    "flag": "松勤教育",
    "code": 200,
    "message": "登录成功",
    "token": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJzcSIsInN1YiI6InNxIiwiaWF0IjoxNTk1NjgzM
    DczfQ.SnMF9Eg_9EkoMZy8vNQo1H-l9_cKfEU5knGqVDRUBmE",
    "data": {.......}
    }
    响应消息（失败）：
    {
    "flag": "松勤教育",
    "code": 400,
    "message": "密码错误",
    "data": null,
    "token": null
    }
    '''

    def login(self,indata,getToken=False):
        '''
        data    一般是表单
        json    json格式
        files   文件
        '''
        #payload={"username":username,"password":pwd}  #请求体
        payload=indata       #请求体
        payload['password']=self.get_md5(payload['password'])
        resp=requests.post(url=URL,json=payload)

        if  getToken:#获取token
            return  resp.json()['token']   #获取token
        else:
            return  resp.json()          #获取响应结果，返回 字典格式

        # pprint(resp.json())
        # return  resp.json()

if __name__ =='__main__':
    testdata={"username":'20200163',"password":'123456'}
    # passwordMd5=userLogin().get_md5('123456')
    # userLogin().login('20200163',passwordMd5,getToken=True)

    response=userLogin().login(testdata)#,getToken=True
    print(response)

