import os
import logging
import datetime
import time
from functools import wraps


"""
如何使用logger.py 
1. 在函數中自訂logger.info等資訊
python檔案中引入logger.py檔案；
$ from revise.util.logger import create_logger
再來在程式中添加；
$ logger = create_logger()
會建立logger物件，可以透過該物件寫log
$ logger.info("測試寫入log")
會建立logs資料夾並建立一個log檔案，其命名格式為  %Y-%m-%d_test.log

2. 使用裝飾器對輸入和輸出紀錄log
python檔案中引入logger.py檔案；
$ from revise.util.logger import log_filter
再來在def函數上方添加@log_filter (裝飾器)
$ @log_filter
$ def test(a):
$    ...
會將輸入和輸出的變數記錄到log中
"""


def _log_setting(logger):
    """
    logger基本設定
    """
    # 設定logger基本層級
    logger.setLevel('DEBUG')
    # 設定日誌格式
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    consoleHandler = logging.StreamHandler()  # 輸出到控制台的handler
    consoleHandler.setLevel(logging.DEBUG)  # 設定層級(控制台)
    consoleHandler.setFormatter(formatter)  # 設定日誌格式

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    fileHandler = logging.FileHandler(f"./logs/OneDayOneColor.log", 'a', 'utf-8')  # 輸出到.log的handler
    fileHandler.setLevel(logging.DEBUG)  # 設定層級(.log)
    fileHandler.setFormatter(formatter)  # 設定日誌格式

    # 日誌紀錄器增加此handler
    # 若handler為空，才會添加logger.handlers，避免添加一堆handler重複輸出log
    if not logger.handlers:
        logger.addHandler(consoleHandler)
        logger.addHandler(fileHandler)
    return logger


def create_logger(log_name=__name__):
    """
    建立logger設定
    :return:
    """
    if not os.path.exists("./logs"):  # 若logs不存在，建立該資料夾
        os.makedirs("./logs")
    # logging.captureWarnings(True)  # 捕捉 py waring message
    logger = logging.getLogger(log_name)  # 設定logging名稱，可以自己改成要用的名稱
    logger = _log_setting(logger)
    return logger


def log_filter(func):
    """
    日誌裝飾器，簡單記錄函數的日誌
    :param func: 函数
    :return:
    """
    if not os.path.exists("./logs"):  # 若logs不存在，建立該資料夾
        os.makedirs("./logs")
    # 獲得log日誌紀錄器，設定日誌等級
    logger = logging.getLogger(__name__)
    logger = _log_setting(logger)

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            logger.debug(f"func: {func.__name__} - input: {args, kwargs} -> output: {res}")
            return res
        except Exception as e:
            logger.error(f"func: {func.__name__} - error message: {e}", exc_info=True)
    return inner


def log_filter_error(func):
    """
    日誌裝飾器，簡單記錄函數的日誌，僅在執行錯誤時會記錄log
    :param func: 函数
    :return:
    """
    if not os.path.exists("./logs"):  # 若logs不存在，建立該資料夾
        os.makedirs("./logs")
    # 獲得log日誌紀錄器，設定日誌等級
    logger = logging.getLogger(__name__)
    logger = _log_setting(logger)

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)  # 無異常就直接return
        except Exception as e:  # 異常才紀錄
            logger.error(f"func: {func.__name__} - error message: {e}", exc_info=True)
    return wrapper


def log_filter_around(func):
    """
    日誌裝飾器，簡單記錄函數的日誌
    執行成功會記錄輸入與輸出的變數、執行錯誤時會記錄log、最終結束會記錄時間
    :param func: 函数
    :return:
    """
    if not os.path.exists("./logs"):  # 若logs不存在，建立該資料夾
        os.makedirs("./logs")
    # 獲得log日誌紀錄器，設定日誌等級
    logger = logging.getLogger(__name__)
    logger = _log_setting(logger)

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            res = func(*args, **kwargs)
            logger.debug(f"func: {func.__name__} - input: {args, kwargs} -> output: {res}")
            return res
        except Exception as e:
            logger.error(f"func: {func.__name__} - error message: {e}", exc_info=True)
        finally:
            logger.debug(f"func: {func.__name__} - time: {round(time.time() - start_time, 2)} sec.")

    return wrapper


# 以下為測試用的函數
@log_filter
def test_plus_normal(a, b):
    print(a)
    return a + b


@log_filter_around
def test_plus_error(a, b):
    print(a)
    error  # 不存在的變數，刻意錯誤
    return a + b


if __name__ == "__main__":
    test_plus_normal(1, 2)
    test_plus_error(1, 2)
