import os
import time

class watch(object):
    def __init__(self, file_path: str, separator: str, call_back, sleep_time: float = 0.001):
        self.file_path = file_path
        self.file = open(file_path,"rb")
        self.c_f = sleep_time
        self.eof = separator
        self.call_f = call_back
        self.os_st_size = 6
    def start(self):
        buff = ''
        s1 = os.stat(self.file_path)[self.os_st_size]
        while(True):
            time.sleep(self.c_f)
            s2 = os.stat(self.file_path)[self.os_st_size]
            if s1 < s2 :
                self.file.seek(s1, 0)
                buff += self.file.read(s2 - s1).decode('utf-8')
                c = buff.split(self.eof)
                if len(c) > 1 :
                    for i in c[:-1] :
                        self.call_f(i)
                    buff = c[-1]
            s1 = s2
