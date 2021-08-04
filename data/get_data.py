#coding:utf-8
import os
from util.operation_json import OperetionJson
from util.operation_execl import OperationExecl
from data.data_config import global_var


class GetData:
    def __init__(self):
        self.opera_execl=OperationExecl()
        self.da=global_var()

    def get_case_lines(self):
        return self.opera_execl.get_lines()
    def is_run(self,row):
        flag=None
        col=int(self.da.get_run(self))
        run_model=self.opera_execl.get_cell_value(row,col)
        if run_model=="yes":
            flag=True
        else:
            flag=False
    def is_header(self,row):
        col=int(self.da.get_header(self))
        header=self.opera_execl.get_cell_value(row,col)
        if header=="yse":
            return 'header'
        else:
            return None
    def get_request_method(self,row):
        col=int(self.da.get_run_way(self))
        request_method=self.opera_execl.get_cell_value(row,col)
        return request_method
    def get_requset_url(self,row):
        col=self.da.url
        print(row, col)
        url=self.opera_execl.get_cell_value(row,col)
        print(url)
        return url
    def get_request_data(self,row):
        col=int(self.da.get_data(self))
        data=self.opera_execl.get_cell_value(row,col)
        if data=='':
            return None
        else:
            return  data
    def get_for_jsondata(self,row):
        oper_json=OperetionJson()
        request_data=oper_json.get_data(self.get_request_data(row))
        return request_data
    def get_request_execpt(self,row):
        col=int(self.da.get_expect())
        exepct=self.opera_execl.get_cell_value(row,col)
        return exepct
    def write_result(self,row,value):
        col=int(self.da.get_result(self))
        self.opera_execl.write_value(row,col,value)

if __name__ == '__main__':
    g=GetData()
    print(g.get_requset_url(2))



