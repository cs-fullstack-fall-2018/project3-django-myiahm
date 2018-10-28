from .forms import TheForm
from .models import User
from .models import Deposit
from .models import Withdaraw
from .forms import DepositForm
from .forms import WithdrawForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required


def index(request):
    # user_list = User.objects.filter(name=request.user)

    if (request.user.is_authenticated):
        user_list = User.objects.get(name=request.user)
        print(user_list)
        user_deposits = Deposit.objects.all()
        print(user_deposits)
        user_withdarawls = Withdaraw.objects.all()
        print(user_withdarawls)
        context = {'user_list': user_list, 'user_deposits': user_deposits, 'user_withdarawls': user_withdarawls}
        return redirect('userindex')

    else:
        return render (request, 'registration/login.html')


def userIndex(request, pk):
    user_list = User.objects.filter(name=request.user, pk=pk)
    print(user_list)
    user_deposit = Deposit.objects.filter(name=request.user, pk=pk)
    user_withdrawal = Withdaraw.objects.filter(name=request.user, pk=pk)
    context = {'user_list': user_list, 'user_deposit': user_deposit, 'user_withdrawal': user_withdrawal}
    return render(request, 'expense_app/index.html', context)


def add(request):
    if (request.user.is_authenticated.method == 'POST'):
        form = User(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect("index")
    else:
        form = TheForm()
    return render(request, 'expense_app/add.html', {'form': form})


def deposit(request, pk):
    theModel = get_object_or_404(User, pk=pk)

    if (request.method == 'POST'):
        form = DepositForm(request.POST, instance=theModel)
        if (form.is_valid()):
            form.save()
            return redirect("index")
        else:
            print("It looks like your form was invalid. Try again please...")
            return redirect("edit", pk=pk)
    else:
        form = DepositForm(instance=theModel)
    return render(request, 'expense_app/deposit.html', {'form': form})


def withdraw(request, pk):
    theModel = get_object_or_404(User, pk=pk)

    if (request.method == 'POST'):
        form = WithdrawForm(request.POST, instance=theModel)
        if (form.is_valid()):
            form.save()
            return redirect("index")
        else:
            print("It looks like your form was invalid. Try again please...")
            return redirect("edit", pk=pk)
    else:
        form = WithdrawForm(instance=theModel)
    return render(request, 'expense_app/withdraw.html', {'form': form})


def edit(request, pk):
    theModel = get_object_or_404(User, pk=pk)

    if (request.method == 'POST'):
        form = TheForm(request.POST, instance=theModel)
        if (form.is_valid()):
            form.save()
            return redirect("index")
        else:
            print("It looks like your form was invalid. Try again please...")
            return redirect("edit", pk=pk)
    else:
        form = TheForm(instance=theModel)
    return render(request, 'expense_app/add.html', {'form': form})


def log(request):
    return render(request, 'registration/login.html')


def log2(request):
    return render(request, 'registration/logged_out.html')


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('add')

    else:
        f = UserCreationForm()

    return render(request, 'registration/registration.html', {'form': f})
#
# class AuthRequiredMiddleware(object):
#     def process_request(self, request):
#         if not request.user.is_authenticated():
#             return HttpResponseRedirect(reverse('index')) # or http response
#         return None
