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
            hdl_result=HDL_driver()
            print('Your HDL level is {}'.format(hdl_result))
        pass

def HDL_driver():
    # Get input
    hdl=input('Insert HDL: ')
    hdl=int(hdl)
    #Check if HDL is normal
    results=check_HDL(hdl)
    #Outputs
    return results
    pass

def check_HDL(hdl):
    if (hdl>=60):
        return 'Normal'
    elif 40 <= hdl < 60 :
        return 'Borderline Low'
    else:
        return 'Low'
    pass

interface()
