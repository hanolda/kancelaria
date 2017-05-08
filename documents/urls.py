from django.conf.urls import url,  include



from . import views
from documents.views import ContactListView, ContactDetailView, ContactCreateView,UpadloscListView, UpadloscDetailView, UpadloscCreateView, ContactGroupListView, LegalListView, LegalDetailView, LegalCreateView, CourtsCreateView, CourtsDetailView, CourtsListView, CourtsUpdateView, CourtsDeleteView, AdressesDetailView, AdressesListView
#upadly_list
#from formupload import views

urlpatterns = [
	
	url(r'^$', views.index, name='index'),
	#url(r'^$', views.detail, name='detail'),
	#zastapiony generic url(r'^upadly/$', upadly_list, name='upadly-list'),
	#zarzadzanie kontaktami
	url(r'^contact/$', ContactListView.as_view(), name='contact-list'),
	url(r'^contact/(?P<pk>\d+)$', ContactDetailView.as_view(), name='contact-detail'),
	url(r'^contact/create$', ContactCreateView.as_view(), name='contact-create'),
	#zarzadzanie urzedami
	url(r'^contact/legal$', LegalListView.as_view(), name='legal-list'),
	url(r'^contact/legal/(?P<pk>\d+)$', LegalDetailView.as_view(), name='legal-detail'),
	url(r'^contact/legal/create$', LegalCreateView.as_view(), name='legal-create'),
	# zarzadzanie sądami
	url(r'^contact/courts$', CourtsListView.as_view(), name='courts-list'),
	url(r'^contact/courts/(?P<pk>\d+)$', CourtsDetailView.as_view(), name='courts-detail'),
	url(r'^contact/courts/create$', CourtsCreateView.as_view(), name='courts-create'),
	url(r'^contact/courts/(?P<pk>\d+)/update$', CourtsUpdateView.as_view(), name='courts-update'),
	url(r'^contact/courts/remove_court/(?P<pk>\d+)/$', CourtsDeleteView.as_view(), name='courts-delete'),
	#url(r'^(?P<slug>[-\w]+)/remove_court/(?P<pk>\d+)/$', CourtsDeleteView.as_view(), name='courts-delete'),
	#zarzadzanie upadlosciami
	url(r'^upadlosc/$', UpadloscListView.as_view(), name='upadlosc-list'),
	url(r'^upadlosc/create$', UpadloscCreateView.as_view(), name='upadlosc-create'),
	url(r'^upadlosc/(?P<pk>\d+)$', UpadloscDetailView.as_view(), name='upadlosc-detail'),
	#adress
	url(r'^contact/adress/$', AdressesListView.as_view(), name='adress-list'),
	url(r'^contact/adress/$', AdressesDetailView.as_view(), name='radress--detail'),
	url(r'^$', views.home, name="home"),
    url(r'^upload/', views.upload, name="upload"),

]