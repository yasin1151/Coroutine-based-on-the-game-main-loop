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


class Default(object):
    ''' Brief : 用于在yield时返回的对象，
        如果返回该对象，会在下一帧继续执行
    '''


class WaitTime(object):
    ''' Brief : 用于在yield时返回的对象，
        如果返回该对象，会在等待时间过后执行
        Attribute : :attr: m_wait_time : 等待的时间
    '''
    def __init__(self, wait_time):
        self.m_wait_time = wait_time

    def get_wait_time(self):
        ''' Brief : 获取剩余的等待时间
        '''
        return self.m_wait_time

    def add_time(self, time):
        ''' Brief : 增加或减少时间
        '''
        self.m_wait_time += time
