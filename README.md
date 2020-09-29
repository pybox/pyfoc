# pyfoc
Focus on real-time file changes in log files, real-time charts, etc.

## Usage
```python
import pyfoc

def call_back_func(data):
  #Do something.
  print(data)

w = pyfoc.watch(file_path="/var/log/syslog", separator="\n", call_back=call_back_func)
w.start()
```
