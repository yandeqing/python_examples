import os


def getFileParentDir(filepath):
    """
    获取文件的上一级文件夹
    :param filepath:
    :return:
    """
    return os.path.abspath(os.path.join(os.path.dirname(filepath), os.path.pardir))


def createFile(proDir,fileName):
    """
    创建文件
    :param fileName:
    :return:
    """
    resultPath = os.path.join(proDir, fileName)
    print(resultPath)
    if not os.path.exists(resultPath):
        os.mkdir(resultPath)


if __name__ == "__main__":
    proDir = getFileParentDir(__file__)
    print(proDir)
    createFile(proDir,"result")
