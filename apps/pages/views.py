from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from ..users.models import City
from ..movies.models import Movie

# Create your views here.


class IndexView(ListView):
    template_name = 'pages/index.html'
    model = Movie
    context_object_name = 'movies'
    paginate_by = 5

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        city_name = request.POST.get('city')
        if not city_name:
            messages.error(request, 'Invalid city entered')
            return redirect(request.path)
        try:
            city = City.objects.get(name=city_name)
        except City.DoesNotExist:
            messages.error(request, "Invalid city entered")
            return redirect(request.path)
        if city == request.user.city:
            messages.info(request, 'City already updated')
            return redirect(request.path)
        request.user.city = city
        request.user.save()

        messages.success(request, 'City updated')
        return redirect(request.path)
