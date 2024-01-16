names  = []
phone_numbers = []
emails = []
store_names = []
addresses = []
num = 1

for i in range(num):
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    email = input("Email: ")
    store_name = input("Store Name: ")
    address = input("Address: ")
    names.append(name)
    phone_numbers.append(phone_number)
    emails.append(email)
    store_names.append(store_name)
    addresses.append(address)


print("\nName\t\t\t\nPhone Number\t\t\t\nEmail\t\t\t\nStore Name\t\t\t\nAddress\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i], email[i], store_name[i], address[i]))

search_term = input("\nEnter Search Term: ")
print("Search Result")
if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}, Email: {}, Store Name: {}, Address: {}".format(search_term, phone_number, email, store_name, address))
else:
    print("Name Not Found")

def edit_contact():
    search_term = input("Enter Name to Edit: ")
    if search_term in names:
        index = names.index(search_term)
        print("Current Details:")
        print("Name: {}, Phone Number: {}, Email: {}, Store Name: {}, Address: {}".format(names[index], phone_numbers[index], emails[index], store_names[index], addresses[index]))

        phone_number = input("New Phone Number: ")
        email = input("New Email: ")
        store_name = input("New Store Name: ")
        address = input("New Address: ")

        phone_numbers[index] = phone_number
        emails[index] = email
        store_names[index] = store_name
        addresses[index] = address
        print("Contact updated successfully!")
    else:
        print("Name Not Found")

def delete_contact():
    search_term = input("Enter Name to Delete: ")
    if search_term in names:
        index = names.index(search_term)
        del names[index]
        del phone_numbers[index]
        del emails[index]
        del store_names[index]
        del addresses[index]
        print("Contact deleted successfully!")
    else:
        print("Name Not Found")

for i in range(num):
    edit_contact()

edit_contact()

delete_contact()
