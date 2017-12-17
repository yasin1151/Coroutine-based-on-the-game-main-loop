# coding:utf-8
# yasin

'''
默认协程管理管理类
'''


class DefaultCoroutineMgr(object):
    ''' Brief : 默认的协程管理对象，
                加入该对象的管理中后

                会在每一帧执行一次`next()`方法
        Attribute : :attr: m_coroutine_list : 用于管理协程对象

        :attr: m_remove_list : 用于管理移除的对象

        :attr: m_change_list : 用于管理需要切换的对象
    '''
    def __init__(self):
        ''' Brief : 初始化一些变量
        '''
        self.m_coroutine_list = []
        self.m_remove_list = []
        self.m_change_list = []

    def update(self, delta_time):
        ''' Brief : 用于每一帧的更新
            Args : delta_time : 每一帧的间隔时间
        '''
        cor_obj = None
        for item in self.m_coroutine_list:
            try:
                cor_obj = item.next()
            except StopIteration as except_info:
                print except_info
                print "该协程对象已经运行完毕，将加入移除队列中"
                self.m_remove_list.append(item)
                continue

            # 判断协程是否需要切换
            if not isinstance(cor_obj, Default):
                self.m_change_list.append(cor_obj)

        self.do_remove()
        self.do_change()

    def append_coroutine(self, generator_obj):
        ''' Brief : 用于添加协程对象
            Args : :param: generator_obj : 生成器对象
            Return : 返回是否添加进了该对象，不会重复添加
        '''
        cor_obj = None

        # 添加进来时先执行一次
        try:
            cor_obj = generator_obj.next()
        except StopIteration as except_info:
            print except_info
            print "该协程对象已经运行完毕，无法加入默认协程管理器中"
            return False

        # 是否是默认协程对象
        if not isinstance(cor_obj, Default):
            return False
        # 是否被重复添加
        if generator_obj in self.m_coroutine_list:
            return False

        self.m_coroutine_list.append(generator_obj)

        return True

    def do_remove(self):
        ''' Brief : 用于处理需要移除的对象
        '''
        for item in self.m_remove_list:
            self.m_coroutine_list.remove(item)

        # 清理对象
        if self.m_remove_list.__len__() > 0:
            self.m_remove_list = []

    def do_change(self):
        ''' Brief : 用于处理需要切换的对象
        '''
        for item in self.m_change_list:
            self.m_coroutine_list.remove(item)
            # todo ..abs
            # 暂时先移除

        # 清理对象
        if self.m_change_list.__len__() > 0:
            self.m_change_list = []


class Default(object):
    ''' Brief : 用于在yield时返回的对象，
        如果返回该对象，会在下一帧继续执行
    '''
