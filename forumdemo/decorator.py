#encoding:utf8
from functools import wraps
from flask import Flask, render_template,request,redirect,url_for,session
#限制登录的装饰器
def login_required(func):
   @wraps(func)
   def wrapper(*args,**kwargs):
       if session.get('user_id'):
          return func(*args,**kwargs)
       else:
           return redirect(url_for('login'))
   return wrapper