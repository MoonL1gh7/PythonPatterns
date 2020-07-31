from templator import render


class Application:
    def __init__(self, routes, front):
        self.routes = routes
        self.front = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        request = {}
        for front in self.front:
            front(request)
        if path in self.routes:
            view = self.routes[path]
        else:
            view = Not404(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body

class IndexView:
    def __call__(self, request):
        object_list = [{'test': 'one'}, {'test': 'two'}]
        template = render('index.html', object_list = object_list)
        return '200 OK', [bytes(template, encoding='utf-8')]


class Page:
    def __call__(self, request):
        return '200 OK', [b'<h1>next page</h1>']


class Not404:
    def __call__(self, request):
        return '404 NOT FOUND', [b'<h1>404 PAGE Not Found</h1>']


class Other:
    def __call__(self, request):
        return '200 OK', [b'<h1>other info</h1>']


routes = {
    '/': IndexView(),
    '/page/': Page(),
    '/other/': Other()
}


def secret_front(request):
    request['secret'] = 'some_secret'


def other_front(request):
    request['key'] = 'some_key'


fronts = [secret_front, other_front]


application = Application(routes, fronts)

