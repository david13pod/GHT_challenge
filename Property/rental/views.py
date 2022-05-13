from django.shortcuts import render
from django.http import JsonResponse
from .models import Rental, Reservation
from http.client import HTTPResponse
# Create your views here.

# def reservations_table():
def reservations_table(request):
    if request.method =='GET':
        reservations= Reservation.objects.all()
        context={"Rental_name":[], "ID":[], "Checkin":[], "Checkout":[], "Previous reservation ID":[]}

        for index in range(0,len(reservations)):
            context["ID"].append(reservations[index].reserve_id)
            context["Checkin"].append(reservations[index].checkin_date)
            context["Checkout"].append(reservations[index].checkout_date)
            if str(reservations[index].rental) in context["Rental_name"] and index > 0:
                # print(1,reservations[index].rental)
                # print(2, context["Rental_name"])
                found =False
                for i in reversed(range(len(context["Rental_name"]))):
                    if found:
                        break
                    if context["Rental_name"][i] == str(reservations[index].rental) :
                        context["Previous reservation ID"].append(context["ID"][i])
                        found = True
            else:
                context["Previous reservation ID"].append("-")
            
            context["Rental_name"].append(str(reservations[index].rental))
            
        # return HTTPResponse(json.dumps(context),content_type='application/json')
        return JsonResponse(context,status=201)




