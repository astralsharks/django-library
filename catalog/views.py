from django.shortcuts import render
from catalog.models import Author, Genre, Book, Director, Adaptation
from django.views import generic
from django.db.models import Q

# Create your views here.
def index(request):
    """View function for home page of site."""

    num_books = Book.objects.all().count()
    num_adaptations = Adaptation.objects.all().count()
    num_authors = Author.objects.count()
    num_directors = Director.objects.count()
    
    context = {
        'num_books': num_books,
        'num_adaptations': num_adaptations,
        'num_directors': num_directors,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    queryset = Book.objects.order_by('year')
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = Genre.objects.all() 
        context['author'] = Author.objects.all()
        return context
    
    def get_queryset(self):
        qs = super().get_queryset()
        filterName = self.request.GET.get('filterName')
        filterYear = self.request.GET.get('filterYear')
        filterGenre = self.request.GET.get('filterGenre')
        filterAuthor = self.request.GET.get('filterAuthor')
       
        if filterName != '' and filterName is not None:
            qs = qs.filter(title__icontains=filterName)
        if filterYear != '' and filterYear is not None and filterYear.isnumeric():
            qs = qs.filter(year__icontains=filterYear)
        if filterGenre != '' and filterGenre is not None and filterGenre != 'Choose genre...':
            qs = qs.filter(genre__name=filterGenre)
        if filterAuthor != '' and filterAuthor is not None and filterAuthor != 'Choose author...':
            filterAuthor.replace(" ", "")
            result = [x.strip() for x in filterAuthor.split(',')]
            print(result[1])
            print(result[0])
            qs = qs.filter(Q(author__first_name__icontains=result[1]) & Q(author__last_name__icontains=result[0]))

        return qs

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    queryset = Author.objects.order_by('date_of_birth')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nat = Author.objects.values_list('nationality', flat=True).distinct().order_by()
        context['nationality'] = nat
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        filterFirstName = self.request.GET.get('filterFirstName')
        filterLastName = self.request.GET.get('filterLastName')
        filterDate = self.request.GET.get('filterDate')
        filterNationality = self.request.GET.get('filterNationality')
        print('Yo, ', filterNationality)

        if filterFirstName != '' and filterFirstName is not None:
            qs = qs.filter(first_name__icontains=filterFirstName)
        if filterLastName != '' and filterLastName is not None:
            qs = qs.filter(last_name__icontains=filterLastName)
        if filterDate != '' and filterDate is not None:
            qs = qs.filter(date_of_birth__icontains=filterDate)
        if filterNationality != '' and filterNationality is not None and filterNationality != 'Choose nationality...':
            qs = qs.filter(nationality__icontains=filterNationality)

        return qs

class AuthorDetailView(generic.DetailView):
    model = Author

class AdaptationListView(generic.ListView):
    model = Adaptation
    queryset = Adaptation.objects.order_by('year')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = Genre.objects.all() 
        context['director'] = Director.objects.all()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        filterName = self.request.GET.get('filterName')
        filterYear = self.request.GET.get('filterYear')
        filterGenre = self.request.GET.get('filterGenre')
        filterDirector = self.request.GET.get('filterDirector')
       
        if filterName != '' and filterName is not None:
            qs = qs.filter(title__icontains=filterName)
        if filterYear != '' and filterYear is not None and filterYear.isnumeric():
            qs = qs.filter(year__icontains=filterYear)
        if filterGenre != '' and filterGenre is not None and filterGenre != 'Choose genre...':
            qs = qs.filter(genre__name=filterGenre)
        if filterDirector != '' and filterDirector is not None and filterDirector != 'Choose director...':
            filterDirector.replace(" ", "")
            result = [x.strip() for x in filterDirector.split(',')]
            print(result[1])
            print(result[0])
            qs = qs.filter(Q(director__first_name__icontains=result[1]) & Q(director__last_name__icontains=result[0]))
        
        return qs

class AdaptationDetailView(generic.DetailView):
    model = Adaptation

class DirectorListView(generic.ListView):
    model = Director
    queryset = Director.objects.order_by('date_of_birth')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nat = Director.objects.values_list('nationality', flat=True).distinct().order_by()
        context['nationality'] = nat
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        filterFirstName = self.request.GET.get('filterFirstName')
        filterLastName = self.request.GET.get('filterLastName')
        filterDate = self.request.GET.get('filterDate')
        filterNationality = self.request.GET.get('filterNationality')
        print('Yo, ', filterFirstName)

        if filterFirstName != '' and filterFirstName is not None:
            qs = qs.filter(first_name__icontains=filterFirstName)
        
        if filterLastName != '' and filterLastName is not None:
            qs = qs.filter(last_name__icontains=filterLastName)
        
        if filterDate != '' and filterDate is not None:
            qs = qs.filter(date_of_birth__icontains=filterDate)

        if filterNationality != '' and filterNationality is not None and filterNationality != 'Choose nationality...':
            qs = qs.filter(nationality__icontains=filterNationality)

        return qs

class DirectorDetailView(generic.DetailView):
    model = Director