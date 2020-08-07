from app.wsgiapp import Application 
from view import IndexView, Other, contact_view, Contact

urlpatterns = {
    '/': IndexView(),
    '/other/': Other(),
    '/contact/': contact_view,
    # '/contact/': Contact()
}


def secret_controller(request):
    request['secret_key'] = 'SECRET_KEY'


front_controllers = [
    secret_controller
]

application = Application(urlpatterns, front_controllers)

# Запуск:
# gunicorn main:application
