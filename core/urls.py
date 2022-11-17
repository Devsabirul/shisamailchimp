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
    path('category/<str:category>', categoryTable, name="categoryTable"),
]
