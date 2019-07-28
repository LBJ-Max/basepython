class MusicPlay(object):

    instance = None
    def __new__(cls, *args, **kwargs):

        # 1.判断类属性是否为空
        if cls.instance is None:

        # 2.如果没有被创建，调用父类的方法分配空间
            cls.instance = super().__new__(cls)
        return cls.instance


player1 = MusicPlay()
print(player1)
player2 = MusicPlay()
print(player2)