from django.shortcuts import render, get_object_or_404
from django.views import generic

from RoomService.models import Customer


class HomeView(generic.ListView):
    template_name = 'RoomService/index.html'
    context_object_name = 'customer_list'

    def get_queryset(self):
        return Customer.objects.all()


def customer_dashboard(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    services_for_customer = customer.service_set.all()

    return render(request,
                  'RoomService/customer.html',
                  {
                      'customer': customer,
                      'services_for_customer': services_for_customer,
                  })
