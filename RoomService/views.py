from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
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
                  'RoomService/customer_dashboard.html',
                  {
                      'customer': customer,
                      'services_for_customer': services_for_customer,
                  })


class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'RoomService/service_detail.html'


class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['customer']
        widgets = {
            'start_datetime': DateTimeInput(),
        }


def customer_request_service(request, customer_id):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        service = form.save()
        service.customer = get_object_or_404(Customer, pk=customer_id)
        service.save()
        return redirect('customer-dashboard', customer_id)

    context = {'form': form}
    return render(request, 'RoomService/request_service.html', context)


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


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


def customer_register(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        customer = form.save()
        return redirect('customer-dashboard', customer.id)
    context = {'mode': 'register', 'form': form}
    return render(request, 'RoomService/customer_form.html', context)


def customer_update(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customer-dashboard', customer_id)

    context = {'mode': 'update', 'form': form}
    return render(request, 'RoomService/customer_form.html', context)


def cancel_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('customer-dashboard', service.customer_id)

    context = {'object': service}
    return render(request, 'RoomService/service_confirm_delete.html', context)
