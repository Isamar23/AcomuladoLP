class City:
    def __init__(self, name, status, id):
        self.name = name
        self.status = status
        self.id = id

    def __str__(self):
        return self.name
    
class jobsj:
    def __init__(self, name, status, id):
        self.name = name
        self.status = status
        self.id = id

    def __str__(self):
        return self.name
    
class Employee:
    def __init__(self, name,city_id, jobsj_id, salary, status, id):
        self.name = name
        self.city = city_id
        self.jobsj = jobsj_id
        self.salary = salary
        self.status = status
        self.id = id
    
    def __str__(self):
        return self.name 
    
    def get_full_name(self):
        return self.name 
    
    def get_city(self):
        return self.city.name
    
    def get_jobsj(self):
        return self.jobsj.name
    
    def get_salary(self):
        return self.salary
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status

def set_status(self, id):
        self.id = id
    
