from app.wsgiapp import Application 
from app.template import render
from app.controller import front_controllers
from app.log import Logger
from view import SiteModel



site = SiteModel()
LOGGER = Logger('main')


class IndexView:
    def __call__(self, request):
        LOGGER.log('IndexView')
        secret = request.get('secret_key', None)
        print(secret)
        return '200 OK', render('index.html', objects_list=site.courses)


class CreateCourse:
    def __call__(self, request):
        LOGGER.log('CreateCourse')
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            category_id = data.get('category_id')
            print(category_id)
            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
                course = site.create_course('record', name, category)
                site.courses.append(course)
            return '200 OK', render('create_course.html')
        else:
            categories = site.categories
            return '200 OK', render('create_course.html', categories=categories)


class CreateCategory:
    def __call__(self, request):
        LOGGER.log('CreateCategory')
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            category_id = data.get('category_id')
            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
            new_category = site.create_category(name, category)
            site.categories.append(new_category)
            return '200 OK', render('create_category.html')
        else:
            categories = site.categories
            return '200 OK', render('create_category.html', categories=categories)


class Contact:
    def __call__(self, request):
        LOGGER.log('Contacts')
        if request['method'] == 'POST':
            data = request['data']
            title = data['title']
            text = data['text']
            email = data['email']
            print(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
            return '200 OK', render('contact.html')
        else:
            return '200 OK', render('contact.html')


# @application.add_route('/category-list/')
# class CategoriesList:
#     def __call__(self, request):
#         LOGGER.log('CategoriesList')
#         return '200 OK', render('category_list.html', objects_list=site.categories)


urlpatterns = {
    '/': IndexView(),
    # '/category_list/': CategoriesList(),
    '/create_category/': CreateCategory(),
    '/create_course/': CreateCourse(),
    '/contact/': Contact()
}


application = Application(urlpatterns, front_controllers)

@application.add_route('/category_list/')
def category_list(request):
    LOGGER.log('Список категорий')
    return '200 OK', render('category_list.html', objects_list=site.categories)