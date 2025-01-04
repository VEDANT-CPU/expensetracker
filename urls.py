from django.urls import path
from . import views
from .views import ExpenseListView, ExpenseDetailView, ExpenseCreateView

urlpatterns = [
    path("", ExpenseListView.as_view(), name='expenses-home'),
    path("transaction/<int:pk>/", ExpenseDetailView.as_view(), name='expenses-detail'),
    path("transaction/new/", ExpenseCreateView.as_view(), name='expenses-create'),
    path("transaction/<int:pk>/update/", ExpenseUpdateView.as_view(), name='expenses-update'),
    path("transaction/<int:pk>/delete/", ExpenseDeleteView.as_view(), name='expenses-delete'),
]