from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .models import Book
from ..shows.models import Show
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Sum

# Create your views here.


class CreateShowBookingView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['ticket_quantity']
    template_name = 'book/show.html'
    success_url = reverse_lazy('pages:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        show = Show.objects.get(id=self.kwargs['s'])
        context['show'] = show
        return context

    def form_valid(self, form):
        ticket_quantity = form.cleaned_data['ticket_quantity']
        form.instance.user = self.request.user
        show = Show.objects.get(id=self.kwargs['s'])
        form.instance.show = show

        capacity = show.screen.capacity
        current_booking_count = Book.objects.filter(
            show=show.id).aggregate(Sum('ticket_quantity'))['ticket_quantity__sum'] or 0
        
        if (current_booking_count + ticket_quantity) > capacity:
            messages.error(self.request, "Capacity limit reached")
            return redirect(self.success_url)

        messages.success(self.request, 'Booking created')
        return super().form_valid(form)
