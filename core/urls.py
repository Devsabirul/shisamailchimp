from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="HOME"),
    path('send-mail', sendMail, name="send_mail"),
    path('add-email', addemail, name="add_email"),
    path('update-email/<int:id>', updateemail, name="update_email"),
    path('delete/<int:pk>', delete, name="delete"),
    path('historydelete/<int:pk>', historydelete, name="history_delete"),
    path('tables', tableview, name="table_view"),
    path('history', history, name="history"),
    path('settings', settings_, name="settings"),
    path('update-user-info', update_user, name="update_user"),
    path('change-password', change_password, name='change_password'),
    path('category/<str:category>', categoryTable, name="categoryTable"),
    path('export_data_to_excel', export_data_to_excel, name="export_data_to_excel"),
]


