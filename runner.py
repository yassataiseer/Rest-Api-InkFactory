
from subprocess import *
import time
#subprocess.run("python restful.py & python test.py", shell=True)
Popen('python api_1.py')
time.sleep(1)
Popen('test.py')