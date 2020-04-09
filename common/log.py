import os
import logging.config
import readConfig

# 定义三种日志输出格式 开始

# 标准版 格式
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
# 简单版 格式
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

# boss版格式（lowb版）
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

proDir = readConfig.proDir
resultPath = os.path.join(proDir, "result")
# create result file if it doesn't exist
if not os.path.exists(resultPath):
   os.mkdir(resultPath)

# file_path = os.path.dirname(__file__)

logfile_name = resultPath + '\output.log'  # log文件名

# log配置字典

LOGGING_DIC = {
    'version': 1,  # 版本
    'disable_existing_loggers': False,  # 可否重复使用之前的logger对象
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'boss_formatter': {
            'format': id_simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'stream': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志  文件句柄
        'file': {
            'level': 20,
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'boss_formatter',  # 标准
            'filename': logfile_name,  # 日志文件
            'maxBytes': 30000000,  # 日志大小 300 bit
            'backupCount': 5,  #轮转文件数
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['stream', 'file'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'INFO',  # 总级别
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}
# 字典中第一层的所有key都是固定不可变的。

# logging.config.dictConfig(LOGGING_DIC)
# logger = logging.getLogger()  # 这个logger对象是通过自己个性化配置的logger对象



def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    logger.info('It works!')  # 记录该文件的运行状态
###　　  settings.LOGGING_DIC['handlers']['file']['filename'] = 路径地址   # 通过操作字典 可实现动态设置log文件的存储路径，和文件名
if __name__ == '__main__':
    load_my_logging_cfg()