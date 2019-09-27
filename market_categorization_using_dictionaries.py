orders={'apple':3,'cucumber':4,'yogurt':1,'can':5}
vegatables=['cucumber','pepper','zucchini','cabbage']
fruits=['apple','bannana']
dairy=['milk','yogurt','cheese','butter']
no_fruits=0
no_vegatables=0
no_dairy=0
others=0
for types,no in orders.items():
    if types in vegatables:
        no_vegatables+=no
        print("Vegtables\ntype is: {} ,quantatiy is {}".format(types,no))
    elif types in fruits:
        no_fruits+=no
        print("Fruits\ntype is: {} ,quantatiy is {}".format(types,no))
    elif types in dairy:
        no_dairy+=no
        print("Dairy\ntype is: {} ,quantatiy is {}".format(types,no))
    else:
        others+=no
        print("Others\ntype is: {} ,quantatiy is {}".format(types,no))
        
        
        
