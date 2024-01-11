customers=Customer.objects.all()


firstCustomer =Customer.objects.first()


lastCustomer =Customer.objects.last()


customerByName =Customer.objects.get(name='Hamid Shaikh')

customerById =Customer.objects.get(id=1)

firstCustomer.order_set.all()

order =Order.objects.first()
parentName =order.customer.name

products =Products.objects.filter(category="Out Door")

leastToGreatest =Product.objects.all().order_by('id')
greatestToLeast =Product.objects.all().order_by('id')


productsFiltered =Product.objects.filter(tags__name="")



allOrders ={}

for order in firstCustomer.order_set.all():
	if order.parent.name in allOrders:
		allOrders[order.parent.name]+=1
	else:
		allOrders[order.parent.name]=1


class ParentModel(models.Model):
	name = models.CharField(max_length=200,null=True)


class ChildModel(models.Model):
	parent = models.ForeignKey(ParentModel)	
	name = models.CharField(max_length=200,null=True)

parent =ParentModel.objects.first()

parent.childmodel_set.all()