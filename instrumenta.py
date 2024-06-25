first= int( input("enter first number:"))
second= int( input("enter second number:"))
third= int( input("enter third number:"))
forth= int( input("enter forth number:"))

if first<second and first<third and first<forth:
    print(first,"is the smallest")
elif second<first and second<third and second<forth:
    print(second,"is the smallest")
elif third<first and third<second and third<forth:
    print(third,"is the smallest")
else:
    print(forth,"is the smallest")