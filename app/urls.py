"""
Copyright (c) 2022 - present Samed Buğra KARATAŞ
"""

from django.urls import path
from app import views

urlpatterns = [

    # The home page
    path('', views.main_page, name='home'),
    path('main', views.main_page, name='home'),
    path('add#<title>#', views.add_todo, name='add'),
    path('checkTrue#<todo_id>#', views.checked_todo, name='checkTrue'),
    path('delete#<todo_id>#', views.delete_todo, name='delete'),
    # The edit page
    path('edit#<todo_id>#', views.edit_todo_page, name='edit'),
    path('editsave#<todo_id>#<new_title>', views.edit_todo_save, name='editsave'),
    # The login page
    path('signup', views.sign_up_page, name='signup'),
    path('login', views.login_page, name='login'),
    path('logout', views.log_out, name='logout'),

]
