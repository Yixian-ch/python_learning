import class_start
a = 5
b = "5"
reader = class_start.Readrss("../rss","re")
print(type(reader),type(a))
# print(type(reader.path))
print(reader.help)
reader.help = "hello world"
print(reader.help)
b = class_start.Readrss("../rss","re")
print(b.help)

# here self is a normal argument that behaves like any other argument, so the self is a special argument only used in instance methods
def hello(self):
    print("hello")

a = hello("hi")
print(a.help)

