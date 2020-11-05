import hashlib
#MD5加密
def  get_md5(pwd):
    md5=hashlib.md5()  #创建实例对象
    md5.update(pwd.encode('utf-8'))  #加密
    #print(md5.hexdigest())
    return  md5.hexdigest()

import  requests

URL = 'http://120.55.190.222:7080/api/mgr/loginReq'
def  login(inData):
    payload=inData
    response=requests.post(url=URL,data=payload)
    '''
    data：一般为表单数据，  name=tom&age=20    content-type就是表单
    json:json格式       直接传入字典        content-type就是json格式
    params:  参数到url里
    '''
    print(response.headers)
    print(response.url)
    print(response.content)

    #方案一：原生态cookie ---如果后续的接口直接使用这个cookie，不增加其他参数---直接调用使用
    print(response.cookies)
    #方案二：如果后续的接口使用这个cookie，在增加其他参数认证，重新封装cookies
    print(response.cookies['sessionid'])

    print(response.json())
    return  response.cookies,response.cookies['sessionid'],response.json()

def  tmp_eg():
    # 方案一：原生态cookie ---如果后续的接口直接使用这个cookie，不增加其他参数---直接调用使用
    #print(response.cookies)
    cookie1=login(testData)[0]  #返回cookies信息， 返回数据类型：RequestsCookieJar类型
    resp= requests.post('url',cookies=cookie1)

    # 方案二：如果后续的接口使用这个cookie，在增加其他参数认证，重新封装cookies
    #print(response.cookies['sessionid'])
    cookie2=login(testData)[1]    #返回的是sessionID的值
    user_cookie={'sessionid':cookie2}  #对sessionid进行组装使用，可加入token信息
    resp= requests.post('url',cookies=user_cookie)

requests.packages.urllib3.disable_warnings()    #忽略警告
#from  urllib3 import  disable_warnings   #或 urllib3，忽略警告
URLS = 'https://120.55.190.222/api/mgr/loginReq'
def  logins(inData):
    payload=inData
    resp=requests.post(url=URLS,data=payload,verify=False)  #https访问时 不需要进行校验
    print(resp)
    print(resp.json())
    return  resp,resp.json()

if __name__=='__main__':
    testData={'username':'auto','password':'sdfsdfsdf'}
    #login(testData)
    logins(testData)