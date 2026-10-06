header = """BOOKSTORE RECEIPT"""
book1 = "Python Basics"
price1 = 450
book2 = "Data Science Intro"
price2 = 600
item1 = "\t{} \t₹{}".format(book1, price1)
item2 = "\t{} \t₹{}".format(book2, price2)
total = price1 + price2
total_line = "\tTotal Price:\t₹{}".format(total)
thank_you = "Thank you for shopping with us and have a great day ahead !"
receipt = header + "\n" + item1 + "\n" + item2 + "\n" + total_line + "\n" + thank_you
print(receipt.upper())