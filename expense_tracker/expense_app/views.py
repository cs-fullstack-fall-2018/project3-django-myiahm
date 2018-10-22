from .forms import TheForm
from .models import User
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404




def index(request):
    user_list = User.objects.all()
    return render(request, 'expense_app/index.html', {'user_list': user_list})


def userIndex(request):
    user_list = User.objects.filter(name= request.user)
    context = {'user_list': user_list}
    return render(request, 'expense_app/index.html', context)


def add(request):
    if(request.method == 'POST'):
        form = User(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("index")
    else:
        form = TheForm()
    return render(request, 'expense_app/add.html', {'form': form})


def edit(request, pk):
    theModel = get_object_or_404(User, pk=pk)

    if(request.method == 'POST'):
        form = TheForm(request.POST, instance=theModel)
        if(form.is_valid()):
            form.save()
            return redirect("index")
        else:
            print("Hey buddy. It looks like your form was invalid. Sorry about that...")
            return redirect("edit", pk=pk)
    else:
        form = TheForm(instance=theModel)
    return render(request, 'expense_app/add.html', {'form': form})

# def thisUser(request, user_id):
#     try:
#         user_info = User.objects.get(pk=user_id)
#     except User.DoesNotExist:
#         raise Http404("User does not exist")
#     return render(request, 'expense_app/this.html', {'user_info': user_info})
