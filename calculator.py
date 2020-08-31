def interface():
    print('MY Program')
    while True:
        print('Options for you:')
        print('1- HDL')
        print('2- LDL')
        print('3- Cholesterol')
        print('9- Quit')
        choice=input("Enter your code: ")
        if choice=='9':
            return
        elif choice =='1':
            HDL_driver()
            #print('Your HDL level is {}'.format(hdl_result))
        elif choice =='2':
            LDL_driver()
            #print('Your LDL level is {}'.format(ldl_result))
        elif choice =='3':
            Cholesterol_driver()
            #print('Your Cholesterol level is {}'.format(chl_result))
        
        pass

version = 2

def print_me(in_string):
    print(in_string)

def Cholesterol_driver():
    # Get input
    chl=input('Insert Cholesterol levels: ')
    chl=int(chl)
    #Check if HDL is normal
    results=check_Cholesterol(chl)
    #Outputs
    #return results
    print('Your Cholesterol level is {}'.format(results))
    pass

def check_Cholesterol(chl):
    if (chl<200):
        return 'Normal'
    elif 200 <= chl <= 239 :
        return 'borderline high'
    else:
        return 'high'
    pass


def LDL_driver():
    # Get input
    ldl=input('Insert LDL: ')
    ldl=int(ldl)
    #Check if HDL is normal
    results=check_LDL(ldl)
    #Outputs
    #return results    
    print('Your LDL level is {}'.format(results))
    pass

def check_LDL(ldl):
    if (ldl>=190):
        return 'very high'
    elif 160 <= ldl <= 189 :
        return 'high'
    elif 130 <= ldl <= 159 :
        return 'borderline high'
    else:
        return 'normal'
    pass

def HDL_driver():
    # Get input
    hdl=input('Insert HDL: ')
    hdl=int(hdl)
    #Check if HDL is normal
    results=check_HDL(hdl)
    #Outputs
    print('Your HDL level is {}'.format(results))
    #return results
    pass

def check_HDL(hdl):
    if (hdl>=60):
        return 'Normal'
    elif 40 <= hdl < 60 :
        return 'Borderline Low'
    else:
        return 'Low'
    
    pass

if __name__=='__main__':
    interface()
