menu = {"pizza":450, "momo":140, "chowmein":150, "keemanoodle":200, "sandwitch":150, "burger":300 }
order_list=[]
total = 0
print("Menu:")
for item,price in menu.items(): ##here menu.items() is used to extract both key and value from dictionary(ie menu in above example)
    print(f"{item} : Rs{price}")
while True:
    order = input("what do you want to order? ").lower()
    if order in menu:
        print(f"you have ordered {order}.")
        total +=menu[order]
        print(f"your total is {total}")
        order_list.append(order)
    
    else:
        print("not available right now")
    more_order = input("Do you want to order more ? ")

    if more_order =="no":
        print("\n")
        print("-------BILL------")
        for item in order_list:
            print(f"{item} - Rs{menu[item]}")
        print(f"your sum total is Rs{total}")
        break
        

    
    
