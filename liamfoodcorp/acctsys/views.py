from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ChartOfAccounts, ProductList, Crew, Product, VoucherInfo, JV, CDV, CRV, Branch, Sales
from acctsys.forms import BranchForm, COAForm, ProductForm


def index(request):
    return render(request, 'acctsys/index.html')


def branch(request):
    return render(request, 'acctsys/branch.html')


def coa(request):
    return render(request, 'acctsys/coa.html')


def inventory(request):
    return render(request, 'acctsys/inventory.html')


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
        return render(request, 'acctsys/addbranch.html', context)


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
        return render(request, 'acctsys/addcoa.html', context)


def addProduct(request):
    # if request.method == 'POST':
    #     productform = ProductForm(request.POST)
    #     if productform.is_valid():
    #         productform.save()
    #         return redirect('/')
    # else:
    productform = ProductForm()
    context = {
        'productform': productform
    }
    return render(request, 'acctsys/addproduct.html', context)
