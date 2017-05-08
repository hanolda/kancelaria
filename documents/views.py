from django.shortcuts import render_to_response, get_object_or_404, render
from django.urls import reverse
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact, Upadlosc, Contacts, Contacts_groups, Legal, Courts, Adresses
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView



def index(request):
    latest_contact_list = Contact.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.name_text for q in latest_contact_list])
    context = {'latest_contact_list': latest_contact_list}
    return render(request, 'documents/index.html', context)


# return HttpResponse(output)
# return render(request, 'documents/index.html', output)


# def detail(request, upadly_id):
#	upadly = get_object_or_404(Upadly, pk=upadly_id)
#	return render(request, 'documents/detail.html', {'upadly': upadly})

# def upadly_list(request):
#    upadly = Upadly.objects.all()
#    return render(request,'documents/upadly_list.html', {'object_list': upadly})

#adres
class AdressesListView(ListView):
    model = Adresses


class AdressesDetailView(DetailView):
    model = Adresses

# upadly_list zastapiono lista genericclass FoodListView(ListView):
class ContactListView(ListView):
    model = Contact


class ContactDetailView(DetailView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = '__all__'


# zarzadzanie upadlosciami
# lista
class UpadloscListView(ListView):
    model = Upadlosc


# szczegoly
class UpadloscDetailView(DetailView):
    model = Upadlosc


# dodaj
class UpadloscCreateView(CreateView):
    model = Upadlosc
    fields = '__all__'

# zarzadzanie urzedami
# lista
class LegalListView(ListView):
    model = Legal


# szczegoly
class LegalDetailView(DetailView):
    model = Legal


# dodaj
class LegalCreateView(CreateView):
    model = Legal
    fields = '__all__'

# zarzadzanie sądami
# lista
class CourtsListView(ListView):
    model = Courts

#szczególy
class CourtsDetailView(DetailView):
    model = Courts

#dodaj
class CourtsCreateView(CreateView):
    model = Courts
    fields = '__all__'
    def get_success_url(self):
        return reverse ('documents:courts-list')

class CourtsUpdateView(UpdateView):
    model = Courts
    fields = '__all__'

    def get_success_url(self):
        return reverse('documents:courts-detail', args=[self.kwargs['pk']])

#usuń
class CourtsDeleteView(DeleteView):
    model = Courts
    #fields = '__all__'

    def get_success_url(self):
        return reverse ('documents:courts-list')


# zarządzanie grupami kontaktów
class ContactGroupListView(ListView):
    model = Contacts_groups


# file upload
def home(request):
    return render(request, 'index.htm', {'what': 'Django File Upload'})


def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")

    return HttpResponse("Failed")


def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
