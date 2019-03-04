import os

global proDir


def getFileParentDir(filepath):
    """
    获取文件的上一级文件夹
    :param filepath:
    :return:
    """
    dirname = os.path.dirname(filepath)
    pardir = os.path.pardir
    return os.path.abspath(os.path.join(dirname, pardir))


def createFile(proDir, fileName):
    """
    创建文件
    :param fileName:
    :return:
    """
    resultPath = os.path.join(proDir, fileName)
    print(resultPath)
    if not os.path.exists(resultPath):
        os.mkdir(resultPath)


proDir = getFileParentDir(__file__)

if __name__ == "__main__":
    proDir = getFileParentDir(__file__)
    print(proDir)
    createFile(proDir, "result")
