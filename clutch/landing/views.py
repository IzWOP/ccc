from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'landing/index.html', {'title':'home', 'home_page':'active'})

def about(request):
	return render(request, 'landing/about.html', {'title':'about', 'about_page':'active'})

def gallery(request):
	return render(request, 'landing/gallery.html', {'title':'gallery', 'gallery_page':'active'})

