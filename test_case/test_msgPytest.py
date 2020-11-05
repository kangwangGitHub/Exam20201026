#-*-coding:utf-8-*-
# Author    :wangk
# Data  :2020/10/31  16:34
# Software  :PyCharm
from  lib.apiLib.login import userLogin
from  lib.apiLib.msg import Msg
from   tools.ExcelDataCtl import  get_excel_data
import pytest,allure
#测试类：留言模块
@allure.epic('考试系统----史诗级')
@allure.feature('留言模块')
@pytest.mark.message
class  TestMsg:

    # 1、登录
    #在整个文件中的一个class中所有用例的前后运行
    def  setup_class(self):
        #获取token值， 作为类的属性
        self.tokenValue = userLogin().login(indata={"username":'20200163',"password":'123456'}, getToken=True)

    # 2、添加留言
    #测试方法：添加留言
    #数据驱动，从Excel中获取数据，请求体 和 预期结果
    @allure.story('添加留言')
    @allure.title('添加留言用例')
    @allure.issue('https://www.baidun.com')
    
    @pytest.mark.addMsg
    @pytest.mark.parametrize('inData,expectData',get_excel_data('2-留言模块','msg_add'))
    def  test_addMsg(self,inData,expectData):
        resp=Msg(self.tokenValue).add_msg(inData=inData)
        assert  resp['code']==expectData['code']  and  resp['message']==expectData['message']

    #3、留言列表
    # 测试方法：查看留言
    # 数据驱动，从Excel中获取数据，请求体 和 预期结果
    @allure.story('列出留言')
    @allure.title('列出留言用例')
    @pytest.mark.getMsg    #添加标签，方便用例选择执行
    @pytest.mark.parametrize('inData,expectData',get_excel_data('2-留言模块','msg_list'))
    def test_getMsg(self,inData,expectData):
        #将获取indata字典数据{'page': x, 'value': x}，进行处理传值给inData参数
        resp=Msg(self.tokenValue).get_msg(inData=inData)
        assert   resp['code']==expectData['code']  and resp['message']==expectData['message']

if  __name__=='__main__':
    import os
    for one  in  os.listdir('../report/tmp2'):
        if  'json' in  one:
            os.remove(f'../report/tmp2/{one}')
    #执行测试用例，并生产allure报告的源数据，存放到指定目录下
    #'-m','getMsgList': 根据标签选择，进行执行；  如：getMsgList标签
    pytest.main(['test_msgPytest.py','-s','-k','Msg','--alluredir','../report/tmp2'])

    #启动 allure服务，使用浏览自动打开报告
    os.system('allure serve  ../report/tmp2')

