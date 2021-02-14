# pyfoc
Pyfoc focuses on changing files as a real-time process.
## Usage
```python
import pyfoc

def call_back_func(data):
  #Do something.
  print(data)

w = pyfoc.watch(file_path="/var/log/syslog", separator="\n", call_back=call_back_func)
w.start()
```
