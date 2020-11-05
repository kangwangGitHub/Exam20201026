#-*-coding:utf-8-*-
# Author    :wangk
# Data  :2020/11/1  12:6
# Software  :PyCharm
import  pytest

@pytest.fixture(scope='session',autouse=True)  #session级别:对包下的每一个测试文件
def  strt_demo(request):# 一个运行该包下，任何一个test文件，都会一开始执行操作
    print('---开始执行自动化测试----')

    #数据清除操作
    def fin():   #数据清除
        print('---自动测试 结束----')
    request.addfinalizer(fin)

#定制化初始化  不写autouse
#那么环境初始化，是否可以测试人员手动调用？  可以
@pytest.fixture(scope='function')  #不写  autouse，否则：下面的会自己跑
#留言回复初始化
def  repalyMsg_init():
    print('---我的作用是某一个 功能的 初始化---')
    #登录成功
    #列出留言
    #
