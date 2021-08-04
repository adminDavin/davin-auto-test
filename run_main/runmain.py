from method.run_method import Runmethod
from data.get_data import GetData
from util.common import ConnonUtial
class RunTest:
    def __init__(self):
        self.runme=Runmethod()
        self.data=GetData()
        self.com_util=ConnonUtial()
    def go_on_run(self):
        res=None
        row_count=self.data.get_case_lines()
        for i in range(1,row_count):
            url=self.data.get_requset_url(i)
            method=self.data.get_request_method(i)
            is_run=self.data.is_run(i)
            data=self.data.get_for_jsondata(i)
            expect=self.data.get_request_execpt(i)
            header=self.data.is_header(i)
            if is_run:
                res=self.runme.run_main(method,url,data,header)
                if self.com_util.is_contain(expect,res):
                    self.data.write_result(i,"测试通过")
                else:
                    self.data.write_result(i,"测试失败")
if __name__ == '__main__':
    run=RunTest()
    run.go_on_run()

