from django.shortcuts import render
from .models import Toplantı


# import mysql.connector
# from datetime import datetime
#
# connection = mysql.connector.connect(host="localhost", user="root", password="24541048", database="toplantım")
# mycursor = connection.cursor()
#
# sql = "select * from toplantılarım"
# mycursor.execute(sql)
# try:
#     results = mycursor.fetchall()
#
# except mysql.connector.Error as err:
#     print('hata', err)
# finally:
#     connection.close()

# Create your views here.

def index(request):
    toplantı = Toplantı.objects.all()

    context={
        'toplantı':toplantı
        # 'toplantı':results
    }

    return render(request, 'toplantı/list.html',context)

def detail(request):
    return render(request, 'toplantı/detail.html')

def search(request):
    return render(request, 'toplantı/search.html')

