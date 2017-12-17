# coding:utf-8
# yasin

'''
用于测试功能的模块
'''

import defalut_coroutine_mgr as Default


def default_func():
    ''' :Brief:
            用于测试默认协程的功能
    '''
    print "这是第一帧"
    yield Default.Default()
    print "这是第二帧"
    yield Default.Default()
    print "这是第三帧"
    yield Default.Default()


if __name__ == '__main__':
    D_C_M = Default.DefaultCoroutineMgr()
    D_C_M.append_coroutine(default_func())
    for item in xrange(5):
        D_C_M.update(0.1)
