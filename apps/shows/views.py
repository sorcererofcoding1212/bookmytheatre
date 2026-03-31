from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from .models import Show
from ..movies.models import Movie
from django.utils import timezone
from django.contrib import messages
from datetime import timedelta, datetime
from django.shortcuts import redirect

# Create your views here.


class ShowListView(ListView):
    template_name = 'shows/shows.html'
    model = Show
    context_object_name = 'shows'

    def get(self, request, *args, **kwargs):
        date_str = request.GET.get("dt")
        current_date = timezone.localdate()
        if date_str:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            if date_obj < current_date:
                messages.error(request, 'Invalid date selected')
                return redirect("pages:home")
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        date_str = self.request.GET.get('dt')
        current_date = timezone.localdate()

        return super().get_queryset().filter(
            screen__venue__city=self.request.user.city, show_timings__date=datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else current_date, movie_id=self.kwargs['m'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movie"] = Movie.objects.get(id=self.kwargs['m'])
        current_date = timezone.localdate()
        date_str = self.request.GET.get("dt")
        if not date_str:
            selected_date = current_date
        else:
            selected_date = datetime.strptime(
                date_str, "%Y-%m-%d").date()

        dates = [current_date + timedelta(days=i) for i in range(7)]
        context["dates"] = dates
        context["selected_date"] = selected_date
        groupedShows = {}
        shows = context["shows"]
        for show in shows:
            venue = show.screen.venue
            if venue not in groupedShows:
                groupedShows[venue] = []
            groupedShows[venue].append(show)
        context["groupedShows"] = groupedShows
        return context


class ShowDetailView(LoginRequiredMixin, DetailView):
    template_name = 'shows/show.html'
    context_object_name = 'show'
    model = Show
