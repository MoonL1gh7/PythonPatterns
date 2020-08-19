from app.template import render


class IndexView:
    def __call__(self, request):
        secret = request.get('secret_key', None)
        print(secret)
        return '200 OK', render('index.html', secret=secret)


class Other:
    def __call__(self, request):
        print(request)
        return '200 OK', render('other.html')


class Contact:
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            title = data['title']
            text = data['text']
            email = data['email']
            print(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
            return '200 OK', render('contact.html')
        else:
            return '200 OK', render('contact.html')






