#print('The name of the second program module is {}'.format(__name__))
import calculator as calc
#from calculator import HDL_driver, LDL_driver

print(calc.version)
calc.HDL_driver()
calc.LDL_driver()
