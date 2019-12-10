from django.views import generic

from RoomService.models import Customer


class HomeView(generic.ListView):
    template_name = 'RoomService/index.html'
    context_object_name = 'customer_list'

    def get_queryset(self):
        return Customer.objects.all()


class CustomerView(generic.DetailView):
    model = Customer
    template_name = 'RoomService/customer.html'
