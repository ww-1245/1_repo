from asyncio import windows_utils
from encodings import euc_jisx0213


class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def print_info(self):
        print(f"该员工姓名为{self.name},工号为{self.id}")
class FullEmployee(Employee):
    def __init__(self,name,id,mouth_salary):#    def __init__(self,name,id):
        super().__init__(name,id)
        self.mouth_salary = mouth_salary#第一次没加
    def calculate_mouth_salary(self):
    #    super().print_info()
        return self.mouth_salary
class PartTimeEmployee(Employee):
    def __init__(self,name,id,daily_salary,work_days):#    def __init__(self,name,id):
        super().__init__(name,id)
    #    super().print_info()
        self.daily_salary = daily_salary
        self.work_days = work_days
    def print_salary(self):
        return self.daily_salary *self.work_days #        print(f"月薪为{self.daily_salary * self.work_days}")
wu1 = FullEmployee("wu1",187,5000)
#print(wu1.print_info())
wu1.print_info()
print(wu1.calculate_mouth_salary())
wu2 = PartTimeEmployee("wu2",153,85,30)
#print(wu2.print_info())
wu2.print_info()
print(wu2.print_salary())