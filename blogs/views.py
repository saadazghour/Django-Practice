from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleCreateForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

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


def article_create_views(request):
    form = ArticleCreateForm()
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ArticleCreateForm()
    return render(request, "articles/article_create.html", {'form':form})