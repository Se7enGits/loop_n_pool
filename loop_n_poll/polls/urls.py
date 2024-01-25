from django.urls import path

from . import views


# Чтобы обратиться в шаблонах к views.detail именно этого приложения,
# нужно дать ему имя:
app_name = 'polls'
# Теперь в любом шаблоне можно вызвать нужную функцию
# по тегу {% url 'polls:detail'}.

urlpatterns = [
    path('', views.index, name='index'),
    # Используем атрибут "name", чтобы обращаться к нему в html-шаблонах
    # и иметь возможность менять адрес только в этом файле.
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
