from __future__ import with_statement
from contextlib import closing
import amqplib.client_0_8 as amqp

SERVER = dict(host='localhost',
              userid='guest',
              password='guest',
              ssl=False)

def callback(msg):
    for key, val in msg.properties.items():
        print '%s: %s' % (key, str(val))
        for key, val in msg.delivery_info.items():
            print '> %s: %s' % (key, str(val))

    print ''
    print msg.body
    print '-------'
    msg.channel.basic_ack(msg.delivery_tag)

with closing(amqp.Connection(**SERVER)) as conn:
    with closing(conn.channel()) as ch:
        ch.access_request("/data", active=True, read=True)

    ch.exchange_declare('myfan', 'fanout', auto_delete=True)

    qname, _, _ = ch.queue_declare()
    ch.queue_bind(qname, 'myfan')
    ch.basic_consume(qname, callback=callback)

    while ch.callbacks:
        ch.wait()
