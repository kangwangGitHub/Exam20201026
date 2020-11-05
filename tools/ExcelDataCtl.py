import  xlrd
from  xlutils.copy  import   copy
import  json

#用例文件
excelDir = '../data/在线考试系统接口测试用例-v1.3.xls'

#获取Excel数据 --- 请求体 +预期结果
def   get_excel_data(sheetName,casename):
    '''
    :param sheetName:  表名
    :param casename:  用例名
    :return:  一个列表嵌套元组  [(请求体1，期望数据1),(请求体2，期望数据2)]
    '''
    resList=[] #存放结果
    #1、打开excel对象--- formatting_info=Ture  保持样式
    workBook=xlrd.open_workbook(filename=excelDir,formatting_info=True)
    #2、对某一个 sheet操作
    workSheet=workBook.sheet_by_name(sheetName)
    #3、获取某几列的值
    cellvalue=workSheet.col_values(0)
    #print(cellvalue)

    #4、获取数据
    idx=0
    for one  in workSheet.col_values(0):
        if  casename in  one:  #说明这条用例是 我们需要的
            requestBody=workSheet.cell_value(idx,6)   #请求体-- 单元格数据-- cell（行号，列号）从0开始
            expactData=workSheet.cell_value(idx,8)    #期望数据
            #将每一行数据增加 到list中
            resList.append((json.loads(requestBody),json.loads(expactData)))  #json格式数据转换为dictionary格式
        idx+=1
    print(resList)
    return resList

'''
练习数据，未被调用
'''
def   get_excel_data2(sheetName):#,casename
    resList=[] #存放结果
    #1、打开excel对象--- formatting_info=Ture  保持样式
    workBook=xlrd.open_workbook(filename=excelDir,formatting_info=True)
    #2、对某一个 sheet操作
    workSheet=workBook.sheet_by_name(sheetName)
    #3、获取某几列的值
    cellvalue=workSheet.col_values(0)
    print(cellvalue)
'''
w_excel()函数：目前无用，仅供参考
'''
def  w_excel(expactResult):
    #复制Excel文件
    workBook=xlrd.open_workbook(filename=excelDir,formatting_info=True)
    workSheet=workBook.sheet_by_name('Sheet2')
    print(workSheet.cell_value(1,8))
    newWorkBook=copy(workBook)              #复制工作薄
    #获取操作操作表单
    newSheet=newWorkBook.get_sheet(1)   #获取一个工作表
    newSheet.write(1,9,expactResult)
    newSheet.write(1, 10,'info1')
    #3、获取某几列的值
    # cellvalue=newworkSheet.col_values(0)
    # print(cellvalue)
    # #在指定位置写入数据
    # for  casename in
    # newworkSheet.write(idx,9)
    #保存Excel文件
    newWorkBook.save('../data/tc02.xls')

if  __name__=="__main__":
    #get_excel_data2('1-登录模块')
    #responseData = get_excel_data('1-登录模块', 'login')
    responseData = get_excel_data('2-留言模块','msg_list')  #f返回的是列表

    for  one  in  responseData:
        #inData, expectData=one
        print(one)
        # print(inData['page'],inData['value'])
    #w_excel()