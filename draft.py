class MySuperClass(object):
    def __init__(self):
        print 'super'


class MySubClassBetter(MySuperClass):
    def __init__(self):
        super(MySubClassBetter, self).__init__()
        print 'sub'




x=MySuperClass()
y=MySubClassBetter()



