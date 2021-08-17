# from The_Grand import user_transactions
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
# from The_Grand.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth import logout as auth_logout
import requests
from .models import reviews, rooms,user_booking,restaurant
from django.urls import reverse
from datetime import date, datetime

# Create your views here.
def home_view(request):
    # return HttpResponse("<h1>Hi</h1>")
    return render(request,"user_transactions/index.html")

def home(request):
    # request.session.clear()
    auth_logout(request)
    # return HttpResponse("<h1>Hi</h1>")
    return render(request,"user_transactions/home.html")
    

# def contact(request):
#     return render(request,"user_transactions/contact.html")

def booking(request):
    return render(request,'user_transactions/booking.html')

def register(request):
    return render(request,'user_transactions/register.html')

#Email sending----> send_mail() method is imported from django.core.mail module
def contact(request):
    # sub = forms.Subscribe()
    if request.method == 'POST':
        # sub = forms.Subscribe(request.POST)
        name1=request.POST['Name']
        name=name1.capitalize()
        subject = 'Message from ' + name
        sender=request.POST['Email']
        message=request.POST['Message']
        message = 'Hi\n\n' +name +' contacted Hotel The Grand for the mentioned query: \n\n '+ 'Query- \n '+ message + '\n\nThanks\n'+name+'\n'+sender
        # recepient = ['hnagpal0209@gmail.com'] #str(sub['Email'].value())
        recepient = ['testdjangosmtp0@gmail.com',sender] 
        context={
        #    'recepient':recepient,
           'name':name,
           'subject':subject,
           'sender':sender,
           'message':message,
           'date': datetime.now
        }
        print(recepient)
        print('sender',sender)
        send_mail(subject, 
            message, sender, recepient, fail_silently = False)
        return render(request, 'user_transactions/success.html', {'context': context})
    return render(request,"user_transactions/contact.html")

#Map Configuration

def default_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, "user_transactions/location.html", 
                  { 'mapbox_access_token': mapbox_access_token })

#reviews submit
def comments(request):
    
    if request.method == 'POST':
        comment=request.POST['comment']
        user=request.POST['username']
        obj=reviews(comment = comment,user=user)
        obj.save()
        print('Inside POST')
        comments=reviews.objects.all()[:10:-1]
        context={'comm':comments}
        # redirect('user_transactions/reviews')
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button or refreshes the browser
        return HttpResponseRedirect(reverse('reviews'))
        # return render(request,"user_transactions/reviews.html",context)
        
    else:
            
        comments=reviews.objects.all()[:10:-1]
        context={'comm':comments}
        print('GET',context)
        # return render(request,"user_transactions/reviews.html",context)
    return render(request,"user_transactions/reviews.html",context)

def location_detail(request):
    return render(request,'user_transactions/location_detail.html')
    
def news(request):
    import json

    # url = "https://news-article-data-extract-and-summarization1.p.rapidapi.com/extract/v2/"

    # querystring = {"url":"https://www.nytimes.com/live/2020/12/14/world/covid-19-coronavirus","useCache":"true"}

    # headers = {
    #     'x-rapidapi-key': "241b81ca7cmsha9e7435afa4ba4dp17840djsnfe6083f8f2b2",
    #     'x-rapidapi-host': "news-article-data-extract-and-summarization1.p.rapidapi.com"
    #     }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    # data = response.text
    # print(type(data))

    # data_dict = json.loads(data)
    # print(type(data_dict))
    # print(data_dict.keys())
    # print(data_dict['title'],data_dict['description'],'url-',data_dict['url'],'image-',data_dict['mainImage'])
    # context={
    #     'title':data_dict['title'],
    #     'description':data_dict['description'],
    #     'url':data_dict['url'],
    #     'image':data_dict['mainImage']
    # }
    url="https://newsapi.org/v2/top-headlines?country=us&apiKey=c2b313f1b4f24f50b6833dfdf7fc430d"
    r = requests.get(url=url) 
    data = r.json()
    if data["status"] != "ok":
        # return JsonResponse({"success":False})
        # return HttpResponse("<h1>Request Failed</h1>")
        print('Request failed')
    data = data["articles"]
    context = {
        "success": True,
        "data": [],
        "search": "top"
    }
# seprating the necessary data
    for i in data:
        context["data"].append({
            "title": i["title"],
            "description":  "" if i["description"] is None else i["description"],
            "url": i["url"],
            "image": "" if i["urlToImage"] is None else i["urlToImage"],
            "publishedat": i["publishedAt"]
        })
    return render(request,'user_transactions/news.html',context)

def booking_detail(request):
    
    if request.method=='POST':
        
        user=request.POST['user']
        date1=request.POST['date1']
        date2=request.POST['date2']
        room_price=request.POST['item_id']
        no_rooms=request.POST['no_rooms']
        sender=request.POST['email1']
        # room_price=rooms.objects.get(id=room_id)
        # print('room_price',room_price)
        print('date1',date1)
        print('user',user)
        print('date2',date2)
        print('room_price',type(room_price))
        print('no_rooms',type(no_rooms))
        print('email',sender)
        start_date = datetime.strptime(date1, "%Y-%m-%d")
        end_date = datetime.strptime(date2, "%Y-%m-%d")
        days=(end_date-start_date).days
        print ((end_date-start_date).days)
        total_price=int(no_rooms)*int(days)*int(room_price)
        obj=user_booking(price=room_price,no_rooms=no_rooms,days=days,total_price=total_price,user=user,email=sender,date1=date1,date2=date2)
        obj.save()
        # diff=date1-date2
        # print(diff)

        # for i in span:
        #     print(i)
        print('POST called')
        subject='Hotel The Grand - Booking confirm'
        # message='Your Booking has been confirmed from date' + date1 +'to '+date2 + 'Booking details below \n\n'+'Number of rooms\n '+no_rooms+'\nPrice per room'+room_price+'\nTotal stay'+days+'\nTotal price '+total_price
        message='Hi Dear,\n\n' + 'Your Booking has been confirmed from date ' + date1 + ' to ' + date2 + '\n\nBooking details : \n'+'Number of rooms - ' + no_rooms + '\nPrice per room - ' + room_price + '\nTotal stay - ' + str(days) + '\nTotal Price - ' + str(total_price) + '\n\nThanks\nHotel The Grand\nAdmin Team'
        context={
        #    'recepient':recepient,
           'name':user,
           'subject':subject,
           'sender':sender,
           'message':message,
           'date': datetime.now
        }
        recepient = ['testdjangosmtp0@gmail.com',sender] 
        send_mail(subject,message, sender, recepient, fail_silently = False)
        return render (request,'user_transactions/booking_confirm.html', {'context': context})
    #     # return HttpResponseRedirect(reverse('booking_detail'))
        # return render (request,'user_transactions/booking_confirm.html')
        # return HttpResponse('Hello %s' % span)
    else:
        print('GET called')
        room1=rooms.objects.all()
        context1={'room':room1}
        return render(request,'user_transactions/booking_detail.html',context1)

def booking_confirm(request):
    
    return render (request,'user_transactions/booking_confirm.html')

def event(request):
    return render(request,'user_transactions/event.html')

from django.http import JsonResponse 
def booking_view(request):

    if request.method=='GET':
            
        detail=user_booking.objects.all()
        context1={'detail':detail}
        # print('details',detail)
        # print('email',sender)
        return render(request,'user_transactions/booking_view.html',context1)
    # return render(request,'user_transactions/booking_view.html')
    else:
        b_id= request.POST['booking']
        email = request.POST['email1']
        date1 = request.POST['date1']
        date2 = request.POST['date2']
        print(email,date1,date2)
            
        user_booking.objects.filter(
            # email=email,
            id=b_id
            
        ).delete()
        
        return HttpResponseRedirect(reverse('booking_view'))
    

    #PDF generation
from django.template.loader import get_template
from xhtml2pdf import pisa
def pdf_generation(request):
    template_path = 'user_transactions/receipt.html'
    detail=user_booking.objects.all()
    context1={'detail':detail}
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download use attachment
    response['Content-Disposition'] = 'attachment; filename="Receipt.pdf"'
    #if display
    # response['Content-Disposition'] = 'filename="Receipt.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context1)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def restaurant_view(request):
    if request.method=='GET':
        try:
            rest=restaurant.objects.latest('id')
            context={'rest': rest}
            return render(request,'user_transactions/restaurant.html',context)
        except:
            return render(request,'user_transactions/restaurant.html')
    else:
        print("POST CALLED")
        user=request.POST['user']
        input1=request.POST['inp1']
        input2=request.POST['inp2']
        input3=request.POST['inp3']
        quantity=int(input1)+int(input2)+int(input3)
        
        print(input1,input2,input3,user)
        sum=(int(input1)*200) + (int(input2) * 300) + (int(input3) * 250)
        print(sum)
        obj=restaurant(amount=sum,user=user,quantity=quantity)
        obj.save()
    # return render(request,'user_transactions/restaurant.html')
    return HttpResponseRedirect(reverse('restaurant'))

def about(request):
    return render(request,'user_transactions/about.html')