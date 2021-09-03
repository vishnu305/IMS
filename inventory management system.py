fd = open("Records.txt","r")
txt = fd.read()
fd.close()
products = txt.split("\n")

ui_prod  = str(input("Enter the product_Id: "))
ui_quant = input("Enter the quantity: ")

for product in products:
    prod = product.split(",")
    
    
    if(prod[0] == ui_prod):
        print("***********************")
        print("Product ID: ", prod[0])
        print("Name: ", prod[1])
        print("Price: ",prod[2])
        print("Quant: ",ui_quant)
        print("------------------------")
        print("Billing Amout: ", ui_quant * int(prod[2]))
        print("***********************")
new_record = []

for product in products:
    prod = product.split(",")
    if(ui_prod == prod[0]):
        prod[3] = str(int(prod[3]) - ui_quant)
        
    new_record.append(prod[0] + "," + prod[1] + "," + prod[2] + "," + prod[3] + "\n")
    
new_record[-1] = new_record[-1][:-1]

fd = open("Records.txt", 'w')

for i in new_record:
    fd.write(i)
    
fd.close()