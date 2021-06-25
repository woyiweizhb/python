import os

if __name__ == "__main__":
    ret = os.popen('node 1.js')
    print(ret.readlines())