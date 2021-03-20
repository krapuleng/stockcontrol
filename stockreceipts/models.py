# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.shortcuts import reverse
from django.conf import settings
CURRENCY = settings.CURRENCY
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django_random_id_model import RandomIDModel
from django.forms import inlineformset_factory
from django.contrib import admin
import uuid



class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name
        
class OrderManager(models.Manager):
    def active(self):
        return self.filter(active=True)

class Applications(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APPLICATIONS'


class Attribute(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATTRIBUTE'


class Attributeinstance(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    attributesetinstance = models.ForeignKey('Attributesetinstance', models.DO_NOTHING, db_column='ATTRIBUTESETINSTANCE_ID')  # Field name made lowercase.
    attribute = models.ForeignKey(Attribute, models.DO_NOTHING, db_column='ATTRIBUTE_ID')  # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATTRIBUTEINSTANCE'


class Attributeset(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATTRIBUTESET'


class Attributesetinstance(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    attributeset = models.ForeignKey(Attributeset, models.DO_NOTHING, db_column='ATTRIBUTESET_ID')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATTRIBUTESETINSTANCE'


class Attributeuse(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    attributeset = models.ForeignKey(Attributeset, models.DO_NOTHING, db_column='ATTRIBUTESET_ID')  # Field name made lowercase.
    attribute = models.ForeignKey(Attribute, models.DO_NOTHING, db_column='ATTRIBUTE_ID')  # Field name made lowercase.
    lineno = models.IntegerField(db_column='LINENO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATTRIBUTEUSE'
        unique_together = (('attributeset', 'lineno'),)


class Attributevalue(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    attribute = models.ForeignKey(Attribute, models.DO_NOTHING, db_column='ATTRIBUTE_ID')  # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATTRIBUTEVALUE'


class Categories(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=255)  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='PARENTID', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='IMAGE', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'CATEGORIES'


class Closedcash(models.Model):
    money = models.CharField(db_column='MONEY', primary_key=True, max_length=255)  # Field name made lowercase.
    host = models.CharField(db_column='HOST', max_length=255)  # Field name made lowercase.
    hostsequence = models.IntegerField(db_column='HOSTSEQUENCE')  # Field name made lowercase.
    datestart = models.DateTimeField(db_column='DATESTART')  # Field name made lowercase.
    dateend = models.DateTimeField(db_column='DATEEND', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.money

    class Meta:
        managed = False
        db_table = 'CLOSEDCASH'
        unique_together = (('host', 'hostsequence'),)


class Customers(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    searchkey = models.CharField(db_column='SEARCHKEY', unique=True, max_length=255)  # Field name made lowercase.
    taxid = models.CharField(db_column='TAXID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    taxcategory = models.ForeignKey('Taxcustcategories', models.DO_NOTHING, db_column='TAXCATEGORY', blank=True, null=True)  # Field name made lowercase.
    card = models.CharField(db_column='CARD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maxdebt = models.FloatField(db_column='MAXDEBT')  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='ADDRESS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postal = models.CharField(db_column='POSTAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FIRSTNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LASTNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='PHONE2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='NOTES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    visible = models.TextField(db_column='VISIBLE')  # Field name made lowercase. This field type is a guess.
    curdate = models.DateTimeField(db_column='CURDATE', blank=True, null=True)  # Field name made lowercase.
    curdebt = models.FloatField(db_column='CURDEBT', blank=True, null=True)  # Field name made lowercase.
    properties = models.TextField(db_column='PROPERTIES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMERS'


class Floors(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    image = models.TextField(db_column='IMAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FLOORS'


class Geolayers(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    visible = models.TextField(db_column='VISIBLE')  # Field name made lowercase. This field type is a guess.
    icon = models.TextField(db_column='ICON', blank=True, null=True)  # Field name made lowercase.
    colour = models.CharField(db_column='COLOUR', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GEOLAYERS'


class Geomarkers(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE')  # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE')  # Field name made lowercase.
    visible = models.TextField(db_column='VISIBLE')  # Field name made lowercase. This field type is a guess.
    geolayer = models.ForeignKey(Geolayers, models.DO_NOTHING, db_column='GEOLAYER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GEOMARKERS'


class Locations(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isclose = models.TextField(db_column='ISCLOSE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'LOCATIONS'


class Payments(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    receipt = models.ForeignKey('Receipts', models.DO_NOTHING, db_column='RECEIPT')  # Field name made lowercase.
    payment = models.CharField(db_column='PAYMENT', max_length=255)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL')  # Field name made lowercase.
    transid = models.CharField(db_column='TRANSID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    returnmsg = models.TextField(db_column='RETURNMSG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PAYMENTS'


class People(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    apppassword = models.CharField(db_column='APPPASSWORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    card = models.CharField(db_column='CARD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    role = models.ForeignKey('Roles', models.DO_NOTHING, db_column='ROLE')  # Field name made lowercase.
    visible = models.TextField(db_column='VISIBLE')  # Field name made lowercase. This field type is a guess.
    image = models.TextField(db_column='IMAGE', blank=True, null=True)  # Field name made lowercase.
    properties = models.TextField(db_column='PROPERTIES', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'PEOPLE'
        verbose_name_plural='People'


class Places(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    x = models.IntegerField(db_column='X')  # Field name made lowercase.
    y = models.IntegerField(db_column='Y')  # Field name made lowercase.
    floor = models.ForeignKey(Floors, models.DO_NOTHING, db_column='FLOOR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLACES'


class Products(models.Model):
    id = models.CharField(default=uuid.uuid4, db_column='ID', primary_key=True, max_length=255,editable= False)
    reference = models.CharField(db_column='REFERENCE', unique=True, max_length=255)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=255)  # Field name made lowercase.
    codetype = models.CharField(db_column='CODETYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    pricebuy = models.FloatField(db_column='PRICEBUY')  # Field name made lowercase.
    pricesell = models.FloatField(db_column='PRICESELL')  # Field name made lowercase.
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='CATEGORY', default='000')  # Field name made lowercase.
    taxcat = models.ForeignKey('Taxcategories', models.DO_NOTHING, db_column='TAXCAT', default='000')  # Field name made lowercase.
    attributeset = models.ForeignKey(Attributeset, models.DO_NOTHING, db_column='ATTRIBUTESET_ID', blank=True, null=True)  # Field name made lowercase.
    stockcost = models.FloatField(db_column='STOCKCOST', blank=True, null=True)  # Field name made lowercase.
    stockvolume = models.FloatField(db_column='STOCKVOLUME', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='IMAGE', blank=True, null=True, default='null')  # Field name made lowercase.
    iscom = models.BooleanField(db_column='ISCOM',default=0)  # Field name made lowercase. This field type is a guess.
    isscale = models.BooleanField(db_column='ISSCALE',blank=True, default=0)  # Field name made lowercase. This field type is a guess.
    attributes = models.TextField(db_column='ATTRIBUTES', blank=True, null=True, default='null')  # Field name made lowercase.    objects = models.Manager()
    browser = OrderManager()
    
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'PRODUCTS'
        verbose_name_plural='Products'

    def get_absolute_url(self):
        return reverse('productdetail', kwargs={'slug': self.slug})

    def add_to_purchases(self):
        return reverse("add_to_purchases", kwargs={'slug': self.slug})

    def update_slug(self,*args, **kwargs):
        for obj in Products.objects.all():
            obj.slug = slugify(obj.name)
            print(obj.code,obj.slug)
            #obj.save()
   

class ProductsCat(models.Model):
    product = models.OneToOneField(Products, models.DO_NOTHING, db_column='PRODUCT', primary_key=True)  # Field name made lowercase.
    catorder = models.IntegerField(db_column='CATORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCTS_CAT'


class ProductsCom(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    product = models.ForeignKey(Products, models.DO_NOTHING, db_column='PRODUCT', related_name='MainProduct')  # Field name made lowercase.
    product2 = models.ForeignKey(Products, models.DO_NOTHING, db_column='PRODUCT2',related_name='SubProduct')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCTS_COM'
        unique_together = (('product', 'product2'),)


class Receipts(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    money = models.ForeignKey(Closedcash, models.DO_NOTHING, db_column='MONEY',blank=True, null=True)  # Field name made lowercase.
    datenew = models.DateTimeField(db_column='DATENEW')  # Field name made lowercase.
    attributes = models.TextField(db_column='ATTRIBUTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RECEIPTS'
        ordering = ['-datenew']


class Reservations(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    created = models.DateTimeField(db_column='CREATED')  # Field name made lowercase.
    datenew = models.DateTimeField(db_column='DATENEW')  # Field name made lowercase.
    datenew = models.DateTimeField(db_column='DATENEW')  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255)  # Field name made lowercase.
    chairs = models.IntegerField(db_column='CHAIRS')  # Field name made lowercase.
    isdone = models.TextField(db_column='ISDONE')  # Field name made lowercase. This field type is a guess.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVATIONS'


class ReservationCustomers(models.Model):
    id = models.OneToOneField(Reservations, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CUSTOMER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVATION_CUSTOMERS'


class Resources(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    restype = models.IntegerField(db_column='RESTYPE')  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESOURCES'


class Roles(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    permissions = models.TextField(db_column='PERMISSIONS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROLES'


class Sharedtickets(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHAREDTICKETS'


class Stockcurrent(models.Model):
    location = models.ForeignKey(Locations, models.DO_NOTHING, db_column='LOCATION')  # Field name made lowercase.
    product = models.ForeignKey(Products, models.DO_NOTHING, db_column='PRODUCT')  # Field name made lowercase.
    attributesetinstance = models.ForeignKey(Attributesetinstance, models.DO_NOTHING, db_column='ATTRIBUTESETINSTANCE_ID', blank=True, null=True)  # Field name made lowercase.
    units = models.FloatField(db_column='UNITS')  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=255, primary_key=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.product.name) + " "+str(self.units)
        pass
    class Meta:
        managed = False
        db_table = 'STOCKCURRENT'
        unique_together = (('location', 'product', 'attributesetinstance'),)


class Stockdiary(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    datenew = models.DateTimeField(db_column='DATENEW')  # Field name made lowercase.
    reason = models.IntegerField(db_column='REASON')  # Field name made lowercase.
    location = models.ForeignKey(Locations, models.DO_NOTHING, db_column='LOCATION')  # Field name made lowercase.
    product = models.ForeignKey(Products, models.DO_NOTHING, db_column='PRODUCT')  # Field name made lowercase.
    attributesetinstance = models.ForeignKey(Attributesetinstance, models.DO_NOTHING, db_column='ATTRIBUTESETINSTANCE_ID', blank=True, null=True)  # Field name made lowercase.
    units = models.FloatField(db_column='UNITS')  # Field name made lowercase.
    price = models.FloatField(db_column='PRICE')  # Field name made lowercase.
    def __str__(self):
        return str(self.datenew) +"  "+ str(self.product.name) +" "+str(self.reason)
        pass
    class Meta:
        managed = False
        db_table = 'STOCKDIARY'


class Stocklevel(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    location = models.ForeignKey(Locations, models.DO_NOTHING, db_column='LOCATION')  # Field name made lowercase.
    product = models.ForeignKey(Products, models.DO_NOTHING, db_column='PRODUCT')  # Field name made lowercase.
    stocksecurity = models.FloatField(db_column='STOCKSECURITY', blank=True, null=True)  # Field name made lowercase.
    stockmaximum = models.FloatField(db_column='STOCKMAXIMUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STOCKLEVEL'


class Taxcategories(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    def __str__(self):
        return str(self.name)
    class Meta:
        managed = False
        db_table = 'TAXCATEGORIES'


class Taxcustcategories(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXCUSTCATEGORIES'


class Taxes(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    validfrom = models.DateTimeField(db_column='VALIDFROM')  # Field name made lowercase.
    category = models.ForeignKey(Taxcategories, models.DO_NOTHING, db_column='CATEGORY')  # Field name made lowercase.
    custcategory = models.ForeignKey(Taxcustcategories, models.DO_NOTHING, db_column='CUSTCATEGORY', blank=True, null=True)  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='PARENTID', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='RATE')  # Field name made lowercase.
    ratecascade = models.TextField(db_column='RATECASCADE')  # Field name made lowercase. This field type is a guess.
    rateorder = models.IntegerField(db_column='RATEORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXES'


class Taxlines(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    receipt = models.ForeignKey(Receipts, models.DO_NOTHING, db_column='RECEIPT')  # Field name made lowercase.
    taxid = models.ForeignKey(Taxes, models.DO_NOTHING, db_column='TAXID')  # Field name made lowercase.
    base = models.FloatField(db_column='BASE')  # Field name made lowercase.
    amount = models.FloatField(db_column='AMOUNT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAXLINES'


class Ticketlines(models.Model):
    ticket = models.OneToOneField('Tickets', models.DO_NOTHING, db_column='TICKET', primary_key=True)  # Field name made lowercase.
    line = models.IntegerField(db_column='LINE',blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey(Products, models.DO_NOTHING, db_column='PRODUCT', blank=True, null=True)  # Field name made lowercase.
    attributesetinstance = models.ForeignKey(Attributesetinstance, models.DO_NOTHING, db_column='ATTRIBUTESETINSTANCE_ID', blank=True, null=True)  # Field name made lowercase.
    units = models.FloatField(db_column='UNITS')  # Field name made lowercase.
    price = models.FloatField(db_column='PRICE')  # Field name made lowercase.
    taxid = models.ForeignKey(Taxes, models.DO_NOTHING, db_column='TAXID',blank=True, null=True)  # Field name made lowercase.
    attributes = models.TextField(db_column='ATTRIBUTES', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=255, blank=True, null=True)# Field name made lowercase.
    def __str__(self):
        return f'{self.product.name}'

    class Meta:
        managed = False
        db_table = 'TICKETLINES'
        unique_together = (('ticket', 'line'),)

class TicketlinesInline(admin.TabularInline):
    model = Ticketlines

class Tickets(models.Model):
    id = models.OneToOneField(Receipts, models.DO_NOTHING, db_column='ID', primary_key=True)  
    tickettype = models.IntegerField(db_column='TICKETTYPE')  # Field name made lowercase.
    ticketid = models.IntegerField(db_column='TICKETID',default=0)  # Field name made lowercase.
    person = models.ForeignKey(People, models.DO_NOTHING, db_column='PERSON',default=0)  # Field name made lowercase.
    customer = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CUSTOMER', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.  # Field name made lowercase.
    inlines = [
        TicketlinesInline,
        ]
    def __str__(self):
        return str(self.id.datenew) +"   "+ str(self.person) +"   "+str(self.status)
        pass

    class Meta:
        managed = False
        db_table = 'TICKETS'
        verbose_name_plural='TICKETS'

    #def save(self, *args, **kwargs):
    #    ticketlines = self.Ticketlines.all()
    #   self.value = ticketlines.aggregate(Sum('price'*'units'))['total_price__sum'] if ticketlines.exists() else 0.00
    #  super().save(*args, **kwargs)

class Ticketsnum(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'TICKETSNUM'


class TicketsnumPayment(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'TICKETSNUM_PAYMENT'


class TicketsnumRefund(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'TICKETSNUM_REFUND'
        
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
