import ast
import unittest
import urllib3

from common.configHttp import ConfigHttp
from common import Common as cm
import logging.config
import common.log
import time
'''
Author: zhaoyongzhi
Date: 2020/04/03
Describe: 服务的基本状态
'''
# 配置测试接口名称
case_name = "test_service_basic_status"
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


class Test_service_basic_status(unittest.TestCase):

    def setUp(self):
        urllib3.disable_warnings()

    def tearDown(self):
        time.sleep(1.5)
        pass

    def test_service_basic_status_01(self):
        test_case = test_cases[0]
        logger.info(test_case[0])
        # 设置访问url、传递参数
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "password": test_case[5],
            "service": test_case[6]
        }
        ch.set_url(url)
        ch.set_params(params)
        result = ch.get().json()
        try:
            self.assertEqual(result['status'], int(test_case[7]), test_case[0] + ":测试失败,status错误")
            self.assertEqual(result['data']['ip'], test_case[4], test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['stat'], True, test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))

    def test_service_basic_status_02(self):
        test_case = test_cases[1]
        logger.info(test_case[0])
        # 设置访问url、传递参数
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "password": test_case[5],
            "service": test_case[6]
        }
        ch.set_url(url)
        ch.set_params(params)
        result = ch.get().json()
        try:
            self.assertEqual(result['status'], int(test_case[7]), test_case[0] + ":测试失败,status错误")
            self.assertEqual(result['data']['ip'], '', test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['stat'], False, test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['infos'], None, test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['msg'],
                             'get performanceInfo by SNMP failed: Please check if you can communicate !',
                             test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))

    def test_service_basic_status_03(self):
        test_case = test_cases[2]
        logger.info(test_case[0])
        # 设置访问url、传递参数
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "password": test_case[5],
            "service": test_case[6]
        }
        ch.set_url(url)
        ch.set_params(params)
        result = ch.get().json()
        try:
            self.assertEqual(result['status'], int(test_case[7]), test_case[0] + ":测试失败,status错误")
            self.assertEqual(result['data']['ip'], test_case[4], test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['stat'], False, test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['infos'], None, test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['msg'], 'get performanceInfo by SNMP failed:Request timed out.',
                             test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))

    def test_service_basic_status_04(self):
        test_case = test_cases[3]
        logger.info(test_case[0])
        # 设置访问url、传递参数
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "password": test_case[5],
            "service": test_case[6]
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

    def test_service_basic_status_05(self):
        test_case = test_cases[4]
        logger.info(test_case[0])
        # 设置访问url、传递参数
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "password": test_case[5],
            "service": test_case[6]
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

    def test_service_basic_status_06(self):
        test_case = test_cases[5]
        logger.info(test_case[0])
        # 设置访问url、传递参数
        url = test_case[2]
        params = {
            "password": test_case[5],
            "service": test_case[6]
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

    def test_service_basic_status_07(self):
        test_case = test_cases[6]
        logger.info(test_case[0])
        # 设置访问url、传递参数
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "service": test_case[6]
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

    def test_service_basic_status_08(self):
        test_case = test_cases[7]
        logger.info(test_case[0])
        # 设置访问url、传递参数
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "password": test_case[5],
            "service": test_case[6]
        }
        ch.set_url(url)
        ch.set_params(params)
        result = ch.get().json()
        try:
            self.assertEqual(result['status'], int(test_case[7]), test_case[0] + ":测试失败,status错误")
            self.assertEqual(result['data']['ip'], test_case[4], test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['infos'], None, test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['stat'], False, test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['msg'],
                             'can not found any data,Please check if a service exists or check netsign',
                             test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))

    def test_service_basic_status_09(self):
        test_case = test_cases[8]
        logger.info(test_case[0])
        # 设置访问url、传递参数
        url = test_case[2]
        params = {
            "ip": test_case[4],
            "password": test_case[5],
            "service": test_case[6]
        }
        ch.set_url(url)
        ch.set_params(params)
        result = ch.get().json()
        try:
            self.assertEqual(result['status'], int(test_case[7]), test_case[0] + ":测试失败,status错误")
            self.assertEqual(result['data']['ip'], test_case[4], test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['infos'], None, test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['stat'], False, test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['data']['msg'],
                             'can not found any data,Please check if a service exists or check netsign',
                             test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))

    def test_service_basic_status_10(self):
        test_case = test_cases[9]
        logger.info(test_case[0])
        # 设置访问url、传递参数
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
            self.assertEqual(result['data']['ip'], test_case[4], test_case[0] + ":测试失败,data错误")
            self.assertNotEqual(result['data']['infos'], None, test_case[0] + ":测试失败,data错误")
            self.assertEqual(result['operation'], test_case[9], test_case[0] + ":测试失败,operation错误")
            self.assertEqual(result['msg'], test_case[10], test_case[0] + ":测试失败,msg错误")
        except Exception as ex:
            logger.error(str(ex) + "\n实际返回内容：" + str(result))

if __name__ == "__main__":
    unittest.main()
    # test_suit= unittest.TestSuite()
    # # test_suit.addTest(Test_service_basic_status('test_service_basic_status_08'))
    # # test_suit.addTest(Test_service_basic_status('test_service_basic_status_09'))
    # # test_suit.addTest(Test_service_basic_status('test_service_basic_status_10'))
    # runner = unittest.TextTestRunner
    # runner.run(test_suit)