
import  pytest,allure
from  lib.apiLib  import  login
from   tools.ExcelDataCtl import  get_excel_data
import os

class  Test_sq:
    def  test_001(self):
        print(u'---开始执行----')
        assert  (1+1)==1
        print(u'----结束执行-----')

    def  test_002(self):
        print(u'---开始执行----')
        assert  (1+1)==2
        print(u'----结束执行-----')

# 1、获得Excel 数据---  请求体+ 预期结果
# 2、数据传入接口代码--请求体
# 3、写入测试结果    pass/fail   预期结果与实际结果对比
responseData = get_excel_data(sheetName='1-登录模块', casename='login')
# 1-登录的测试类
@allure.feature('用户登录功能')  # 用feature 说明产品需求
class TestLogin:
    #[(1,2),(2,4)]  数据来源于Excel（即请求体（用户登录信息）、预期结果（预期请求响应结果））
    @pytest.mark.parametrize('inBody,expectData',responseData)#pytest 数据驱动法； 开发自己写--需要一个for
    @allure.story('不同场景验证登录')  #用story 说明用户场景
    def  test_login001(self,inBody,expectData):
        #2-  调用登录接口代码
        resp=login.userLogin().login(indata=inBody,getToken=False)
        #3- 预期结果---Excel里与实际结果对比
        assert resp['message'] == expectData['message']
        assert resp['code'] == expectData['code']
        assert resp['data']==expectData['data']


if  __name__ =='__main__':
    #清除report/tmp下的 执行用例结果数据
    for  one  in  os.listdir('../report/tmp'):
        if  'json' in one:
            os.remove(f'../report/tmp/{one}')

    # 框架执行后的结果数据  --alluerdir:用于存放结果数据
    pytest.main(['test_loginPytest.py','-s','--alluredir','../report/tmp'])

    #下面的语句执行时，提示  ../report/tmp 不存在
    #os.system('allure generate  ../report/tmp -o  ../report/tmp --clean')

    #使用alluer 应用，去打开这个结果数据;  并且 浏览器访问（建立使用火狐/谷歌）； #alluer serve 启服务
    os.system('allure serve  ../report/tmp')



