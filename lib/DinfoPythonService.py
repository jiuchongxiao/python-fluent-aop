# -*- coding: utf-8 -*-
# @Time    : 2017-11-14 15:03:12
# @Author  : lzg
# @File    : DinfoPythonService.py
# @Desc    : 自定义算法或训练模型时需要继承该抽象类
from abc import ABCMeta, abstractmethod


class BaseCom:
    __metaclass__ = ABCMeta

    # 组件执行主方法
    # param input 输入的dataset
    # param paramMap 参数列表
    # return 组件返回的结果，内有返回的dataset，根据具体组件不同，可能含有其他的辅助信息
    @abstractmethod
    def sparkExecute(self, inputData, paramMap):
        pass