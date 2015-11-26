__metaclass__=type
class Myclass:
    @staticmethod
    def smeth(name):
        print 'This is a static method',name
    @classmethod
    def classmethod(cls):
        print 'This is a class method of',cls
Myclass.smeth('smeth')
Myclass.classmethod()