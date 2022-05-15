from django.shortcuts import render
from django.contrib import messages
from .models import customer,transactions

# Create your views here.
def home(request):
    users = customer.objects.values()
    params = {'users':users}
    return render(request, 'accounts/bank.html',params)

def userView(request,userid):
    user = customer.objects.filter(id=userid)
    alluser = customer.objects.exclude(id=userid)
    myuser = user[0]
    name = myuser.name.split()[0]
    if request.method=="POST":
        sender_id = request.POST.get('sender')
        receiver_id = request.POST.get('receiver')
        amount=request.POST.get('amount')
        print(sender_id,receiver_id)
        if customer.objects.filter(id=sender_id) and customer.objects.filter(id=receiver_id):
            x = customer.objects.get(id=sender_id)
            y = customer.objects.get(id=receiver_id)
            sname=x.name
            rname=y.name
            if int(amount)<=0:
                messages.error(request,"Invalid Amount")
                return render(request,"accounts/user.html",{"user":myuser,"alluser":alluser,"name":name})
            if int(amount)<=x.curr_balance:
                x.curr_balance = int(x.curr_balance)-int(amount)
                y.curr_balance = int(y.curr_balance)+int(amount)
                x.save()
                y.save()
                transfer=transactions(sender_name=sname,receiver_name=rname,sender_id=sender_id,receiver_id=receiver_id,amount=amount,status="Successful")
                transfer.save()
                messages.success(request, "Successfully Transfered")
            else:
                transfer=transactions(sender_name=sname,receiver_name=rname,sender_id=sender_id,receiver_id=receiver_id,amount=amount, status="Failed")
                transfer.save()
                messages.error(request,"Insufficient Balance")
           
    
    

    return render(request,"accounts/user.html",{"user":myuser,"alluser":alluser,"name":name})


def search(request):
    query=request.GET['query']
    if len(query)>78:
        allusers=customer.objects.none()
    else:
        allusername= customer.objects.filter(name__icontains=query)
        alluserid= customer.objects.filter(id__icontains=query)
        allusers=  allusername.union(alluserid)
    if allusers.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'users': allusers, 'query': query}
    return render(request, 'accounts/search.html', params)


def transaction(request):
    tr = transactions.objects.all().order_by('-date')
    genres = ["All","Successful","Failed"]
    if request.method=="POST":
        cat = request.POST.get('genre')
        if cat=="All":
            tr = transactions.objects.all().order_by('-date')
        else:
            tr = transactions.objects.filter(status=cat).order_by('-date')
    
    return render(request, 'accounts/transactions.html', {"tr":tr,"genres":genres})


def about(request):
    return render(request, 'accounts/about.html')