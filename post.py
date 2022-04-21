class Post:
  
  def __init__(self, title, company, location, salary):
      self.title = title
      self.company = company
      self.location = location
      self.salary = salary
  
  def __repr__(self) -> str:
    return 'Title : {}\nCompany : {}\nLocation : {}\nSalary : {}'.format(self.title, self.company, self.location, self.salary)
  
  def set_title(self, title) -> str:
    self.title = title
  
  def set_company(self, company) -> str:
    self.company = company
  
  def set_location(self, location) -> str:
    self.location = location
  
  def set_salary(self, salary) -> str:
    self.salary = salary
  