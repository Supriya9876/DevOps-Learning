class person:
    def __init__(self,fname,age):
        self.fname=fname
        self.age=age
        self.skills=[]
    def printing(self):
        return f'fname={self.fname},age={self.age},skills={self.skills}'
    def skill_insertion(self,skill):
        self.skills.append(skill)
    
p=person("Supriya",23)
p.skill_insertion("python")
print(p.printing())

class student(person):
    pass
s1=student(24,"Rohit")
print(s1.printing())