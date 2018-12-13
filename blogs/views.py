from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

from .models import Article
from .forms import ArticleCreateForm


# Create your views here.
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'   # <blog>/<modelname>_lise.html
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("my_id")
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html"
    form_class = ArticleCreateForm
    queryset = Article.objects.all()
    # success_url = '/'                      # you can override get_absolute_url for my models through success_url attr


    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)


    # def get_success_url(self):
    #     return '/'


class ArticleUpdateView(UpdateView):
    template_name = "articles/article_update.html"
    form_class = ArticleCreateForm


    def form_valid(self, form):
        return super().form_valid(form)


    def get_object(self):
        id_ = self.kwargs.get("id_update")
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"
    form_class = ArticleCreateForm
    # success_url = "../../"

    def get_object(self):
        id_ = self.kwargs.get("id_delete")
        return get_object_or_404(Article, id=id_)


    def get_success_url(self):
        return reverse("article_list")



# def article_create_views(request):
#     form = ArticleCreateForm()
#     if request.method == 'POST':
#         form = ArticleCreateForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             form = ArticleCreateForm()
#     return render(request, "articles/article_create.html", {'form':form})