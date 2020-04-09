import os
from xlrd import open_workbook
from common.configHttp import ConfigHttp
from readConfig import proDir
import logging.config
import common.log

loacalConfigHttp = ConfigHttp()
logging.config.dictConfig(common.log.LOGGING_DIC)
logger = logging.getLogger(__name__)
# 从 excel文件中读取测试用例,获取所有用例
def get_xls(xls_name, sheet_name):
    cls = []
    # get xls file's path
    xlsPath = os.path.join(proDir, "testFile", xls_name)
    # open xls file
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls


# 根据指定用例名称，从 excel文件中读取测试用例
def get_xls_cases(xls_name, sheet_name, case_name):
    # 读取excel，获得测试case
    test_cases = get_xls(xls_name, sheet_name)
    cls = []
    # 遍历所有case
    for i in range(len(test_cases)):
        test_case = test_cases[i]
        strs = test_case[0].split(":")
        if case_name.__eq__(strs[0]):
            cls.append(test_case)
    return cls


if __name__ == '__main__':
    a = get_xls_cases("testFile.xlsx", "test_censign_key_normal", "test_sys_software_version")
    print(a)
