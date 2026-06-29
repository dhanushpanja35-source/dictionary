#create new dictionary
employee = {"emp_id":101,"emp_name":"ram","emp_age":24,"emp_dept":"testing"}
print(employee)

#retrieve data
ret=(employee.get("emp_name"))
print(ret)

#update or modify details
modify=employee.update({"emp_age":26})
print(modify)

#delete details
dele = employee.pop("emp_dept")     #pop for deleting the particular value in the dictionary
print(dele)

dele1=employee.popitem()            #popitem will deletes the last item in the dictionary
print(dele1)

print(employee)
