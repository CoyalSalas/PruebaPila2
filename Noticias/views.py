from django.contrib.auth.mixins import LoginRequiredMixin #Obliga a que estes con tus credenciales para poder visualizar una vista
from django.core.exceptions import PermissionDenied #Valida los permisos
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Comentario, Noticias
from django.urls import reverse_lazy # ne



from django.http import HttpResponse, HttpResponseNotFound

class NoticiasListView(LoginRequiredMixin, ListView):
    model = Noticias
    template_name = 'lista_noticias.html'
    context_object_name = 'noticias_lista'

    login_url = 'login'

class NoticiaDetailView(LoginRequiredMixin, DetailView):
    model = Noticias
    template_name = 'detalle_noticia.html'
    context_object_name = 'noticias_lista'
    
    login_url = 'login'


class NoticiaDeleteView(LoginRequiredMixin, DeleteView):
    model = Noticias
    template_name = 'eliminar_noticia.html'
    success_url = reverse_lazy('lista_noticias')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class NoticiaUpdateView(LoginRequiredMixin, UpdateView):
    model = Noticias
    template_name = 'editar_noticia.html'
    fields = ('Titulo','Descripcion', 'autor')
    login_url = 'login'
    context_object_name = 'noticias_lista'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            return HttpResponseNotFound('<h1>Sin acceso</h1>')
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
class NoticiaCreateView(LoginRequiredMixin, CreateView):
    model = Noticias
    template_name = 'nueva_noticia.html'
    #fields = ('Titulo', 'autor', 'Descripcion')
    fields = ('Titulo', 'Descripcion')

    login_url = 'login'


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseNotFound('<h1>Sin acceso</h1>')
        
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ComentarioCreateView(LoginRequiredMixin,CreateView):
    model = Comentario
    template_name = "agregar_comentario.html"
    success_url = reverse_lazy('home')
    login_url = 'login'

    fields = ('comentario',)


    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.noticia_id = self.kwargs['pk']
        return super().form_valid(form)


