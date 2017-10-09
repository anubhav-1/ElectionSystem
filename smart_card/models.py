from django.db import models

class Country(models.Model):
    country_id = models.CharField(max_length=2)
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_id + ' ' + self.country_name

class State(models.Model):
    country_id = models.CharField(max_length=2) #CC
    state_id = models.CharField(max_length=2)
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_id + ' ' + self.state_id + ' ' + self.state_name

class District(models.Model):
    state_id = models.CharField(max_length = 4) #CCSS
    district_id = models.CharField(max_length = 2)
    district_name = models.CharField(max_length = 150)

    def __str__(self):
        return self.state_id + ' ' + self.district_id + ' ' + self.district_name

class Tehsil(models.Model):
    district_id = models.CharField(max_length = 6) #CCSSDD
    tehsil_id = models.CharField(max_length = 2)
    tehsil_name = models.CharField(max_length = 150)

    def __str__(self):
        return self.district_id + ' ' + self.tehsil_id + ' ' + self.tehsil_name

class GramPanchayat(models.Model):
    tehsil_id = models.CharField(max_length = 8) #CCSSDDTT
    gram_panchayat_id = models.CharField(max_length = 2)
    gram_panchayat_name = models.CharField(max_length = 150)

    def __str__(self):
        return self.tehsil_id + ' ' + self.gram_panchayat_id + ' ' + self.gram_panchayat_name

class Person(models.Model):
    gram_panchayat_id = models.CharField(max_length = 10)
    person_id = models.CharField(max_length = 5)
    net_person_id = models.CharField(max_length=15)
    password = models.CharField(max_length = 8)
    first_name = models.CharField(max_length = 20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length = 20)
    fathers_name = models.CharField(max_length = 50)
    mothers_name = models.CharField(max_length=50)
    dob = models.CharField(max_length=15)
    email= models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    pan = models.CharField(max_length=11)
    phone_number = models.CharField(max_length = 10)
    housenum = models.CharField(max_length = 1000)
    streetnum = models.CharField(max_length=100)
    postalnum = models.CharField(max_length=100)

    def __str__(self):
        return self.gram_panchayat_id + ' ' + self.person_id + ' ' + self.first_name + ' ' + self.last_name
