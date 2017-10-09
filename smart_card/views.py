from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
import random, string
import pyqrcode

def index(request):
    return render(request, 'smart_card/index.html', context=None)

def register(request):
    context = {
        'sta' : State.objects.all()
    }

    return render(request, 'smart_card/register.html', context)

def details(request):
    return render(request, 'smart_card/details.html', context=None)

def get_districts(request):
    state_id = request.GET.get('state_id', None)
    data = District.objects.filter(state_id = str(state_id))
    result = []
    for row in data:
        info = {}
        info['district_id'] = row.district_id
        info['district_name'] = row.district_name
        result.append(info)
    return JsonResponse(result, safe = False)

def get_tehsils(request):
    country_id = request.GET.get('country_id', None)
    state_id = request.GET.get('state_id', None)
    district_id = request.GET.get('district_id', None)
    parent_id = str(country_id) + str(state_id) + str(district_id)
    data = Tehsil.objects.filter(district_id = parent_id)
    result = []
    for row in data:
        info = {}
        info['tehsil_id'] = row.tehsil_id
        info['tehsil_name'] = row.tehsil_name
        result.append(info)
    return JsonResponse(result, safe = False)

def get_gram_panchayats(request):
    country_id = request.GET.get('country_id', None)
    state_id = request.GET.get('state_id', None)
    district_id = request.GET.get('district_id', None)
    tehsil_id = request.GET.get('tehsil_id', None)
    parent_id = str(country_id) + str(state_id) + str(district_id) + str(tehsil_id)
    data = GramPanchayat.objects.filter(tehsil_id = parent_id)
    result = []
    for row in data:
        info = {}
        info['gram_panchayat_id'] = row.gram_panchayat_id
        info['gram_panchayat_name'] = row.gram_panchayat_name
        result.append(info)
    return JsonResponse(result, safe = False)

def next_string(current):
    l = [str(i) for i in range(0, 10)]
    l = l + list(string.ascii_uppercase)
    s = list(current)
    i = len(current) - 1
    ch = l[(l.index(s[i]) + 1) % 36]
    while i != -1:
        s[i] = ch
        if ch != '0':
            break
        i = i - 1
        ch = l[(l.index(s[i]) + 1) % 36]
    return ''.join(s)

def do_register(request):
    person = Person()
    person.first_name = request.POST.get("fname", None)
    person.middle_name = request.POST.get("mname", None)
    person.last_name = request.POST.get("lname", None)
    person.gender = request.POST.get('gender', None)
    person.fathers_name = request.POST.get('faname', None)
    person.mothers_name = request.POST.get('moname', None)
    person.dob = request.POST.get('dob', None)
    person.phone_number = request.POST.get('cnumber', None)
    person.email = request.POST.get('email')
    person.pan = request.POST.get('Pan', None)
    person.housenum = request.POST.get('hnum', None)
    person.streetnum = request.POST.get('sname', None)
    person.postalnum = request.POST.get('pnum', None)
    country_id = '01'
    state_id = str(request.POST.get('state', None))
    district_id = str(request.POST.get('district', None))
    tehsil_id = str(request.POST.get('tehsil', None))
    gram_panchayat_id = str(request.POST.get('gram_panchayat', None))
    person.gram_panchayat_id = country_id + state_id + district_id + tehsil_id + gram_panchayat_id
    q = Person.objects.raw('SELECT MAX(person_id), id FROM smart_card_person WHERE gram_panchayat_id="' + person.gram_panchayat_id + '"')
    max_id = ''
    for row in q:
        max_id = row.person_id
    person.person_id = next_string(max_id)
    person.net_person_id = person.gram_panchayat_id + person.person_id
    person.password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    person.save()
    big_code = pyqrcode.create(str(person.gram_panchayat_id) + str(person.person_id), error='L', mode='binary')
    big_code.png('smart_card/static/smart_card/images/qrcode.png', scale=2, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    context = {
        'ID': person.gram_panchayat_id + person.person_id,
        'name': person.first_name + ' ' + person.middle_name + ' ' + person.last_name,
        'fathers_name': person.fathers_name,
        'gender': person.gender,
        'postalnum': person.postalnum,
        'password': person.password,
        'dob': person.dob
    }
    return render(request, 'smart_card/ID.html', context)

def view_details(request):
    person = Person()
    country = Country()
    state = State()
    district = District()
    tehsil = Tehsil()
    grampanch = GramPanchayat()
    person.country = str(request.POST.get("country", None))
    person.state = str(request.POST.get("state", None))
    person.district = str(request.POST.get("district", None))
    person.tehsil = str(request.POST.get("tehsil", None))
    person.gram = str(request.POST.get("gram", None))
    person.personal_id = str(request.POST.get("personal_id", None))

    person.password = str(request.POST.get("passwd", None))
    person.net_id = person.country + person.state + person.district + person.tehsil + person.gram + person.personal_id
    #q = Person.objects.raw('SELECT first_name FROM smart_card_person WHERE gram_panchayat_id ="' + person.gram_id + '" AND person_id="' + person.personal_id + '"')
    q = Person.objects.filter(net_person_id= person.net_id).values('first_name', 'last_name', 'password', 'fathers_name', 'mothers_name', 'gender', 'email', 'pan', 'phone_number', 'housenum', 'streetnum', 'postalnum', 'dob')
    per = Person()
    for p in q:
        per = p
    if per['password'] != person.password:
        return HttpResponse("Wrong password loser!")
    con_q = Country.objects.filter(country_id=person.country).values('country_name')
    sta_q = State.objects.filter(state_id= person.state).values('state_name')
    dist_q = District.objects.filter(district_id=person.district, state_id=person.country+person.state).values('district_name')
    teh_q = Tehsil.objects.filter(tehsil_id=person.tehsil, district_id=person.country+person.state+person.district).values('tehsil_name')
    gram_q = GramPanchayat.objects.filter(gram_panchayat_id=person.gram, tehsil_id=person.country+person.state+person.district+person.tehsil).values('gram_panchayat_name')
    context = {
        'per' : Person.objects.all(),
        'id': person.country + person.state + person.district + person.tehsil + person.personal_id,
        'tehsil_id': person.country + person.state + person.district + person.tehsil,
        'only_personal': person.personal_id,
        'query' : q,
        'country' : con_q,
        'state' : sta_q,
        'district': dist_q,
        'tehsil' : teh_q,
        'gram' : gram_q
    }
    return render(request, 'smart_card/view_details.html', context)
