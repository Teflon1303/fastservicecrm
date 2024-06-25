import django.contrib.auth
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Company, Workshop, Order, StatusOrder, CustomerOrder, TypeOrder
from django.db.models import Sum

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from .serializes import StatusOrderSerializer


def user_login(request):
    context = {
        'text_login': 'вход'
    }
    if request.POST:
        print("post прошел!")
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user=user)
            print(f'Пользователь: {user} авторизован.')
            filterCompany = Company.objects.filter(user=request.user)
            context = {
                'userName': f'{user.first_name} {user.last_name}!',
                'user': user.username,
                'company': Company.objects.filter(user=user),
                'WorkShop': Workshop.objects.filter(company=filterCompany[0].id)
                # 'orders':
            }
            context['sumOrders'] = sum_orders()
            context['countOrders'] = order_count()
            context['averageCheck'] = average_check(sum_orders(),order_count())
            print(context)

            # return render(request, "index.html", context)
            return redirect('index')
    return render(request, "login.html", context)
# Create your views here.


def index(request):
    if request.user.is_authenticated == True:
        user = request.user
        print(f'Пользователь: {user} авторизован.')
        filterCompany = Company.objects.filter(user=request.user)
        fiterWorkShop = Workshop.objects.filter(company=filterCompany[0].id)
        print(fiterWorkShop)
        context = {
            'userName': f'{user.first_name} {user.last_name}!',
            'user': user.username,
            'company': Company.objects.filter(user=user),
            'WorkShop': Workshop.objects.filter(company=filterCompany[0].id),
            'Orders1': Order.objects.filter(workShop=fiterWorkShop[0].id),
            'Orders2': Order.objects.filter(workShop=fiterWorkShop[1].id),
            'colorStatus': StatusOrder.objects.all(),
            'customer': CustomerOrder.objects.all()
        }

        print()

        context['sumOrders'] = sum_orders()
        context['countOrders'] = order_count()
        context['averageCheck'] = average_check(sum_orders(), order_count())
        print(context)
        print()
        # filterCompany = Company.objects.filter(user=request.user)
        # context = {
        #     'user': f'{request.user.first_name} {request.user.last_name}',
        #     'text_login': 'выход',
        #     'company': Company.objects.filter(user=request.user),
        #     'WorkShop': Workshop.objects.filter(company=filterCompany[0].id)
        # }
        return render(request, "index.html", context)
    else:
        context = {
            'text_login': 'вход'
        }
        return render(request, "login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def sum_orders():
    orders_sum = Order.objects.aggregate(Sum('estimatedСost'))
    print(f'Сумма заказазов:{orders_sum.get('estimatedСost__sum')}')
    return orders_sum.get('estimatedСost__sum')


def order_count():
    orders_count = Order.objects.all().count()
    print(f'Колличество заказов:{orders_count}')
    return orders_count


def average_check(sum, count):
    return round((sum / count), 2)

def workShop (request):
    user = request.user
    print(f'Пользователь: {user} авторизован.')
    filterCompany = Company.objects.filter(user=request.user)
    context = {
        'userName': f'{user.first_name} {user.last_name}!',
        'user': user.username,
        'company': Company.objects.filter(user=user),
        'WorkShop': Workshop.objects.filter(company=filterCompany[0].id),

    }
    context['sumOrders'] = sum_orders()
    context['countOrders'] = order_count()
    context['averageCheck'] = average_check(sum_orders(), order_count())
    print(context)
    return render(request, "workshop.html", context)





def home(request):
    return render(request,"users/home.html")



class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def OrderThis(request, OrderID):
    print(OrderID)
    context = {
        'order': Order.objects.filter(id=OrderID),
        'colorStatus': StatusOrder.objects.all(),
        'typeOrder': TypeOrder.objects.all(),
        'сustomerOrder': CustomerOrder.objects.all()
    }
    print(Order.objects.filter(id=OrderID))
    print(StatusOrder.objects.all())


    return render(request, "order.html", context)



def printReportOrder (request, OrderID):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setFont("Helvetica", 20)
    p.drawString(0,0,f"Oder #{OrderID}")
    p.drawString(0, 0, f"Статус: {Order.status}")

    # Close the PDF object cleanly, and we're done.

    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="order.pdf")


class StatusOrderGet(APIView):
    def get(self, request):
        courses = StatusOrder.objects.all()
        serializer = StatusOrderSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)