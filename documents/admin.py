from django.contrib import admin
#from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline

# Register your models here.
from .models import Contact, Upadlosc, ColorCode, Contacts_groups, Contacts, Legal, Company_types, Adresses, Countries, Courts

from django.contrib import admin
from attachments.admin import AttachmentInlines
from django_object_actions import DjangoObjectActions

class contactsGroupInline(admin.TabularInline):
    model = Contacts_groups
    #extra = 3


class MyEntryOptions(admin.ModelAdmin):
    inlines = (AttachmentInlines,)

admin.site.register(Company_types)

class AdressesInline(admin.TabularInline):
    model = Adresses
admin.site.register(Adresses)
admin.site.register(Countries)

class CourtsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nazwa sądu:', {'fields': ['companyName']}),
        ('Departament:', {'fields': ['department']}),
        ('www:', {'fields': ['www']}),
        ('Adres:', {'fields':['adress_id']}),
    ]
    list_display = ('companyName', 'department', 'www',  'adress_id')
    inlines = [AdressesInline]
    def __unicode__(self):
        return self.companyName
admin.site.register(Courts, CourtsAdmin)

#urzedy
class LegalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nazwa urzędu:', {'fields': ['companyName']}),
        ('Imię:', {'fields': ['name']}),
        ('Nazwisko:', {'fields': ['lastname']}),
        ('Rodzaj spółki:',{'fields': ['companyType_id']}),
        ('Adres:', {'fields':['adress_id']}),
    ]
    list_display = ('companyName', 'name', 'lastname', 'companyType_id', 'adress_id')

    def __unicode__(self):
        return self.companyName
admin.site.register(Legal, LegalAdmin)

class ContactsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Wersja', {'fields': ['version']}),
        ('Sąd:', {'fields': ['court_id']}),
        ('Urząd:', {'fields': ['legal_id']}),
        ('Komornik:', {'fields': ['baillif_id']}),
    ]

    list_display = ('version', 'court_id', 'legal_id', 'baillif_id')

    def __unicode__(self):
        return self.name


admin.site.register(Contacts, ContactsAdmin)

class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nazwa Kontaktu', {'fields': ['name_text']}),
        ('Data publikacji', {'fields': ['pub_date']}),
    ]

    list_display = ('name_text', 'pub_date')
    inlines = (AttachmentInlines,)

    # inlines = [MyEntryOptions]
    #inlines = [contactsGroupInline,]
    def __unicode__(self):
        return self.name


admin.site.register(Contact, ContactAdmin)


# admin.site.register(AttachmentInlines, MyEntryOptions)

class UpadloscAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nazwa Upadłości', {'fields': ['name']}),
        ('Symbol', {'fields': ['symbol']}),
        ('Kolor', {'fields': ['colorCode']}),
        ('Data publikacji', {'fields': ['pub_date']}),
    ]
    list_display = ('name', 'symbol', 'pub_date', 'colorCode')
    inlines = (AttachmentInlines,)

    # inlines= [ColorCode]
    # inlines = [MyEntryOptions]
    # inlines = [ChoiceInline]
    def __unicode__(self):
        return self.name


admin.site.register(Upadlosc, UpadloscAdmin)
admin.site.register(ColorCode)
admin.site.register(Contacts_groups)

# print button

class MyModelAdmin(DjangoObjectActions, admin.ModelAdmin):
    def toolfunc(self, request, obj):
        pass

    toolfunc.label = "Drukuj"  # optional
    toolfunc.short_description = "Kliknij aby wydrukować"  # optional

    def make_published(modeladmin, request, queryset):
        queryset.update(status='p')

    change_actions = ('toolfunc',)
    changelist_actions = ('make_published',)
