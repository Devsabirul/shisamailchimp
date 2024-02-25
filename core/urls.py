from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="HOME"),
    path('send-mail', sendMail, name="sendMail"),
    path('add-email', addemail, name="addemail"),
    path('update-email/<int:id>', updateemail, name="updateemail"),
    path('delete/<int:pk>', delete, name="delete"),
    path('historydelete/<int:pk>', historydelete, name="historydelete"),
    path('tables', tableview, name="tableview"),
    path('history', history, name="history"),
    path('settings', settings, name="settings"),
    path('update-user-info', update_user, name="update_user"),
    path('change-password', change_password, name='change_password'),
    path('category/<str:category>', categoryTable, name="categoryTable"),
    path('export_data_to_excel', export_data_to_excel, name="export_data_to_excel"),
]


