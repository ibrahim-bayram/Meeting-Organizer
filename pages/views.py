from django.shortcuts import render
from django.http import HttpResponse


import mysql.connector
from datetime import datetime

# Create your views here.

def index(request):
    if request.method == 'POST':
        konu = request.POST['konu']
        katılımcılar = request.POST['katılımcılar']
        bsaat = request.POST['bsaat']
        ssaat = request.POST['ssaat']
        tarih = request.POST['tarih']
        kal=1
        connection = mysql.connector.connect(host="localhost", user="root", password="24541048", database="toplantım")
        mycursor = connection.cursor()
        sql = "INSERT INTO toplantı_toplantı(name,description,tarih,isPublished,bsal,ssal) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (konu,katılımcılar,tarih,kal,bsaat,ssaat)
        mycursor.execute(sql, value)
        try:
            connection.commit()
            print(f'{mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            connection.close()


    return render(request, 'pages/index.html')



    # return HttpResponse('<h1>Hello from pages app</h1>')
def about(request):
    if request.method == 'POST':
        if 'düzenle' in request.POST:
            id=request.POST['id']
            konu = request.POST['konu']
            katılımcılar = request.POST['katılımcılar']
            bsaat = request.POST['bsaat']
            ssaat = request.POST['ssaat']
            tarih = request.POST['tarih']
            kal=1
            connection = mysql.connector.connect(host="localhost", user="root", password="24541048", database="toplantım")
            mycursor = connection.cursor()
            sql = "update toplantı_toplantı set name=%s,description=%s,tarih=%s,isPublished=%s,bsal=%s,ssal=%s where id=%s"
            value = (konu,katılımcılar,tarih,kal,bsaat,ssaat,id)
            mycursor.execute(sql, value)
            try:
                connection.commit()
                print(f'{mycursor.rowcount} tane kayıt eklendi.')
            except mysql.connector.Error as err:
                print('hata:', err)
            finally:
                connection.close()
        elif 'sil' in request.POST:
            id = request.POST['id']
            connection = mysql.connector.connect(host="localhost", user="root", password="24541048",database="toplantım")
            mycursor = connection.cursor()
            sql = "delete from toplantı_toplantı  where id=%s"
            value = (id,)
            mycursor.execute(sql, value)
            try:
                connection.commit()
                print(f'{mycursor.rowcount} tane kayıt silindi')
            except mysql.connector.Error as err:
                print('hata:', err)
            finally:
                connection.close()
    return render(request, 'pages/about.html')