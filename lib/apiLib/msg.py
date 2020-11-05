import requests
from configs.cfg import  host
from  lib.apiLib.login import  userLogin  #导入登录模块
import pprint

MsgURL=f'{host}/api/message'        #添加留言
Get_url=f'{host}/api/messages'  #/1/4 #留言列表
class  Msg:
    #操作留言，需要token 值
    def  __init__(self,tokenValue):
        self.headers={'X-AUTH-TOKEN':tokenValue}   #请求头

    #添加留言
    def  add_msg(self,inData):
        #headers={'X-AUTH-TOKEN':tokenValue}          #构建请求头
        #payload={"title":title,"content":content}    #构建请求体
        payload = inData  # 构建请求体
        resp=requests.post(url=MsgURL,json=payload,headers=self.headers)
        return resp.json()

    #留言列表
    def get_msg(self,inData):#page,size
        #inData 参数为字典格式：{'page': x, 'value': x}，进行处理传值给 对应的page、size参数
        #格式：/api/messages+  /1/10
        paramsData=f"/{inData['page']}/{inData['value']}"

        resp=requests.get(url=Get_url+paramsData,headers=self.headers)
        print(resp.json())
        return resp.json()

    #回复留言
    def replay_msg(self):
        pass

    #删除留言
    def delete_msg(self):
        pass


if  __name__ =='__main__':
    #1、用户登录,获取token值
    Get_Token=userLogin().login({"username":'20200163',"password":'123456'},getToken=True) #登录，并返回token值
    print(Get_Token)

    #2、添加留言
    res=Msg(Get_Token).add_msg(inData={'title':'留言内容002','content':'留言内容002'})
    pprint.pprint(res)

    #3、列出留言
    inData={'page': 0, 'value': 1}
    print(type(inData['page']))
    res1=Msg(Get_Token).get_msg(inData=inData)
    pprint.pprint(res1)

