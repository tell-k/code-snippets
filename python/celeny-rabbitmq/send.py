from __future__ import with_statement
from contextlib import closing
import amqplib.client_0_8 as amqp

SERVER = dict(host='localhost',
              userid='guest',
              password='guest',
              ssl=False)

with closing(amqp.Connection(**SERVER)) as conn:
    with closing(conn.channel()) as ch:
        ch.access_request("/data", active=True, write=True)

    ch.exchange_declare('myfan', 'fanout', auto_delete=True)

    msg = amqp.Message("Hello World",
                        content_type="text/plain",
                        application_headers={})

    ch.basic_publish(msg, 'myfan')
