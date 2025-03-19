# 类也是python中的一个对象，类所含有的东西被分为：类属性，实例属性，类方法，实例方法
# 实例：在类的基础上生成的对象，指向类。共享类的属性，下面代码中help和show就是类属性，会被所有的实例共享
class Greeting():
    
    def say_hello():
        print("hello world")


chatbot = Greeting()















# from dataclasses import dataclass

# @dataclass
# class rss_reader:
#     method : str # = vs : different behavior of class attributes and instance attributes
#     path : str
#     class_attribute = "hi"

# my_rss = rss_reader(method=3,path=4)
# print(type(my_rss.method),rss_reader.class_attribute)
