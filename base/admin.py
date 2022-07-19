from re import A
from django.contrib import admin
from base.models import Customer, Ticket ,Countrie, Airline_Company, Flight, User_Role, Admin

# Register your models here.
admin.site.register (Admin),

class Ticket_Admin(admin.ModelAdmin):
    #ALC= AIRLINE COMPANY
    model = Ticket
    list_display = ['_id', 'flight','customer'] #Indicates which fields will show

    def get_name(self, obj):
        return {
            obj.airline_companie.flight,
            obj.airline_companie.customer,}
    get_name.short_description = 'Flight'
    get_name.short_description = 'Customer' #Renames column head

admin.site.register(Ticket, Ticket_Admin)


class Customer_Admin(admin.ModelAdmin):
    #ALC= AIRLINE COMPANY
    model = Customer
    list_display = ['_id', 'f_name','l_name',
    'address','phone_No','credit_Card','user'] #Indicates which fields will show

    def get_name(self, obj):
        return {
            obj.airline_companie.f_name,
            obj.airline_companie.l_name,
            obj.airline_companie.address,
            obj.airline_companie.phone_No,
            obj.airline_companie.credit_Card,
            obj.airline_companie.user,}
    get_name.short_description = 'First Name'
    get_name.short_description = 'Last Name' 
    get_name.short_description = 'Address' 
    get_name.short_description = 'Phone Number'
    get_name.short_description = 'Credit Card' 
    get_name.short_description = 'User'  #Renames column head

admin.site.register(Customer, Customer_Admin)


class Flight_Admin(admin.ModelAdmin):
    #ALC= AIRLINE COMPANY
    model = Flight
    list_display = [
        '_id', 'airline_company',
        'origin_country','destination_country',
        'departure','landing_time'] #Indicates which fields will show

    def get_name(self, obj):
        return {
            obj.airline_companie.airline_company,
            obj.airline_companie.origin_country,
            obj.airline_companie.destination_country,
            obj.airline_companie.departure,
            obj.airline_companie.landing_time,}
    get_name.short_description = 'Airline Company'
    get_name.short_description = 'Origin Country' 
    get_name.short_description = 'Destination Country' 
    get_name.short_description = 'Departure'
    get_name.short_description = 'Landing Time'  #Renames column head

admin.site.register(Flight, Flight_Admin)


class ALC_Admin(admin.ModelAdmin):
    #ALC= AIRLINE COMPANY
    model = Airline_Company
    list_display = ['_id', 'name','country','user'] #Indicates which fields will show

    def get_name(self, obj):
        return {
            obj.airline_companie.name,
            obj.airline_companie.country,
            obj.airline_companie.user}
    get_name.short_description = 'Airline Company'
    get_name.short_description = 'Country' 
    get_name.short_description = 'User' #Renames column head

admin.site.register(Airline_Company, ALC_Admin)


class RolesAdmin(admin.ModelAdmin):
    model = User_Role
    list_display = ['id','role_name'] #Indicates which fields will show

    def get_name(self, obj):
        return obj.user_role.role_name
    get_name.short_description = 'User Role'  #Renames column head

admin.site.register(User_Role, RolesAdmin)


class CountrieAdmin(admin.ModelAdmin):
    model = Countrie
    list_display = ['_id', 'name'] #Indicates which fields will show

    def get_name(self, obj):
        return obj.countrie.name
    get_name.short_description = 'Countrie Name'  #Renames column head

admin.site.register(Countrie, CountrieAdmin)