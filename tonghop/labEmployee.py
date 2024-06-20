import matplotlib.pyplot as plt
import Employee as emp
import numpy as np
import pandas as pd
import os
import EmployeeSystem as es

menu_options ={
    1: 'Load data from file',
    2: 'Add new employee',
    3: 'Display list of employees',
    4: 'Show employee details',
    5: 'Update employee information',
    6: 'Delete employee',
    7: 'Increase salary of employee',
    8: 'Decrease salary of employee',
    9: 'Show total employee a month',
    10: 'Show total salary a month',
    11: 'Show average of salary a month',
    12: 'Show average of age',
    13: 'Show maxium salary',
    14: 'Sort list of employee according to salary by ascending',
    15: 'Draw salary according to age',
    16: 'Draw average of salary chart by age group',
    17: 'Draw percentage of salary by age group',
    18: 'Draw percentage of total employee by age group',
    19: 'Store data to file',
    'Others': 'Exit program'

}
def print_menu():
    for key in menu_options.keys():
        print(key,'--',menu_options[key])

ab = es.EmployeeSystem()

while(True):

    os.system('cls')
    print_menu()
    chon=''
    try:
        chon=int(input('Enter your choice: '))
    except:
        print('Wrong format, please try again...')
    #Load data from file 
    if chon==1:
        ab.load_data_from_file()
    #Add new employee
    elif chon==2:
        ab.add_employee()
    #Display list of employees
    elif chon==3:
        ab.display_list_of_employees()
    #Show employee details
    elif chon==4:
        ab.show_employee_details()
    #Update employee information
    elif chon==5:
        ab.update_employee_information()
    #Delete employee
    elif chon==6:
        ab.delete_employee()
    #Increase salary of employee
    elif chon==7:
        ab.increase_salary_of_employee()
    #Decrease salary of employee
    elif chon==8:
        ab.decrease_salary_of_employee()
    #Show total employee a month
    elif chon==9:
        ab.show_total_employee_a_month()
    #Show total salary a month
    elif chon==10:
        ab.show_total_salary_a_month()
    #Show average of salary a month
    elif chon==11:
        ab.show_average_of_salary_a_month()
    #Show average of age
    elif chon==12:
        ab.show_average_of_age()
    #Show maxium salary
    elif chon==13:
        ab.show_maxium_salary()
    #Sort list of employee according to salary by ascending
    elif chon==14:
        ab.sort_list_of_employee_according_to_salary_by_ascending()
    #Draw salary according to age
    elif chon==15:
        ab.draw_salary_according_to_age()
    #Draw average of salary chart by age group
    elif chon==16:
        ab.draw_average_of_salary_chart_by_age_group()
    #Draw percentage of salary by age group
    elif chon==17:
        ab.draw_percentage_of_salary_by_age_group()
    #Draw percentage of total employee by age group
    elif chon==18:
        ab.draw_percentage_of_total_employee_by_age_group()
    #Store data to file
    elif chon==19:
        ab.store_data_to_file()
    #Exit program
    
        


