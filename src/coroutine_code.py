# coding:utf-8
# yasin

'''
用于标识协程对象的枚举
'''


class CoroutineCode(object):
    ''' Brief :
            用于标识枚举对象的类型
        Attribute :
            default : 默认的协程，每一帧执行
            wait_time : 在一定时间后在执行的协程
    '''

    default = 1
    wait_time = 2
