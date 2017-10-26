from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ChartOfAccounts, ProductList, Crew, Product, VoucherInfo, JV, CDV, CRV, Branch, Sales
from acctsys.forms import BranchForm, COAForm


def index(request):
    return HttpResponse("<a href='/addBranch/'>click this</a>")


def addBranch(request):
    if request.method == 'POST':
        branchform = BranchForm(request.POST)
        if branchform.is_valid():
            branchform.save()
            return redirect('/')
    else:
        branchform = BranchForm()
        context = {
            'branchform': branchform
        }
        return render(request, '/acctsys/addbranch.html', context)


def addCOA(request):
    if request.method == 'POST':
        coaform = COAForm(request.POST)
        if coaform.is_valid():
            coaform.save()
            return redirect('/')
    else:
        coaform = COAForm()
        context = {
            'coaform': coaform
        }
        return render(request, '/acctsys/addcoa.html', context)

