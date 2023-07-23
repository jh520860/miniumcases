import logging
import os
from logging import Logger, handlers




class MyLogger(Logger):

    def __init__(self):
        # log_name = '{}.log'.format(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
        # log_path_file = os.path.join(get_log_path(), log_name)

        # 获取日志文件路径
        all_log_path_file = os.path.join("E://logs", "api_test.log")
        error_log_path_file = os.path.join("E://logs", "error.log")

        # 设置日志的名字、日志的收集级别
        super().__init__("test_api", logging.DEBUG)

        # 自定义日志格式(Formatter), 实例化一个日志格式类
        fmt_str = '%(asctime)s  %(levelname)s  %(filename)s : %(funcName)s  [line: %(lineno)s]  %(message)s'
        formatter = logging.Formatter(fmt_str)
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 实例化控制台渠道(StreamHandle)
        sh = logging.StreamHandler()
        # 设置控制台输出的日志级别
        sh.setLevel(logging.ERROR)
        # 设置渠道当中的日志显示格式
        sh.setFormatter(formatter)
        # 将渠道与日志收集器绑定起来
        self.addHandler(sh)

        # 实例化文件渠道(FileHandle)
        # fh = logging.FileHandler(log_path_file, mode='a', encoding="utf-8")
        '''
        创建一个文件实例，如果 api_test.log 文件不存在，就会自动创建；
        mode 参数设置为追加；另外为防止乱码， encoding 参数设置为 utf-8 编码格式
        '''
        fh = handlers.RotatingFileHandler(all_log_path_file, maxBytes=10**6, backupCount=5,
                                          encoding="utf-8", mode="a")
        # 设置向文件输出的日志格式
        fh.setLevel(logging.DEBUG)
        # 设置渠道当中的日志显示格式
        fh.setFormatter(formatter)
        # 加载文件实例到 logger 对象中
        self.addHandler(fh)
        # 当log达到最大字节长度，将自动backup5个log文件。当5个log文件都达到最大长度时，将只保留最新的log。
        fh1 = handlers.RotatingFileHandler(error_log_path_file, maxBytes=10 ** 6, backupCount=5,
                                           encoding="utf-8", mode="a")
        # 设置向文件输出的日志格式
        fh1.setLevel(logging.ERROR)
        # 设置渠道当中的日志显示格式
        fh1.setFormatter(formatter)
        # 加载文件实例到 logger 对象中
        self.addHandler(fh1)

        fh.close()
        fh1.close()
        sh.close()


# 实例化MyLogger对象，在其他文件直接使用log就能调用
log = MyLogger()


if __name__ == '__main__':
    log.error("this is a error log")
    log.info("this is a info log")

