from django.db import models


class ColorCode(models.Model):
    # `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Upadlosc(models.Model):
    name = models.CharField('Nazwa Upadłości', max_length=300, unique=True)
    symbol = models.CharField('Symbol', max_length=50, unique=True)
    colorCode = models.ForeignKey(ColorCode)
    pub_date = models.DateTimeField('Data Publikacji')

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('documents:upadlosc-detail', [self.id])

class Contact(models.Model):
    name_text = models.CharField('Nazwa Upadłego', max_length=300)
    pub_date = models.DateTimeField('Data Publikacji')

    def __str__(self):
        return self.name_text

    @models.permalink
    def get_absolute_url(self):
        return ('documents:contact-detail', [self.id])


# Grupy kontaktów:urzędy, sądy itp.
class Contacts_groups(models.Model):
    # `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name



# kraje
class Countries(models.Model):
    # `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name = models.CharField(default=163, max_length=25)

    def __str__(self):
        return self.name


# adresy korespondencyjne
class Adresses(models.Model):
    # id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    version = models.CharField(max_length=25)
    street = models.CharField('Ulica', max_length=80)
    postalcode = models.CharField('Kod pocztowy', max_length=20)
    city = models.CharField('Miasto', max_length=50)
    country_id = models.ForeignKey(Countries)  # refernecja do id kraju

    def __str__(self):
        return "%s %s %s %s" % (self.street, self.postalcode, self.city, self.country_id)
      #  return self.id




# Rodzaj działalności
class Company_types(models.Model):
    # id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    companyType = models.CharField(max_length=25)
    description = models.TextField
    def __str__(self):
        return self.companyType


# Komornicy
class Bailiffs(models.Model):
    # `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    companyName = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    adress_id = models.ForeignKey(Adresses)
    companyType_id = models.ForeignKey(Company_types)


# Foldery
class Folders(models.Model):
    # `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    number = models.IntegerField(default=1)
    description = models.CharField(max_length=300)


# Upadłości
class Clients(models.Model):
    # `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    version = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    colorCode = models.IntegerField(default=00000)
    folder_id = models.ForeignKey(Folders)


# Sądy
class Courts(models.Model):
    # `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    companyName = models.CharField('Nazwa sądu:', max_length=300)
    department = models.CharField('Wydział:', max_length=50)
    adress_id = models.ForeignKey(Adresses)
    www = models.CharField('www:', max_length=100)
    #slug = models.SlugField()


    def __str__(self):
        return "%s %s %s %s" % (self.companyName, self.department, self.adress_id, self.www)

    @models.permalink
    def get_absolute_url(self):
        return ('documents:courts-create', [self.id])



# Urzędy
class Legal(models.Model):
    # id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    companyName = models.CharField('Urząd', max_length=25)
    name = models.CharField('Imię', max_length=25)
    lastname = models.CharField('Nazwisko', max_length=25)
    companyType_id = models.ForeignKey(Company_types)
    adress_id = models.ForeignKey(Adresses)
    def __str__(self):
        return self.companyName

# Kontakty
class Contacts(models.Model):
    # id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    version = models.IntegerField
    court_id = models.ForeignKey(Courts)
    legal_id = models.ForeignKey(Legal)
    baillif_id = models.ForeignKey(Bailiffs)


# Typ korespondencji: wychodząca, przychodząca
class Correspondency_type(models.Model):
    # `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name = models.CharField('Typ korespondencji', max_length=25)


# Wspomniane kontakty/ Do wiadomości
class Mentioned_clients(models.Model):
    # id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name = models.CharField('Wymienione kontakty', max_length=25)


# Korespondencja
class Correspondencies(models.Model):
    # id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    client_id = models.ForeignKey(Clients)
    receivedSentDate = models.DateTimeField('Data wysyłki')
    writingDate = models.DateTimeField('Data napisania')
    signature = models.CharField('Podpis', max_length=25)
    autoNumeration = models.IntegerField(default=0)  # jak zrobić autonumerację/inrementację?
    correspondencyType_id = models.ForeignKey(Correspondency_type)
    contactsGroup_id = models.ForeignKey(Contacts_groups)
    contact_id = models.ForeignKey(Contacts)
    subject = models.CharField('Temat', max_length=25)
    dueDate = models.DateTimeField('Data do której należy odpisać')
    scannedDocument = models.CharField('Skanuj dokument', max_length=25)
    fileName = models.CharField('Nazwa pliku', max_length=25)
    mentionedClient_id = models.ForeignKey(Mentioned_clients)


# Create your models here.

# Dokument
'''class Document(models.Model):
	version = models.CharField(max_length=255) #text: wersja dokumentu
	fullfilments = models.ManyToManyField(User, through="UserDocument") # wszystkie wypelnienia jednego TEGO dokumentu przez wszytskich uzytkownikow

#Pola w dokumencie
class Field(models.Model):
	type = models.CharField(max_length=255) # typ danych np.text
	version = models.CharField(max_length=255) # wersja pola w dokumencie
	active = models.BooleanField() # czy pole ma się pokazac w najnowszej wersji formularza
	documentID = models.ForeignKey(Document) # referencja do id dokumentu

#Dane do JSONa
class Data(models.Model):
	data = models.TextField() #zawsze musi być wpisany poprawny JSON, czyli jak dict w Pythonie

#relacja ManyToMany
class UserDocument(models.Model):
	userID = models.ForeignKey(User) #użytkownik id
	documentID = models.ForeignKey(Document)
	version = models.CharField(max_length=255)
	dataID = models.ForeignKey(Data)
'''
