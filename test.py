import os

if __name__ == "__main__":
    ret = os.popen('dir')
    print(ret.readlines())