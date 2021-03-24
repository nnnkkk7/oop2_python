class Employee:
    
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Employee.num_of_emps += 1

    ##フルネームに整形   
    def fullname(self):
        return '{} {}'.format(self.first, self.last)    

    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount )


##サブクラスを作成
class Developer(Employee):
    raise_amount = 1.20

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Maneger(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)   

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())             

dev1 = Developer('soo', 'huu', 30000, 'python') 
dev2 = Developer('koo', 'hoo', 70000, 'ruby')


mgr1 = Maneger('huuu', 'fuu', 100000, [dev1])

mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)

mgr1.print_emps()

print(mgr1.email)
mgr1.add_emp(dev2)



print(dev1.prog_lang)

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)
