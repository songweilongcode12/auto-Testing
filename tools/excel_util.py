# coding=utf-8

from tools.logger import Loggings
logger = Loggings()
import xlrd

# coding=utf-8
import xdrlib, sys
from loguru import logger
import xlrd


class excel_util(object):
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # get titles
        self.row = self.table.row_values(0)
        # get rows number
        self.rowNum = self.table.nrows
        # get columns number
        self.colNum = self.table.ncols
        # the current column
        self.curRowNo = 1

    def next(self):
        '''
         获取下一行
        :return:
        '''
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            if col[0] == '总':
                break
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1

        return r

    def hasNext(self):
        '''
         判断是否还有行数
        :return:
        '''
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

    def open_excel(self, file='file.xls'):
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception as e:
            print(str(e))

    def get_table_byindex(self, file='file.xls', colnameindex=0, by_index=0):
        '''
        根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
        :param file:
        :param colnameindex:
        :param by_index:
        :return:
        '''
        data = self.open_excel(file)
        table = data.sheets()[by_index]
        nrows = table.nrows  # 行数
        ncols = table.ncols  # 列数
        colnames = table.row_values(colnameindex)  # 某一行数据
        logger.error(colnames)
        list = []
        for rownum in range(1, nrows):
            row = table.row_values(rownum)
            logger.error(row)
            if row:
                app = {}
                for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                list.append(app)
        return list

    def get_table_byname(self, file='file.xls', colnameindex=0, by_name=u'Sheet1'):
        '''
        #根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
        :param file:
        :param colnameindex:
        :param by_name:
        :return:
        '''
        data = self.open_excel(file)
        table = data.sheet_by_name(by_name)
        nrows = table.nrows  # 行数
        colnames = table.row_values(colnameindex)  # 某一行数据
        cell = table.cell(0, 0)
        if cell.ctype == 2 and cell.value % 1 == 0:
            colnames = int(cell.value)
        if colnames == int:
            colnames = int(table.row_values(colnameindex))
        list = []
        for rownum in range(1, nrows):
            row = table.row_values(rownum)
            if row:
                app = {}
                for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                list.append(app)
        return list

    def get_rows_count_by_sheet_index(self, file='file.xls', sheetindex=0):
        data = self.open_excel(file)
        sheet = data.sheet_by_index(sheetindex)
        return sheet.nrows

    def get_cols_count_by_sheet_index(self, file='file.xls', sheetindex=0):
        data = self.open_excel(file)
        sheet = data.sheet_by_index(sheetindex)
        return sheet.ncols

    def get_cell_by_col_row(self, file='file.xls', colindex=0, rowsindex=0, sheetindex=0):
        data = self.open_excel(file)
        sheet = data.sheet_by_index(sheetindex)
        rows = sheet.row_values(rowsindex)
        cell_value = sheet.cell(rowsindex, colindex).value.encode('utf-8')
        print(cell_value.ctype)
        if cell_value.ctype == 2 and cell_value.value % 1 == 0:
            cell_value = str(int(cell_value.value))
        return cell_value
    # def get_sheelName_all(self):
    #     sheetName =self.data.sheet_names()
    #     for i in sheetName:
    #         return sheetName


# coding=utf-8
import xlrd
import traceback
from datetime import datetime
from xlrd import xldate_as_tuple


class excelHandle:
    def decode(self, filename, sheetname):
        try:
            filename = filename.decode('utf-8')
            sheetname = sheetname.decode('utf-8')
        except Exception:
            print(traceback.print_exc())
        return filename, sheetname

    def read_excel(self, filename, sheetname):
        filename, sheetname = self.decode(filename, sheetname)
        rbook = xlrd.open_workbook(filename)
        sheet = rbook.sheet_by_name(sheetname)
        rows = sheet.nrows
        cols = sheet.ncols
        all_content = []
        for i in range(rows):
            row_content = []
            for j in range(cols):
                ctype = sheet.cell(i, j).ctype  # 表格的数据类型
                cell = sheet.cell_value(i, j)
                if ctype == 2 and cell % 1 == 0:  # 如果是整形
                    cell = int(cell)
                elif ctype == 3:
                    # 转成datetime对象
                    date = datetime(*xldate_as_tuple(cell, 0))
                    cell = date.strftime('%Y/%d/%m %H:%M:%S')
                elif ctype == 4:
                    cell = True if cell == 1 else False
                row_content.append(cell)
            all_content.append(row_content)
            print('[' + ','.join("'" + str(element) + "'" for element in row_content) + ']')
        return all_content


