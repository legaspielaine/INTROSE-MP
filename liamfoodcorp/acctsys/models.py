from django.db import models


# Create your models here.
class ChartOfAccounts(models.Model):
    accGrpentry = models.CharField(max_length=50)
    accCode = models.IntegerField(default=0)
    accDescrip = models.CharField(max_length=50)
    Debit = 'Debit'
    Credit = 'Credit'
    TYPES_ENTRY =(
        (Debit, 'Debit'),
        (Credit, 'Credit'),
    )
    accEntry = models.CharField(max_length=10, choices=TYPES_ENTRY)
    
    def _str_(self):
        return "ChartAcct - " + str(self.id)
    
class ProductList(models.Model):
    prodCategory = models.CharField(max_length=50) #productList like dimsum, mami, etc.
    
    def _str_(self):
        return str(prodCategory)
    
class Crew(models.Model):
    crewName = models.CharField(max_length=50)
    
    def _str_(self):
        return str(crewName)
    

    
class Products(models.Model):
    grpCode = models.ForeignKey(ProductList, null=True)
    prodCode = models.IntegerField(default=0)
    prodDescrip = models.CharField(max_length=50)
    sellingPrice = models.DecimalField(max_digits=20, decimal_places=2)
    purchaseAmt = models.DecimalField(max_digits=20, decimal_places=2)
    actualStock = models.DecimalField(max_digits=20, decimal_places=2)
    
    def _str_(self):
        return str(prodCode)
    

class VoucherInfo(models.Model):
    acctCode = models.IntegerField(default=0)
    acctDescrip = models.CharField(max_length=50)
    particulars = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=20, decimal_places=2)
    credit = models.DecimalField(max_digits=20, decimal_places=2)
    
    
    
class JV(models.Model):
    pubDateJV = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=150)
    totalAmt =  models.DecimalField(max_digits=10, decimal_places=2) #computed fixed amount not editable by user 
    vInfo = models.ManyToManyField(VoucherInfo)
    
    def _str_(self):
        return "JV - " + str(self.id)
    
class CDV(models.Model):
    payee = models.CharField(max_length=30)
    checkAmt = models.DecimalField(max_digits=10, decimal_places=2)
    checkNo = models.CharField(max_length=30)
    pubDateCDV = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=150)
    totalAmt =  models.DecimalField(max_digits=10, decimal_places=2) #computed fixed amount not editable by user 
    vInfo = models.ManyToManyField(VoucherInfo)
    
    def _str_(self):
        return "CDV - " + str(self.id)
    
class CRV(models.Model):
    receivedFr = models.CharField(max_length=20)
    pubDateCRV = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=150)
    totalAmt =  models.DecimalField(max_digits=10, decimal_places=2) #computed fixed amount not editable by user 
    vInfo = models.ManyToManyField(VoucherInfo)
    

class Branch(models.Model):
    branchName = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    defaultBank = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    prodList = models.ManyToManyField(ProductList)
    listJV = models.ManyToManyField(JV)
    listCDV = models.ManyToManyField(CDV)
    listCRV = models.ManyToManyField(CRV)
    
    def _str_(self):
        return str(branchName)
    
class Sales(models.Model):
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
	coa = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
	crv = models.ForeignKey(CRV, on_delete=models.CASCADE)
	crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
	beginBal = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	incoming = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	availBal = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	out = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	endBal = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	actualCount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	shortOrOver = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	salesAmt = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	purchaseAmt = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	shortOrOverAmt = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	discount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	vat = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	netAmt = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	cashOnHand = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	cashInBank = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	remarks = models.CharField(max_length=200)

	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)
		