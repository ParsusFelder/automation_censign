import ast
import unittest
import urllib3

from common.configHttp import ConfigHttp
from common import Common as cm
import common.log
import logging.config

'''
Author: zhaoyongzhi
Date: 2020/03/29
Describe: 软件版本类型接口自动化用例
用例覆盖点：
1）test_sys_software_version:测试软件版本类型接口,ip,password均正确输入
2）test_sys_software_version:测试软件版本类型接口,ip有建无值，password正常
3）test_sys_software_version:测试软件版本类型接口,ip不通，password正常
4）test_sys_software_version:测试软件版本类型接口,ip正确，password密码错误
5）test_sys_software_version:测试软件版本类型接口,ip正确，password密码为空
'''
# 配置测试接口名称
case_name = "test_sys_software_version"
# 配置excel表格名称
xls_name = "testFile.xlsx"
# 配置sheet名称
sheet_name = "test_censign_key_normal"
# 开启日志
logging.config.dictConfig(common.log.LOGGING_DIC)
logger = logging.getLogger(__name__)
# 获取所有该接口测试用例
test_cases = cm.get_xls_cases(xls_name, sheet_name, case_name)
# 实例化ConfigHttp()类
ch = ConfigHttp()


class Test_sys_software_version(unittest.TestCase):

    def setUp(self):
        urllib3.disable_warnings()

    def tearDown(self):
        pass

    def test_sys_software_version_01(self):

        test_case = test_cases[0]
        logger.info(test_case[0])
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "password": test_case[5]
        }
        ch.set_url(url)
        ch.set_params(params)
        result = ch.get().json()
        try:
            self.assertEqual(result['status'], int(test_case[7]), test_case[0] + ":测试失败,status错误")
            self.assertEqual(result['data'], ast.literal_eval(test_case[8]), test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误!!!")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))

    def test_sys_software_version_02(self):

        test_case = test_cases[1]
        logger.info(test_case[0])
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "password": test_case[5]
        }
        ch.set_url(url)
        ch.set_params(params)
        result = ch.get().json()
        try:
            self.assertEqual(result['status'], int(test_case[7]), test_case[0] + ":测试失败,status错误")
            self.assertEqual(result['data'], ast.literal_eval(test_case[8]), test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))

    def test_sys_software_version_03(self):

        test_case = test_cases[2]
        logger.info(test_case[0])
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "password": test_case[5]
        }
        ch.set_url(url)
        ch.set_params(params)
        result = ch.get().json()
        try:
            self.assertEqual(result['status'], int(test_case[7]), test_case[0] + ":测试失败,status错误")
            self.assertEqual(result['data'], ast.literal_eval(test_case[8]), test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))

    def test_sys_software_version_04(self):

        test_case = test_cases[3]
        logger.info(test_case[0])
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "password": test_case[5]
        }
        ch.set_url(url)
        ch.set_params(params)
        result = ch.get().json()
        try:
            self.assertEqual(result['status'], int(test_case[7]), test_case[0] + ":测试失败,status错误")
            self.assertEqual(result['data'], ast.literal_eval(test_case[8]), test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))

    def test_sys_software_version_05(self):

        test_case = test_cases[4]
        logger.info(test_case[0])
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "password": test_case[5]
        }
        ch.set_url(url)
        ch.set_params(params)
        result = ch.get().json()
        try:
            self.assertEqual(result['status'], int(test_case[7]), test_case[0] + ":测试失败,status错误")
            self.assertEqual(result['data'], ast.literal_eval(test_case[8]), test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))

    def test_sys_software_version_06(self):

        test_case = test_cases[5]
        logger.info(test_case[0])
        url = test_case[2]
        params = {
            "password": test_case[5]
        }
        ch.set_url(url)
        ch.set_params(params)
        result = ch.get().json()
        try:
            self.assertEqual(result['status'], int(test_case[7]), test_case[0] + ":测试失败,status错误")
            self.assertEqual(result['data'], ast.literal_eval(test_case[8]), test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))

    def test_sys_software_version_07(self):

        test_case = test_cases[6]
        logger.info(test_case[0])
        url = test_case[2]
        params = {
            "ip": test_case[4]
        }
        ch.set_url(url)
        ch.set_params(params)
        result = ch.get().json()
        try:
            self.assertEqual(result['status'], int(test_case[7]), test_case[0] + ":测试失败,status错误")
            self.assertEqual(result['data'], ast.literal_eval(test_case[8]), test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))


if __name__ == "__main__":
    unittest.main()
