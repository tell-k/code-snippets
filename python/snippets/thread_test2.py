import threading
import Queue
import commands
import time

# thread class to run a command
class ExampleThread(threading.Thread):
    def __init__(self, cmd, queue):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.queue = queue

    def run(self):
        # execute the command, queue the result
        (status, output) = commands.getstatusoutput(self.cmd)
        self.queue.put((self.cmd, output, status))

# queue where results are placed
result_queue = Queue.Queue()

# define the commands to be run in parallel, run them
cmds = ['python echo3.py',
        'python echo2.py',
        'python echo1.py',
       ]
for cmd in cmds:
    thread = ExampleThread(cmd, result_queue)
    thread.start()

# print results as we get them
while threading.active_count() > 1 or not result_queue.empty():
    while not result_queue.empty():
        (cmd, output, status) = result_queue.get()
        print('%s:' % cmd)
        print(output)
        print('='*60)
    time.sleep(1)
