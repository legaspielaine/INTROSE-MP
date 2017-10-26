from django import forms
from django.forms import widgets, ModelChoiceField
from .models import Branch, ChartOfAccounts, Products

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = [
            'branchName',
            'address',
            'defBank',
        ]
        widgets = {
            'branchName': forms.TextInput(attrs=('required': True,'placeholder':'Enter branch name')),
            'address': forms.TextInput(attrs=('placeholder':'Enter branch address')),
            'defBank': forms.TextInput(attrs=('required': True,'placeholder':'Enter default bank')),
            
        }
        
        labels = {
           'branchName':'Branch Name : ',
            'address':'Address : ',
            'defBank': 'Default Bank : ',
        }
class COAForm(form.ModelForm):
    class Meta:
        model = ChartOfAccounts
        exclude = [
            'branch',
        ]
        fields = [
            'accGrpentry', 
            'accCode',
            'accDescrip', 
            'accEntry', 
        ]
        
        widgets = [
            
            'accGrpentry': forms.TextInput(attrs=( 'required': True,'placeholder':'Enter branch name')),
            'accCode': forms.TextInput(attrs=('required': True,'placeholder':'Enter branch name')),
            'accDescrip': forms.TextInput(attrs=('required': True,'placeholder':'Enter account Description')), 
            'accEntry': forms.TextInput(attrs=('required': True,'placeholder':'Enter account entry ')),  
        ]
        
        label = [
            'accGrpentry': 'Account Group Entry', 
            'accCode': 'Account Code',
            'accDescrip': ' Account Description', 
            'accEntry':'Account Entry (Debit/Credit)', 
        ]
        
        
class ProductForm:
    class Meta:
        model = Products
        fields = [
            'grpcode',
            'prodCode',
            'prodDescrip', 
            'sellingPrice', 
            'purchaseAmt',
            'actualStock', 
        ]
        widgets = [
            'grpcode': forms.TextInput(attrs={'required': True, 'placeholder':'Enter grpcode'}),
            'prodCode': forms.NumberInput(attrs={'required': True,'placeholder':'Enter prodcode'}), 
            'prodDescrip': forms.TextInput(attrs={'required': True, 'placeholder':'Enter grpcode'}), 
            'sellingPrice':forms.NumberInput(attrs={'step': 0.01, 'value':'0.00', 'placeholder':'0.00'}), 
            'purchaseAmt':forms.NumberInput(attrs={'step': 0.01, 'value':'0.00', 'placeholder':'0.00'}), 
            'actualStock':forms.NumberInput(attrs={'step': 0.01, 'value':'0.00', 'placeholder':'0.00'}),  
            
        ]
        label = [
            'grpcode':'Group Code : ',
            'prodCode': 'Product Code : ',
            'prodDescrip': 'Product Description : ', 
            'sellingPrice':'Selling Price : ', 
            'purchaseAmt':'Purchase Amount : ',
            'actualStock': 'Actual Stock : ', 
        ]
        