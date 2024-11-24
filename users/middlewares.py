from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class LevelMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            level = request.POST.get('level')
            if level not in ['Junior', 'Middle', 'Senior']:
                return HttpResponseBadRequest('Такого уровня не существует.')
            elif level == 'Junior':
                request.salary = 300
            elif level == 'Middle':
                request.salary = 1000
            elif level == 'Senior':
                request.salary = 2000

        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'salary', 'Уровень не определен.')