#-*-coding:utf-8-*-
# Author    :wangk
# Data  :2020/10/31  9:59
# Filename  :PyCharm
''''
未使用框架，实现测试用例的自动化执行
'''
from   lib.apiLib.login import  userLogin
from   tools.ExcelData import Get_Excel_Data
from   tools.ExcelData import Set_write_excel
import json,pprint
import pytest

#登录模块
# class  testLogin:
#     def  login01(self):
#         #1、选择执行的模块，和 需要执行的用例， 获取 请求体、预期响应结果
#         Get_resData=Get_Excel_Data(sheetname='1-登录模块',casename='login')
#         pprint.pprint(Get_resData)
#
#         #调用Excel 写入操作，获取新的Excel 和 操作的表单
#         NewWorkBook,NewWorkSheet=Set_write_excel()  #数据类型：元组
#
#         #2、调用用户  登录接口,  遍历  执行每一条用例
#         num_idx=1
#         for one  in   Get_resData:
#             #2-1  获取请求的 实际响应结果
#             resp=userLogin().login(indata=one[0])
#             print(resp)
#             #2-2  将实际结果 写入到新的Excel中;
#             #json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
#             NewWorkSheet.write(num_idx,9,json.dumps(resp,ensure_ascii=False))
#             #2-3 将用例的执行结果写入Excel， 期望结果和预期结果进行对比
#             if  resp['code']== one[1]['code'] and  resp['message']== one[1]['message']:
#                 #print(f'用例：{one[2]}--PASS--')
#                 print('--PASS--')
#                 NewWorkSheet.write(num_idx,10,'PASS')
#             else:
#                 #print(f'用例：{one[2]}--FAIL--')
#                 print('-FAIL--')
#                 NewWorkSheet.write(num_idx, 10, 'FAIL')
#             num_idx+=1
#
#         #3、保存Excel,（注意：使用.xlsx，保存文件有问题：打不开文件）
#         NewWorkBook.save('../data/newTestResult.xls')

#测试类
class  TestLogin1:
    #测试方法
    @pytest.mark.parametrize('inData,respData',Get_Excel_Data(sheetname='1-登录模块',casename='login'))  # parametrize('变量','值')
    def  test_login01(self,inData,respData):
        #调用--封装模块
        resp=userLogin().login(indata=inData)
        #断言： 实际结果与预期结果进行比较
        assert resp['code']==respData['code']
        assert resp['message'] == respData['message']

if  __name__=='__main__':
    #testLogin().login01()
    #-s：输出打印信息; -q: 简化输出
    #--allure=../report/tmp1---- 生成allure报告需要的的源数据
    pytest.main(['testLogin.py','-s','--alluredir','../report/tmp1'])

    # 生成报告
    #方案一：allure  generate  --生成报告
    #方案二 ：allure serve   --启服务  --自动打开浏览器--- 需要设置默认浏览器（火狐/谷歌）
    import  os
    os.system('allure serve  ../report/tmp1')
