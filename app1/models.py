from django.db import models
import bcrypt
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['fname']) < 2 :
            errors['first']= 'First name should be more than 2 characters'
        if len(postData['lname']) < 2 :
            errors['last']= 'Last name should be more than 2 characters'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']= 'Invalid Email Address'
        if len(postData['password']) < 8:
            errors['password']= 'Please Password must be at least 8 characters.'
        if postData['password'] != postData['confirm']:
            errors['confirm']= 'Password not match'
        return errors



class User(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    email=models.CharField(max_length=255)
    password=models.TextField()
    dob=models.DateTimeField()
    gender=models.CharField(max_length=7)
    avatar=models.ImageField(upload_to='image',default='image/default.jpg',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= UserManager()

class Post(models.Model):
    desc=models.TextField()
    posted_by=models.ForeignKey(User,related_name='posts',on_delete = models.CASCADE)
    liked_by=models.ManyToManyField(User, related_name='post_likes')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    desc=models.TextField()
    commented_by=models.ForeignKey(User,related_name='user_comments',on_delete = models.CASCADE)
    related_post=models.ForeignKey(Post,related_name='post_comments',on_delete = models.CASCADE)
    liked_by=models.ManyToManyField(User, related_name='comment_likes') #not used field, but i'll used in feature
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Message(models.Model):
    content=models.TextField()
    sent_by=models.ManyToManyField(User,related_name='message_sent')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class Image(models.Model):
    uploaded_by=models.ForeignKey(User,related_name='photos',on_delete = models.CASCADE)
    photo=models.ImageField(upload_to='image',null=True,blank=True)
    related_post=models.ForeignKey(Post,related_name='post_photos',on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Friend(models.Model):
    user=models.ForeignKey(User,related_name='this_user',on_delete = models.CASCADE)
    friends=models.ManyToManyField(User, related_name='allfriends')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Request(models.Model):
    user=models.ForeignKey(User,related_name='requests',on_delete = models.CASCADE)
    user_request=models.ManyToManyField(User, related_name='friend_requests')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Note(models.Model):
    reciever=models.ForeignKey(User,related_name='user_reciever',on_delete = models.CASCADE)
    sender=models.ManyToManyField(User,related_name='user_sender')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)