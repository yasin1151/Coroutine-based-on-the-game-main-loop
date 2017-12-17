# coding:utf-8
# yasin

'''
协程管理类
'''


class CoroutineMgr(object):
    ''' Brief :
            用于管理协程和协程的切换的类

        Attributes :
            m_Name hello
    '''
    def start_coroutine(self, generator_obj):
        ''' Brief :
                传入一个生成器对象，会将该生成器加入协程管理中，
                根据每一次运行.next()方法返回的对象，
                会加入到不同行为的管理器中,
                在不同的时机调用

            Args :
                oGenerator : 生成器对象

            Return :
                None
        '''
        pass

    def remove_all_coroutine(self):
        ''' Brief :
                移除所有的协程对象

            Return :
                是否有东西被移除
                    如果有则返回True，无则返回None
        '''
        pass
