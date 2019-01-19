import glob
import os
import zipfile

from day3_file import FileUtil
from day2_log.Log import ZLog


def zip_file(zippath, reportpath):
    f = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
    # zip file
    files = glob.glob(reportpath + '\*')
    for file in files:
        # 修改压缩文件的目录结构
        f.write(file, '/report/' + os.path.basename(file))
    f.close()


def get_log_path():
    """
    获取日志文件
    :param fileName:
    :return:
    """
    return ZLog.get_log().get_result_path()


if __name__ == "__main__":
    logger = ZLog.get_log().get_logger()
    logger.info("start")
    logger.error("error")
    logger.info("end")
    reportpath = get_log_path()
    zippath = os.path.join(FileUtil.getFileParentDir(__file__), "output", "test.zip")
    zip_file(zippath, reportpath)
