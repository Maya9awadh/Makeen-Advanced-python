class Resturant:
    def __init__(self,menu_item,book_table,customer_order):
        self.menu_item=menu_item
        self.book_table=book_table
        self.customer_order=customer_order
    def add_item(self,item):
        self.menu_item.append(item)
        
    def table_reservations(self):
        return self.book_table
    
    def take_order(self):
        order=input("What is your order: ")
        while order !='':
            self.customer_order.append(order)
            order=input("What is your order: ")
        
    def get_menu(self):
        return self.menu_item
    def get_order(self):
        return self.customer_order
r1=Resturant(['water','cake','tea'],3,[])
r1.add_item('coffee')

print(r1.get_menu())
r1.take_order()
print(r1.get_order())