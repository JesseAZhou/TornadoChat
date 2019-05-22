import tornado.ioloop
import tornado.web
from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ])


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body

# asynchronous
async def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body

# coroutines
def async_fetch_manual(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_fututre = http_client.fetch(url)
    def on_fetch(f):
        my_future.set_result(f.result().body)
    fetch_fututre.add_done_callback(on_fetch)
    return my_future

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()
    a = synchronous_fetch('localhost:8888')
    print(a,'--------')