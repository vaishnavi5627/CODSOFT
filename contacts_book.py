contacts={}

while True:
    print('\n CONTACT BOOK ')
    print('------------------')
    print('1.Add contact')
    print('2.View contact list')
    print('3.Search contact')
    print('4.Update contact')
    print('5.Delete contact')
    print('6.Exit')
    print('----------------------')

    choice = input('Enter your choice:')

    if choice == '1':
        name = input('Enter your name:')
        if name in contacts:
            print(f'Contact name{name} already exist!!!')
        else:
            phoneno = input('Enter phone number:')
            email = input('Enter email:')
            address = input('Enter address:')
            contacts[name] = {'phoneno':phoneno,  'email':email,  'address':address}
            print(f'Contact name {name} has been created!!!')


    elif choice == '2':
            name = input('Enetr contact name:')
            if name in contacts:
                contact = contacts[name]
                print(f'name:{name},  phoneno:{phoneno},  email:{email},  address:{address}')    
            else:
                print('Contact not found')

    elif choice == '3':
            search_name = input('Search contact:')
            found = False
            for name, contact in contacts.items():
                if search_name.lower() in name.lower():
                    print(f'found {name},  phoneno:{phoneno},  email:{email},  address:{address}')
                    found = True
            if not found:
                print('No contact found ')

    elif choice == '4':
            name = input('Enter name to update:')
            if name in contacts:
                phoneno = input('Enter updated  phone number:')
                email = input('Enetr updated email:')
                address = input('Enter updated address:')
            else:
                print('Contact not found to update')

    elif choice == '5':
            name = input('Enetr contact name to delete :')
            if name in contacts:
                del contacts[name]
                print(f'Contact name:{name} has been deleted')
            else:
                print('Contact not found to delete') 

    elif choice == '6':
            print('Existed........')
            break

    else:
            print('Invalid choice')                                                       
           