class MusicPlayer(object):

    def __init__(self):
        print("播放器开机")

    # *args 表示多值的元组  ； **kwargs:多值的字典参数
    def __new__(cls, *args, **kwargs):
        # 创建对象时候new方法被自动调用
        print("new 方法被调用")

        # 为对象分配空间
        instance = super().__new__(cls)

        #返回对象引用
        return instance



player = MusicPlayer()
print(player)