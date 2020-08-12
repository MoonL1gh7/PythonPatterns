from app.template import render


class IndexView:
    def __call__(self, request):
        secret = request.get('secret_key', None)
        print(secret)
        template = render('index.html', secret=secret)
        return '200 OK', template


class Other:
    def __call__(self, request):
        print(request)
        return '200 OK', '<h1>other info</h1>'


def contact_view(request):
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        print(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
        return '200 OK', render('contact.html')
    else:
        return '200 OK', render('contact.html')



class Contact:
    def __call_(self, request):
        if request['method'] == 'POST':
            data = request['data']
            title = data['title']
            text = data['text']
            email = data['email']
            print(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
            template = render('contact.html')
            return '200 OK', template
        else:
            return '200 OK', template






