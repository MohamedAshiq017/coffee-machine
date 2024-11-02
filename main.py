from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

status="on"
dismenu=Menu()

cmaker = CoffeeMaker()
cmaker.__init__()

counter=MoneyMachine()

# menuitem=MenuItem()
# print(menuitem.name)
while(status=="on"):
  flav=dismenu.get_items()
  choice=input(f"What would you like to have {flav} :")
  if(choice=="off"):
    status=choice
  elif(choice=="report"):
    what=int(input("1.Money\n2.Resource\n"))
    if(what==1):
      counter.report()
    else: 
      cmaker.report()
  else:
    flavobj=dismenu.find_drink(choice)
    menuitemobj=flavobj
    # print(menuitemobj.name,menuitemobj.cost,menuitemobj.ingredients)
    # cmaker.report()
    canMake=cmaker.is_resource_sufficient(menuitemobj)


    if(canMake):
      paid=counter.make_payment(menuitemobj.cost)

    if(paid and canMake):
      cmaker.make_coffee(menuitemobj)



  '''  shortest way
  if  cmaker.is_resource_sufficient(..) and counter.make_payment(...)
    cmaker.make_coffee(...)
  '''


































'''
# choice=input("What would you like? (espresso/latte/cappuccino/):")
cmaker=CoffeeMaker()
cmaker.__init__()
cmaker.report()

# menuitem=MenuItem()
# menuitem.__init__()

menu1=Menu()
menu1.__init__()
available_items=menu1.get_items()
print(available_items)
drink=input("Whatd you want:")
ingdnt=menu1.find_drink(drink)
# menu.get_items()
# menu.find_drink()

print(f"{ingdnt}")
menuitem=ingdnt
print(menuitem['name'])

'''
