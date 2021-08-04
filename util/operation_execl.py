import xlrd
from xlutils.copy  import copy
class OperationExecl:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name=file_name
            self.sheet_id=sheet_id

        else:
            self.file_name= "../resquest.xls"
            self.sheet_id=0
        self.data=self.get_data()
    def get_data(self):
        data=xlrd.open_workbook(self.file_name)
        tables=data.sheets()[self.sheet_id]
        return tables
    def get_lines(self):
        return self.data.nrows
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)
    def write_value(self,row,col,value):
        read_date=xlrd.open_workbook(self.file_name)
        write_data=copy(read_date)
        sheet_data=write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)
        #根据对应的case_id找到对应行的内容
    def get_row_data(self,case_id):
        row_num=self.get_row_num(case_id)
        rows_data=self.get_row_values(row_num)
        return rows_datat
              #根据对应的case_id找到应号
    def get_row_num(self,case_id):
        num=0
        clols_data=self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return  num
            num=num+1
        pass
    #根据行号，找到该行的内容
    def get_row_values(self,row):
        tables=self.data
        row_data=tables.row_values(row)
        return row_data
    #获取某一行的内容
    def get_cols_data(self,col_id=None):
        if col_id!=None:
            cols=self.data.col_values(col_id)
        else:
            cols=self.data.col_values(0)
        return cols


if __name__ == '__main__':

    operat=OperationExecl()
    print(operat.get_lines())

