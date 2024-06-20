import Employee as emp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

class EmployeeSystem:
    # Constructor
    def __init__(self):
        self.employees = []
    
    
    # 2.Add new employee
    def add_employee(self):
        code = input('Enter code: ')
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        salary = float(input('Enter salary: '))
        self.employees.append(emp.Employee(code, name, age, salary))
        print('Add new employee successfully')
    # 3.Display list of employees
    def display_list_of_employees(self):
        for e in self.employees:
            e.display()
    # 4.Show employee details
    def show_employee_details(self):
        code = input('Enter code: ')
        for e in self.employees:
            if e.code == code:
                e.display()
                return
        print('Employee not found')
    # 5.Update employee information
    def update_employee_information(self):
        code = input('Enter code: ')
        for e in self.employees:
            if e.code == code:
                name = input('Enter name: ')
                age = int(input('Enter age: '))
                salary = float(input('Enter salary: '))
                e.name = name
                e.age = age
                e.salary = salary
                print('Update employee information successfully')
                return
        print('Employee not found')
    # 6.Delete employee
    def delete_employee(self):
        code = input('Enter code: ')
        for e in self.employees:
            if e.code == code:
                self.employees.remove(e)
                print('Delete employee successfully')
                return
        print('Employee not found')
    # 7.Increase salary of employee
    def increase_salary_of_employee(self):
        code = input('Enter code: ')
        for e in self.employees:
            if e.code == code:
                percent = float(input('Enter percent: '))
                e.increase_salary(percent)
                print('Increase salary successfully')
                return
        print('Employee not found')
    #8.decrease salary of employee
    def decrease_salary_of_employee(self):
        code = input('Enter code: ')
        for e in self.employees:
            if e.code == code:
                percent = float(input('Enter percent: '))
                e.decrease_salary(percent)
                print('Decrease salary successfully')
                return
        print('Employee not found')
    #9. Show total employee a month
    def show_total_employee_a_month(self):
        print('Total employee a month: ', len(self.employees))
    #10.Show total salary a month
    def show_total_salary_a_month(self):
        total_salary = 0
        for e in self.employees:
            total_salary += e.salary
        print('Total salary a month: ', total_salary)
    #11.Show average of salary a month
    def show_average_of_salary_a_month(self):
        total_salary = 0
        for e in self.employees:
            total_salary += e.salary
        print('Average of salary a month: ', total_salary/len(self.employees)) 
    #12.Show average of age
    def show_average_of_age(self):
        total_age = 0
        for e in self.employees:
            total_age += e.age
        print('Average of age: ', total_age/len(self.employees))
    #13.show maxium salary
    def show_maxium_salary(self):
        maxium_salary = 0
        for e in self.employees:
            if e.salary > maxium_salary:
                maxium_salary = e.salary
        print('Maxium salary: ', maxium_salary)
    #14.sort list of according to salary
    def sort_list_of_employee_according_to_salary_by_ascending(self):
        for i in range(len(self.employees)):
            for j in range(i+1, len(self.employees)):
                if self.employees[i].salary > self.employees[j].salary:
                    self.employees[i], self.employees[j] = self.employees[j], self.employees[i]
        print('Sort list of employee according to salary by ascending successfully')
    #15.Draw salary according to age
    def draw_salary_according_to_age(self):
        age = []
        salary = []
        for e in self.employees:
            age.append(e.age)
            salary.append(e.salary)
        plt.plot(age, salary, 'ro')
        plt.xlabel('Age')
        plt.ylabel('Salary')
        plt.show()
    #16.Draw average of salary chart by age group
    def draw_average_of_salary_chart_by_age_group(self):
        age_group = []
        average_salary = []
        for i in range(20, 60, 10):
            age_group.append(str(i) + '-' + str(i+9))
            total_salary = 0
            count = 0
            for e in self.employees:
                if e.age >= i and e.age <= i+9:
                    total_salary += e.salary
                    count += 1
            average_salary.append(total_salary/count)
        plt.bar(age_group, average_salary)
        plt.xlabel('Age group')
        plt.ylabel('Average salary')
        plt.show()
    #17.Draw percentage of salary by age group 
    def draw_percentage_of_salary_by_age_group(self):
        age_group = []
        percentage_salary = []
        for i in range(20, 60, 10):
            age_group.append(str(i) + '-' + str(i+9))
            total_salary = 0
            for e in self.employees:
                if e.age >= i and e.age <= i+9:
                    total_salary += e.salary
            percentage_salary.append(total_salary)
        plt.pie(percentage_salary, labels=age_group, autopct='%.2f%%')
        plt.show()
    #18.Draw perentage of total employee by age group
    def draw_percentage_of_total_employee_by_age_group(self):
        age_group = []
        percentage_employee = []
        for i in range(20, 60, 10):
            age_group.append(str(i) + '-' + str(i+9))
            count = 0
            for e in self.employees:
                if e.age >= i and e.age <= i+9:
                    count += 1
            percentage_employee.append(count)
        plt.pie(percentage_employee, labels=age_group, autopct='%.2f%%')
        plt.show()
    

        
