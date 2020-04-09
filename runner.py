import unittest
import os
import readConfig

class runner:
    def set_case_list(self):
        self.case_file = os.path.join(readConfig.proDir, "caseList.txt") #获取测试用例列表路径
        fb = open(self.case_file)
        self.caseList = []
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()
        return self.caseList
# 执行测试用例
    def run(self):
        caseList = self.set_case_list()
        runner = unittest.TextTestRunner()
        test_suite = unittest.TestSuite()
        for test_case in caseList:
            discover = unittest.defaultTestLoader.discover("./case", pattern=test_case + '.py')
            runner.run(discover)
        return test_suite

if __name__ == '__main__':
    s = runner()
    s.run()
