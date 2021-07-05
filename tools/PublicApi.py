#!/usr/bin/python
# -*- coding=utf-8 -*-
# author : Lenovo
# date: 2021/6/17 16:07
# version: 0.1
import time
import math
import abc

import requests

from tools.logger import Loggings
logger = Loggings()

class calculation():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        result =  self.a + self.b
        logger.info("加法的最终结果是:{}".format(result))
        return result
    def subtraction(self):
        result = self.a - self.b
        logger.info("减法法的最终结果是：{}".format(result) )
        return result
    def multiplication(self):
        result = self.a * self.b
        logger.info("乘法的最终结果是：{}".format(result))
        return result

class A(calculation):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add_and_subtra(self):
        result = super(A, self).addition() + super(A, self).subtraction()
        logger.info('加减运算为：{}'.format(result))
        return result

class B(calculation):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add_and_subtra_mult(self):
        rusult = super(B, self).addition() + super(B, self).subtraction() +super(B, self).multiplication()
        logger.info('加减乘除运算：{}'.format(rusult))
        return rusult

class C(B,A):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def finallysult(self):
        result = super(C, self).add_and_subtra_mult() + super(C, self).add_and_subtra()
        logger.info('最终运算结果：{}'.format(result))
        return result

class room:
    def __init__(self,name,owner,width,length,high):
        '''
        :param name:
        :param owner:
        :param width: 私有属性，对外封闭，类的内部使用
        :param length:
        :param high:
        '''
        self.name = name
        self.owner = owner
        self.__width = width
        self.__length = length
        self.__high  = high
    def tell_area(self):
        values =  self.__width * self.__length * self.__high
        logger.info(values)
        return values

#staticmethod 静态方法的使用
class InputMsg:
    @staticmethod
    def msg(x,y,z):
        logger.info('输出数据为：{},{},{}'.format(x,y,z))

    # msg = staticmethod(msg)

class Dete:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @staticmethod
    def now():
        t = time.localtime()
        return Dete(t.tm_year,t.tm_mon,t.tm_mday)
    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return  Dete(t.tm_year,t.tm_mon,t.tm_mday)


class Cicle:
    def __init__(self,radius):
        self.radius = radius
    @property
    def area(self):
        result  = self.radius **2 * math.pi
        return result
    @property
    def perimeter(self):
        result = self.radius * 2 * math.pi
        return result

#抽象类
class FileFunc(metaclass=abc.ABCMeta):
    type = 'file'
    @abc.abstractmethod
    def reading(self):
        logger.info('--')
    @abc.abstractmethod
    def write(self):
        pass


class txt(FileFunc):
    def reading(self):
        logger.info('数据读取功能')
    def write(self):
        logger.info('数据写入功能')

class dictory(FileFunc):
    def reading(self):
        logger.info('调用reading 方法')
    def write(self):
        logger.info('调用write 方法')

class PublicData:
    token = ''
    session = requests.Session()
    def InputMag(self):
        logger.info(session)
# 反射斯大将军setattr():gei类的属性赋值，getattr() 获取类属性的值 hasattr()判断给类属性是否存在该值delattr()删除该属性的值

class DirGet:
    def __init__(self,name,age,idcard,accNo,accName):
        self.name = name
        self.age = age
        self.idCard = idcard
        self.accNo = accNo
        self.accNmme =accName

    def __getitem__(self, item):
        return  self.__dict__.get(item)
    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __delitem__(self,name,age,idcard,accNo,accName):
        '''
        改方法目前应该只支持dic 为一个值得数据
         del runnn['age','idCard','accNo','accNmme'] --调用
        :param name:
        :param age:
        :param idcard:
        :param accNo:
        :param accName:
        :return:
        '''
        del self.__dict__[name,age,idcard,accNo,accName]

class demo:
    pass
    def __call__(self, *args, **kwargs):
        print(self)
        print(args)
        print(kwargs)
#元素
# a = {"name":"testing","age":12}
# b = {}
# exec('''
# global x,z
# x=100
# z=200
# m=300''',a,b)
#
# result = ascii(a)
# logger.info(result)

NowTime = time.strftime('%Y-%m-%d %X',time.localtime())
logger.info(NowTime)
# if __name__ =='__main__':
#     # runnn = DirGet('test',32,'62242419920106818','6230200220110756','测试中心')
#     # runnn()
#     # logger.info(runnn.__dict__)
#     test = demo()
#     test('noah','luo',age=1,sex=2)
    # del runnn['age','idCard','accNo','accNmme']

    # logger.info(runnn.__str__())
    # logger.info(runnn.__setattr__('idCard','修改身份证号'))
    # logger.info(runnn.__dict__)
    # token = PublicData().session
    # setattr(PublicData,token,'test')
