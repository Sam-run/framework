#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 获取根路径
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("autotest") + len("autotest")]
# 将根目录加入path
sys.path.append(rootPath)

from common.venv.var import *
from common.data_operation.mysql_db import OperateMDdb
from common.venv.api_path_mb import *
from common.base_utils.comm_utils import *
import pytest, allure
import warnings

# 去除警告信息
warnings.filterwarnings('ignore')

class TestWeekInput:

    def setup_class(self):
        # 创建配置实例
        self.cf = Config()
        self.db = OperateMDdb()
        self.name_global = create_name()
        self.idnum_global = create_IDCard()
        self.mobile_global = create_phone()

    def setup_method(self):
        # 定义每个用例变量
        self.name = create_name()
        self.idnum = create_IDCard()
        self.mobile = create_phone()



if __name__ == '__main__':
    week = TestWeekInput()
