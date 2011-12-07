
import threading
threading_local = threading.local()

def remove_threading_local(application):
    def func(env, start_response):
        res = application(env, start_response)
        global threading_local
        del threading_local
        threading_local = threading.local()
        return res
    return func

@remove_threading_local
def application(env, start_response):
    start_response('200 OK', [('ContentType', 'text/plain')])

    if hasattr(threading_local, 'key'):
        threading_local.key += 1
    else:
        threading_local.key = 0

    return 'Hello WSGI world!' + str(threading_local.key)

from werkzeug import run_simple
run_simple('0.0.0.0', 8000, application)
