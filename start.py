import os
from Queue import PriorityQueue
from threading import Thread
import datetime
import time
import sys

try:
    import canary
except ImportError:
    os.system('curl https://bootstrap.pypa.io/get-pip.py -o pip.py')
    os.system('python pip.py')
    os.system('rm pip.py')
    os.system('pip install tweepy')
    os.system('pip install requests==1.1.0')
    os.system('pip install python-firebase')
    import canary

import pulse

def __main__():
    q = PriorityQueue()	#elements will be a tuple (-1*time, [tweet])

    #producer = Thread(Target=pulse.stream_thread, args=(q,))
    consumer = Thread(Target=pulse.remove_thread, args=(q,))
    #analyzer = Thread(Target=pulse.analysis_thread, args=(q,))

    #producer.start()
    consumer.start()
    #analyzer.start()

