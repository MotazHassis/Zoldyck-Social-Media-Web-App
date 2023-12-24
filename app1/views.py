from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.utils import timezone



def login_registration(request):

    return render(request,'index.html')

def main(request):
    if 'user_id' in request.session:
        list=[]
        this_user=User.objects.get(id=request.session['user_id'])
        for friend in this_user.this_user.all():
            for all in friend.friends.all():
                list.append(all.id) 
        allphoto1=Image.objects.all()

        context={
            'user':this_user,
            'allrequests':this_user.requests.all(),
            'allfriends':this_user.this_user.all(),
            'allpost':Post.objects.all(),
            'allphoto':allphoto1.order_by('-created_at'),
            'alluser':User.objects.all(),
            'user_friends_list':list,
            'allnote':this_user.user_reciever.all(),
            'currentDate':timezone.now(),
        }
        
        return render(request,'feed.html',context)
    
    else:
        return redirect ('/')


def registre_proccess(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        if 'first' in errors:
            request.session['first']=errors['first']
        if 'last' in errors:
            request.session['last']=errors['last']
        if 'email' in errors:
            request.session['email']=errors['email']
        if 'password' in errors:
            request.session['password']=errors['password']
        if 'confirm' in errors:
            request.session['confirm']=errors['confirm']
        return redirect('/')
    else:
        hash1= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        registered_user = User.objects.create(
            first=request.POST['fname'],
            last=request.POST['lname'],
            email=request.POST['email'],
            password=hash1,
            dob=request.POST['dob'],
            gender=request.POST['gender']
            )
        messages.success(request, "Registered successfully")
        request.session['user_id']=registered_user.id
        request.session['user_name']=registered_user.first
        this_friend=Friend.objects.create(
        user=registered_user
        )
        this_request=Request.objects.create(
            user=registered_user
        )
        this_notify=Note.objects.create(
            reciever=registered_user
        )
        return redirect('/FLEXBOOK')

def login_proccess(request):
    user = User.objects.filter(email=request.POST['lemail'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['lpassword'].encode(), logged_user.password.encode()):
                request.session['user_id']=logged_user.id
                request.session['user_name']=logged_user.first
                return redirect('/FLEXBOOK')
        else:
            err={}
            err['authentication']= 'Invalid authentication'
            request.session['authentication']=err['authentication']
            print(request.session['authentication'])
            return redirect ('/')
            
    else:
        err={}
        err['authentication']= 'Invalid authentication'
        request.session['authentication']=err['authentication']
        print(request.session['authentication'])
        return redirect ('/')

def post(request):
    this_user=User.objects.get(id=request.session['user_id'])
    this_post=Post.objects.create(
        desc=request.POST['post_desc'],
        posted_by=this_user
    )
    if len(request.FILES) != 0:
        filepath = request.FILES.get('img', False)
        this_image=Image.objects.create(
        photo=filepath,
        uploaded_by=this_user,
        related_post=this_post
    )
    
        
    return redirect('/FLEXBOOK')
    

def comment(request,id):
    this_user=User.objects.get(id=request.session['user_id'])
    this_post=Post.objects.get(id=int(id))
    this_comment=Comment.objects.create(
        desc=request.POST['comment_desc'],
        commented_by=this_user,
        related_post=this_post,
        )
    context={
        'post':this_post,
        'user':this_user
    }
    
    return render(request,'comment.html',context)


def friend_request_update(request):
    
    sender_user=User.objects.get(id=request.session['user_id'])
    
    context={
        'allnote':sender_user.user_reciever.all(),
        'allrequests':sender_user.requests.all(),
        'allfriends':sender_user.this_user.all(),

    }
    return render(request,'friends_note.html',context)

def message_continuos_update(request):
    
    sender_user=User.objects.get(id=request.session['user_id'])
    
    context={
        'allnote':sender_user.user_reciever.all(),
        'allrequests':sender_user.requests.all(),
        'allfriends':sender_user.this_user.all(),

    }
    return render(request,'message_updates.html',context)


def edit_post(request,id):
    this_post=Post.objects.get(id=int(id))
    this_post.desc=request.POST['post_desc']
    this_post.save()
    print('hello')
    return redirect('/FLEXBOOK')

def count_comment(request,id):
    this_post=Post.objects.get(id=int(id))
    context={
        'post':this_post,
    }
    return render(request,'comments_count.html',context)

def change(request):
    return render(request,'change.html')

def update(request):
    this_user=User.objects.get(id=request.session['user_id'])
    this_user.avatar=request.FILES['avatar']
    this_user.save()
    return redirect('/FLEXBOOK')

def like(request,id):
    this_user=User.objects.get(id=request.session['user_id'])
    this_post=Post.objects.get(id=int(id))
    this_post.liked_by.add(this_user)
    context={
        'this_post':Post.objects.get(id=int(id))
    }
    return render(request,'ajax.html',context)
    # return redirect('/FLEXBOOK')

def control(request):
    if 'user_id' in request.session:
        context={
            'account':User.objects.all(),
            'admin':User.objects.get(id=request.session['user_id'])
        }
        return render(request,'control.html',context)
    else:
        return redirect ('/')

def control_del(request,id):
    this_user=User.objects.get(id=int(id))
    this_user.delete()
    return redirect('/control')

def send_request(request,id):
    request_user=User.objects.get(id=int(id))
    add_user=User.objects.get(id=request.session['user_id'])
    this_request=Request.objects.get(
        user=request_user, 
        )
    this_request.user_request.add(add_user)
    return redirect('/FLEXBOOK')

def accept_request(request,id):
    request_user=User.objects.get(id=request.session['user_id'])
    add_user=User.objects.get(id=int(id))
    this_friend=Friend.objects.get(
        user=request_user, 
        )
    this_friend.friends.add(add_user)
    this_friend=Friend.objects.get(
        user=add_user, 
        )
    this_friend.friends.add(request_user)
    this_request=Request.objects.get(
        user=request_user, 
        )
    this_request.user_request.remove(add_user)
    return redirect('/FLEXBOOK')

def delete_post(request,id):
    this_post=Post.objects.get(id=int(id))
    this_post.delete()
    return redirect('/FLEXBOOK')

def delete_comment(request,id):
    this_comment=Comment.objects.get(id=int(id))
    this_comment.delete()
    return redirect('/FLEXBOOK')

def send_message(request,id):
    sender_user=User.objects.get(id=request.session['user_id'])
    reciver_user=User.objects.get(id=int(id))
    this_message=Message.objects.create(
        content="["+sender_user.first +'] :'+request.POST['message_content'],
    )
    # this_notify_sender=Note.objects.get(sender=reciver_user)
    this_notify=Note.objects.get(reciever=reciver_user)
    this_notify.updated_at= timezone.now()
    this_notify.save()
    this_notify.sender.add(sender_user)
    this_message.sent_by.add(sender_user)
    this_message.sent_by.add(reciver_user)
    return redirect('/message/'+str(id))

def message_page(request,id):
    
    sender_user=User.objects.get(id=request.session['user_id'])
    reciver_user=User.objects.get(id=int(id))
    this_notify=Note.objects.get(reciever=sender_user)
    this_notify.sender.remove(reciver_user)
    this_message=Message.objects.filter(sent_by=sender_user)
    this_message_re=this_message.filter(sent_by=reciver_user)
    ready_message_sender=this_message_re.order_by('created_at')
    context={
        'sender':sender_user,
        'reciver':reciver_user,
        'message_content_sender':ready_message_sender,
        'allnote':sender_user.user_reciever.all(),
        'allrequests':sender_user.requests.all(),
        'allfriends':sender_user.this_user.all(),

    }
    return render(request,'message.html',context)

def text_message_update(request,id):
    
    
    sender_user=User.objects.get(id=request.session['user_id'])
    reciver_user=User.objects.get(id=int(id))
    this_notify=Note.objects.get(reciever=sender_user)
    this_notify.sender.remove(reciver_user)
    this_message=Message.objects.filter(sent_by=sender_user)
    this_message_re=this_message.filter(sent_by=reciver_user)
    ready_message_sender=this_message_re.order_by('created_at')
    context={
        'sender':sender_user,
        'reciver':reciver_user,
        'message_content_sender':ready_message_sender,
        'allnote':sender_user.user_reciever.all(),
        'allrequests':sender_user.requests.all(),
        'allfriends':sender_user.this_user.all(),

    }
    return render(request,'text_message_update.html',context)

def check(request):
    messages.error(request, 'wrong')
    messages.success(request, "successfully")
    return render(request,'ajax.html') 

def logout(request):
    request.session.flush()
    return redirect ('/')

# def upload_file(request):
#     context={
#         'alluser':User.objects.all()
#     }
        
#     return render(request,'index.html',context)

# def porcces(request):
#     this_user=User.objects.create(
#         name=request.POST['name'],
#         desc=request.POST['desc'],
#         photo=request.FILES['img']
#     )
#     return redirect('/')