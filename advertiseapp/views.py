from django.shortcuts import render, get_object_or_404, redirect
from .models import Ad
from .forms import PostForm
from django.db.models import Q

def home(request):
    reklama = 0
    reklame = Ad.objects.all()
    for x in reklame: #prikaze najsveziju gold reklamu
        if x.posttype == 'G':
            reklama = x
    return render(request,'index.html', {'ad' : reklama})

def advertise(request):
    reklame = Ad.objects.all()
    return render(request, 'advertising.html', {'reklame' : reklame})

def aboutus(request):
    return render(request, 'aboutus.html')

def postad(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/advertising')

    return render(request, 'postad.html',{'form' : form})

def post(request,id):
    ad = get_object_or_404(Ad, id = id)
    return render(request,'post.html', {'ad' : ad})

def like(request, id):
    ad = get_object_or_404(Ad, id = id)
    ad.likes += 1
    ad.save()
    link = "/" + str(id) + 'post'
    return redirect(link)

def dislike(request, id):
    ad = get_object_or_404(Ad, id = id)
    ad.dislikes += 1
    ad.save()
    link = "/" + str(id) + 'post'
    return redirect(link)
    
def search(request):
    reklame = Ad.objects.filter(Q(description1__icontains = request.GET.get('keywords')) | Q(description2__icontains = request.GET.get('keywords')) | Q(pagetype__icontains = request.GET.get('keywords')) | Q(username__icontains = request.GET.get('keywords')))

    if (request.GET.get('anytype') != 'anytype') and (request.GET.get('normal') != None or request.GET.get('bronze') != None or request.GET.get('silver') != None or request.GET.get('gold') != None):
        reklame = reklame.filter(Q(posttype__exact = request.GET.get('normal')) | Q(posttype__exact = request.GET.get('bronze')) | Q(posttype__exact = request.GET.get('silver')) | Q(posttype__exact = request.GET.get('gold')))
    #radi, ali da li je anytype uopste potreban realno? Sad pogledati sutra jos ove forme i baciti se na profil i posle samo ulepsavanje
    if request.GET.get('min') != '' and request.GET.get('max') != '':
        reklame = reklame.filter(followers__gte = request.GET.get('min')).filter(followers__lte = request.GET.get('max'))
    elif request.GET.get('min') != '':
        reklame = reklame.filter(followers__gte = request.GET.get('min'))
    elif request.GET.get('max') != '':
        reklame = reklame.filter(followers__lte = request.GET.get('max'))

    #dodati sta se desi kad je min >= max?
    return render(request, 'advertising.html', {'reklame' : reklame})
    
# Create your views here.
