def interface():
    print('MY Program')
    while True:
        print('Options for you:')
        print('1- HDL')
        print('9- Quit')
        choice=input("Enter your code: ")
        if choice=='9':
            return
        elif choice =='1':
            HDL_driver()
        pass
   

interface()
