from django.shortcuts import render
from django.utils import timezone
from .models import Lists
from .models import request_status
from .models import divisions
from .forms import RequestForm
from django.shortcuts import redirect,  get_object_or_404
from django.contrib import auth
from django.contrib.auth import models

def home(request):
    return render(request, 'requests/base.html')

def app_request_lists(request):
    current_user = request.user.id
    restricted_group = models.Group.objects.get(id=1)
    restricted_users = restricted_group.user_set.filter(id=current_user)

    if request.user.is_authenticated() and len(restricted_users)>0:
        app_requests = Lists.objects.filter(status_id=2, Initiator=current_user).order_by('created_date')
        return render(request, 'requests/app_request_list.html', {'app_requests': app_requests})

    elif request.user.is_authenticated() and len(restricted_users)==0:
        app_requests = Lists.objects.filter(status_id=2).order_by('created_date')
        return render(request, 'requests/app_request_list.html', {'app_requests': app_requests})

    else:
        return redirect('home')


def rej_request_lists(request):
    current_user = request.user.id
    restricted_group = models.Group.objects.get(id=1)
    restricted_users = restricted_group.user_set.filter(id=current_user)

    if request.user.is_authenticated() and len(restricted_users)>0:
        rej_requests = Lists.objects.filter(status_id=3, Initiator=current_user).order_by('created_date')
        return render(request, 'requests/rej_request_list.html', {'rej_requests': rej_requests})

    elif request.user.is_authenticated() and len(restricted_users)==0:
        rej_requests = Lists.objects.filter(status_id=1).order_by('created_date')
        return render(request, 'requests/rej_request_list.html', {'rej_requests': rej_requests})

    else:
        return redirect('home')

def cur_request_lists(request):

    current_user = request.user.id
    restricted_group = models.Group.objects.get(id=1)
    restricted_users = restricted_group.user_set.filter(id=current_user)

    if request.user.is_authenticated() and len(restricted_users)>0:
        cur_requests = Lists.objects.filter(status_id=1, Initiator=current_user).order_by('created_date')
        return render(request, 'requests/cur_request_list.html', {'cur_requests': cur_requests})

    elif request.user.is_authenticated() and len(restricted_users)==0:
        cur_requests = Lists.objects.filter(status_id=1).order_by('created_date')
        return render(request, 'requests/cur_request_list.html', {'cur_requests': cur_requests})

    else:
        return redirect('home')

    # Do something for anonymous users.


def request_new(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            request = form.save(commit=False)
            request.created_date = timezone.now()
            request.save()
            return redirect('cur_request_list')
    else:
        form = RequestForm()
    return render(request, 'requests/request_new.html', {'form': form})

def request_detail(request, pk):

    Assembled_request = get_object_or_404(Lists, pk=pk)
    return render(request, 'requests/request_detail.html', {'Assembled_request': Assembled_request})

