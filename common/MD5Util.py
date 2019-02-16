import hashlib


def md5s(strs):
    m = hashlib.md5()
    m.update(strs.encode("utf8"))
    return m.hexdigest()


if __name__ == '__main__':
    print(md5s("34038092649035HOUSEPHP58"))
