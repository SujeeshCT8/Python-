i_name =[]
i_price =[]

n = int(input("enter the no of items want to buy :"))
for i in range(n):
    item_name = input("item name : ")
    item_price = int(input("item price : "))
    i_name.append(item_name)
    i_price.append(item_price)

   

total = sum(i_price)
if total > 1000:
    final_price = total*.9
else:
    final_price = total


print("---Shoping list bill---")
print("\n")
print("item  price")
for name, price in zip(i_name, i_price):
    print(f"{name}: {price}")

print("Total Price :",total)
print("final price after discount : ",final_price)