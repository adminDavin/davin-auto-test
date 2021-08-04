#coding:utf_8
from util.operation_execl import OperationExecl
from method.run_method import Runmethod
class DependdentData:
    def __init__(self,case_id):
        self.case_id=case_id
        self.oper_execl=OperationExecl()

    #通过case_id获取该case_id的整行数据
    def get_case_lines(self):
        rows_data=self.oper_execl.get_row_data(self.case_id)
        return rows_data
    #执行依赖测试，获取结果
    def run_dependent(self):
        run_method=Runmethod()
