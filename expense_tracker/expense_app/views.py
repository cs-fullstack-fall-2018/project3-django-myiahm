from .forms import TheForm
from .models import User
from .models import Deposit
from .models import Withdaraw

from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404




def index(request):
    user_list = User.objects.all()
    user_deposits = Deposit.objects.all()
    user_withdarawls = Withdaraw.objects.all()
    context = {'user_list': user_list,'user_deposits':user_deposits,'user_withdarawls':user_withdarawls}
    return render(request, 'expense_app/index.html', context)

def userIndex(request):
    user_list = User.objects.filter(name= request.user)
    user_deposit = Deposit.objects.filter(name= request.user)
    user_withdrawal = Withdaraw.objects.filter(name= request.user)
    context = {'user_list': user_list,'user_deposit':user_deposit,'user_withdrawal':user_withdrawal}
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
            print("It looks like your form was invalid. Try again please...")
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
