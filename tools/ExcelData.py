#Python 操作Excel

import   xlrd,json   #读取
from xlutils.copy import copy   #写入
from lib.apiLib import  login
import pprint
#操作的 用例文件
ExcelDir  ='../data/在线考试系统接口测试用例-v1.3.xls'

#获取Excel中 需要的数据,如：返回包含请求体、期望结果数据的 列表
def  Get_Excel_Data(sheetname,casename):
    # 存放Excel读取的结果，包括  请求体、 预期响应结果
    resultListExcel=[]

    #1、打开Excel对象 ---  formatting_info=True  保持Excel原有样式
    workBook=xlrd.open_workbook(filename=ExcelDir,formatting_info=True)

    #2、对一个sheet操作，#获取某一个指定的表，通过表名 易懂操作哪个张表
    workSheet = workBook.sheet_by_name(sheetname)

    #3、获取Excel单元格数据；如：（第X列，第Y行）、整行、整列；
    #cellData_caseID = workSheet.cell_value(1, 0)  #获取指定的单元格数据， 如：用例ID
    col_AllCaseID=workSheet.col_values(0) #获取指定列的所有值，如：用例ID列的所有值；返回数据类型list

    #3-1、获取指定 需要的用例及对应数据，如：只获取登录的用例或 添加操作的用例
    num_idx=0
    for  one  in  col_AllCaseID:  #遍历  用例编号列表
        if  casename in  one: #判断 获取需要 EXcel中的用例，如：login的相关用例，原因：Excel用例编写不受格式限制
            #获取请求体、预期结果信息,并追加到list中；   下面两种格式都可以获取单元格数据
            requestBody=workSheet.cell_value(num_idx,6)   #EXcel获取数据类型：string
            expectData=workSheet.cell(num_idx,8).value

            caseId=workSheet.cell(num_idx,0).value
            #print(caseId)
            #将存放到列表中的元素  数据格式转换为dict
            # resultListExcel.append((json.loads(requestBody),
            #                         json.loads(expectData),
            #                         caseId)) #以元组 格式存放到list中
            resultListExcel.append((json.loads(requestBody),json.loads(expectData)))  # 以元组 格式存放到list中
        num_idx+=1

    #4、获取数据, 返回：包含请求体、期望结果数据的，列表（嵌套元组 ，格式：[(请求体1，期望数据1)，(请求体2，期望数据2)]）
    return  resultListExcel #,cellData_caseID

#将用例运行后的测试结果，写入到新的Excel中
'''
优化：对那个表进行操作，可进行传参 处理
'''
def Set_write_excel(): #caseID, dictResponse
    # 1、打开Excel对象 ---  formatting_info=True  保持样式
    workBook = xlrd.open_workbook(filename=ExcelDir, formatting_info=True)
    #2、保留原来的Excel，复制一个新的Excel;(目的：不影响原始数据)
    NewWorkBook=copy(workBook)
    #3、固定格式.get_sheet(sheet下标)，对一个sheet操作
    NewWorkSheet=NewWorkBook.get_sheet(1)   #获取第2个表单
    #4、 返回新的workbook对象 和  操作表单
    return  NewWorkBook,NewWorkSheet


if __name__=='__main__':
    '''
    思路：
    #获得Excel 数据---  请求体+ 预期结果
    #数据传入接口代码--请求体
    #写入测试结果    pass/fail   预期结果与实际结果对比
    '''
    #1  获取 指定表单 中的  某一类型的测试用例 数据
    resdata=Get_Excel_Data('1-登录模块','login')  #返回数据类型：list
    pprint.pprint(resdata)

    #2  调用登录接口，执行用例
    NewWorkBook,NewWorkSheet= Set_write_excel()    #调用EXcel写操作，写到新的Excel 表单中；数据类型：tuple
    num=1
    for  one  in  resdata:
        Actual_response=login.userLogin().login(one[0])   #返回真实的 执行结果；数据格式：dictionary
        print(Actual_response)
        #2-1  将实际的 响应结果 写入 Excel中
        NewWorkSheet.write(num,9,json.dumps(Actual_response,ensure_ascii=False))

        #2-2  用例：写入测试结果:pass/fail, 预期结果与实际结果对比
        if  Actual_response['code']==one[1]['code']  and  \
            Actual_response['message'] ==one[1]['message']:
            # print(f'用例：{one[2]}--PASS--')
            print('--PASS--')
            NewWorkSheet.write(num,10,'PASS')
        else:
            # print(f'用例：{one[2]}--FAIL--')
            print('-FAIL--')
            NewWorkSheet.write(num, 10, 'FAIL')
        num+=1

    #3、保存新的Excel （注意：使用.xlsx，保存文件有问题：打不开文件）
    NewWorkBook.save('../data/res_wk.xls')
