# -*- coding: utf-8 -*-
from celery.task import Task
from celery.decorators import task

class AddTask(object):
    def run(self, x, y):
        logger = self.get_logger(task_name=u'クラス')
        logger.info("Adding %s + %s" % (x, y))
        return x + y

@task
def add(x, y):
    logger = Task.get_logger(task_name=u'デコレータ')
    logger.info("Adding %s + %s" % (x, y))
    return x + y

#from celery.task import task
#
#@task
#def add(x, y):
#    return x + y
#
#if __name__ == '__main__':
#    print add.delay(4, 4)
