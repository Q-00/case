import xlrd
from xlutils.copy import copy

class ExcelFile:
    def __init__(self,url, table_index=0):
        # excel_file = "C:/Users/Qing/Desktop/test.xls"
        excel_file = url
        excel = xlrd.open_workbook(excel_file)
        self.excelFile = excel_file
        self.table = excel.sheets()[table_index]

    def ReadData(self, row, col):
        return self.table.cell_value(row, col)

    def writeResult(self,row,col,value):
        file = xlrd.open_workbook(self.excelFile)
        write_data = copy(file)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)

        write_data.save(self.excelFile)