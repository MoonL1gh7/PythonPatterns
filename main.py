from app.wsgiapp import Application, FakeApplication, DebugApplication
from app.wavy import ListView, CreateView
from app.template import render
from app.controller import front_controllers
from app.log import Logger
from view import SiteModel



site = SiteModel()


class CategoryCreateView(CreateView):
    template_name = 'create_category.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = site.categories
        return context

    def create_obj(self, data: dict):
        name = data['name']
        category_id = data.get('category_id')

        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

        new_category = site.create_category(name, category)
        site.categories.append(new_category)


class IndexView:
    def __call__(self, request):
        secret = request.get('secret_key', None)
        print(secret)
        return '200 OK', render('index.html', objects_list=site.courses)


class CreateCourse:
    def __call__(self, request):
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


class CreateCategory(CreateView):
    template_name = 'create_category.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = site.categories
        return context

    def create_obj(self, data: dict):
        name = data['name']
        category_id = data.get('category_id')

        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

        new_category = site.create_category(name, category)
        site.categories.append(new_category)


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


class CategoriesList(ListView):
    queryset = site.categories
    template_name = 'categories_list.html'


class StudentCreate(CreateView):
    template_name = 'create_student.html'
    def create_obj(self, data: dict):
        name = data['name']
        new_obj = site.create_user('student', name)
        site.students.append(new_obj)


class AddStudentToCourse(CreateView):
    template_name = 'add_student.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['courses'] = site.courses
        context['students'] = site.students
        return context

    def create_obj(self, data: dict):
        course_name = data['course_name']
        course = site.get_course(course_name)
        student_name = data['student_name']
        student = site.get_student(student_name)
        course.add_student(student)


urlpatterns = {
    '/': IndexView(),
    '/create_category/': CreateCategory(),
    '/create_course/': CreateCourse(),
    '/contact/': Contact(),
    '/categories_list/':CategoriesList(),
    '/create_student/': StudentCreate(),
    '/add_student/': AddStudentToCourse(),
}


application = Application(urlpatterns, front_controllers)
# application = FakeApplication(urlpatterns, front_controllers)
# application = DebugApplication(urlpatterns, front_controllers)


@application.add_route('/students_list/')
class StudentList(ListView):
    queryset = site.students
    template_name = 'students_list.html'