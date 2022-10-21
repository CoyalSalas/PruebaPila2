from django.urls import path, include 
from .views import NoticiaDetailView, NoticiasListView, NoticiaUpdateView, NoticiaDetailView, NoticiaDeleteView, NoticiaCreateView, ComentarioCreateView


urlpatterns = [
    path('<int:pk>/editar', NoticiaUpdateView.as_view(), name = 'editar_noticia'),    
    path('<int:pk>/', NoticiaDetailView.as_view(), name = 'detalle_noticia'),    
    path('<int:pk>/eliminar', NoticiaDeleteView.as_view(), name = 'eliminar_noticia'),  
    path('nuevo/', NoticiaCreateView.as_view(), name = 'nueva_noticia'),      
    path('', NoticiasListView.as_view(), name = 'lista_noticias'),    
    path('', NoticiasListView.as_view(), name = 'lista_noticias'),    
    path('<int:pk>/comentario/', ComentarioCreateView.as_view(), name='agregar_comentario'),
]
