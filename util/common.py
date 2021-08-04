#coding:utf-8
class ConnonUtial:

    def is_contain(self,str_one,str_two):
        """判断一个字符串是否再另一个字符中，str_one,srr_two被查找的字符串"""
        flag=None
        if isinstance(str_one,str): #字符串分为str,unicode,二者均继承自basestring, isinstane("3.0版本"，str)
            str_one=str_one.encode('unicode-escape').decode('string_escape')
        if str_one in str_two:
            flag=True
        else:
            flag=False
        return flag


