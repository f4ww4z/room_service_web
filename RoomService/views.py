from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from RoomService.models import Customer, Service


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


class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'RoomService/service_detail.html'


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        widgets = {
            'start_datetime': DateTimeInput(),
        }


class CustomerRequestServiceView(generic.CreateView):
    model = Service
    form_class = ServiceForm

    def get(self, request, *args, **kwargs):
        context = {'form': ServiceForm()}
        return render(request, 'RoomService/request_service.html', context)

    def post(self, request, *args, **kwargs):
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            service.save()
            return HttpResponseRedirect(
                reverse_lazy('service-detail', args=[service.id]))
        else:
            form = ServiceForm()
