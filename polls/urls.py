from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    ## the 'name' value as called by the {% url %} template tag
    # name=은 html안에서 url이 해당 값을 가지고 찾아온다.
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
]