from django.shortcuts import render
from catalog.models import Author, Genre, Book, Director, Adaptation
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    # qs = Book.objects.all()

    num_books = Book.objects.all().count()
    num_adaptations = Adaptation.objects.all().count()

    # filterName_query = request.GET.get('filterName')
    
    # print('Yo, ', filterName_query)
    
    # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    num_directors = Director.objects.count()
    
    context = {
        'num_books': num_books,
        # 'num_instances': num_instances,
        # 'num_instances_available': num_instances_available,
        'num_adaptations': num_adaptations,
        'num_directors': num_directors,
        'num_authors': num_authors,
        # 'queryset': qs, 
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)





class BookListView(generic.ListView):
    model = Book
    # paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

class AdaptationListView(generic.ListView):
    model = Adaptation
    paginate_by = 10

class AdaptationDetailView(generic.DetailView):
    model = Adaptation

class DirectorListView(generic.ListView):
    model = Director
    paginate_by = 10

class DirectorDetailView(generic.DetailView):
    model = Director