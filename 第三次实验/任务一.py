class Person:
    def __init__(self,name,age,sex):
        self.m_name=name
        self.m_age=age
        self.m_sex=sex
    def personlnfo(self):
        print(f'姓名为：{self.m_name}')
        print(f'年龄为：{self.m_age}')
        print(f'性别为：{self.m_sex}')
class Student(Person):
    def __init__(self,name,age,sex,college,classnum):
        super().__init__(name,age,sex)
        self.m_college=college
        self.m_classnum=classnum
    def personlnfo(self):
        super().personlnfo()
        print(f'学院为：{self.m_college}')
        print(f'班级为：{self.m_classnum}')
class Teacher(Person):
    def __init__(self,name,age,sex,college,pro):
        super().__init__(name,age,sex)
        self.m_college=college
        self.m_pro=pro
    def personlnfo(self):
        super().personlnfo()
        print(f'学院为：{self.m_college}')
        print(f'专业为：{self.m_pro}')
def lnfo(obj:Person):
    obj.personlnfo()


if __name__=='__main__':
    p1= Person('JB',18,'不明')
    s1=Student('JB',18,'不明','计算机学院','三班')
    t1=Teacher('JB',18,'不明','计算机学院','计算机科学与技术')
    lnfo(p1)
    print('----------------------')
    lnfo(s1)
    print('----------------------')
    lnfo(t1)