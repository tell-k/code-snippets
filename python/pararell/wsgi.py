import time

def cpu_bound_work():
    i = 0
    while i < 100000000:
        i += 1


def app(environ, start_response):
    """Simplest possible application object"""
    # Do some work...
    time.sleep(1)

    # Send the response
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
