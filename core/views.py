# from django.contrib.auth import login
from django.shortcuts import redirect, render
from core.models import User,Message
# from core.models import logins
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

def frontpage(request):
    if request.user.is_authenticated:
        return redirect('/viewer',request.path)
    else:
        if request.method=='POST':
            username=request.POST['email']
            password=request.POST['password']
        
            user =authenticate(username=username,password=password)
            print(user)
            if user is not None:
            
                login(request, user)
                return redirect('/',request.path)
            else:
                print('n')

    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['email']
        password= make_password(request.POST['password'])
        if not User.objects.filter(username=username):
            user=User(first_name=first_name,last_name=last_name,username=username,password=password)

            user.save()
            return redirect('/signin',request.path)
    
    return render(request,'signup.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/viewer',request.path)
    else:
        if request.method=='POST':
            username=request.POST['email']
            password=request.POST['password']
        
            user =authenticate(username=username,password=password)
            print(user)
            if user is not None:
            
                login(request, user)
                return redirect('/',request.path)
            else:
                print('n')

    return render(request,'login.html')

def signout(request):
    logout(request)
    return redirect('/signin',request.path)

def contacts(request):
    if not request.user.is_authenticated:
        return redirect('/',request.path)
    else:
        users=User.objects.all()
        context={"users":users}
        return render(request,'contacts.html',context)

def viewer(request):
    if not request.user.is_authenticated:
        return redirect('/',request.path)
    else:
        users=User.objects.all()
        for user in users:
            if user != request.user:
                target= user
                print(target)
                break
            # print(target)
        target=User.objects.get(username=target)
        if request.method=='POST':
            if  "body" in request.POST:
                body=request.POST['body']
                author=request.POST['author']
                target=request.POST['target']

                author=User.objects.get(username=author)
                target=User.objects.get(username=target)

                message =Message(body=body,author=author,target=target)
                message.save()
            else:
               target=request.POST['target']
               target=User.objects.get(username=target)
            #    print(target)
        
        
        
        # print(users[])
        author=request.user
        print(author)
        messagessent=Message.objects.filter(author=author,target=target).order_by('timestamp')
        messagesreceived=Message.objects.filter(target=author,author=target).order_by('timestamp')
        # context={"messagessent":messagessent,"messagesreceived":messagesreceived,"users":users,"active_target":target}
        # messages=Message.objects.filter(author=author,target=target).order_by('timestamp') | Message.objects.filter(target=author,author=target).order_by('timestamp')
        messages=messagessent|messagesreceived
        # print(messages.values)
        context={"messages":messages,"users":users,"active_target":target}

        return render(request,'viewer.html',context)