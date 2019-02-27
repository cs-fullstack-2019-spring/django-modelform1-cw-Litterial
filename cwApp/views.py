from django.shortcuts import render,HttpResponse
from .forms import BlogForm

# Create your views here.
def index(request): #Test page to see if server works.
    return render(request,'cwApp/index.html')

def blogPost(request):
    newForm=BlogForm()  #calls Blog Form and defines it as a variable
    if request.method=='POST':
        newForm=BlogForm(request.POST)  #changes newForm to all the posted information
        if newForm.is_valid():
            newForm.save(commit=True) #saves immediately 'commit=true' if the post info is valid
            return index(request) #returns to the index
        else:
            print('Invalid entries in form')  #otherwise prints invalid entries
    return render(request,'cwApp/submitBlog.html',{'submitForm':newForm})  #Go to submit template