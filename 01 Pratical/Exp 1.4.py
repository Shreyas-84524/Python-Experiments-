#Shreyas Rajendra Shigwan, CSE(AIML), Roll no.90
#Exp 1.4 : Gross Salary Calculator
def calculate_gross_salary():
    basic_salary = float(input("Enter the basic salary: "))

    dearness_allowance = 0.70 * basic_salary
    travel_allowance = 0.30 * basic_salary
    house_rent_allowance = 0.10 * basic_salary

    gross_salary = basic_salary + dearness_allowance + travel_allowance + house_rent_allowance

    print(f"The result of Gross salary is {gross_salary}")
    print(f"The result of Basic salary is {basic_salary}")
    print(f"The result of Dearness allowance is {dearness_allowance}")
    print(f"The result of Travel allowance is {travel_allowance}")
    print(f"The result of House rent allowance is {house_rent_allowance}")

calculate_gross_salary()