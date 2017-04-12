#Maryanne Magnier
    #lab5.py
    #3/9/2017

from functools import reduce
def get_ids(records_list):
    '''This function will be able to pull out the id number specifically
    to be used in the following method in order to see if that id is already
    present.'''
    # go through as many lists as are contained in the records_list
    # id will be the second element of the list within the records list
    id_list = [ls[1] for ls in records_list]

    # return the id
    return id_list

def add_employee(name, id, salary, year, records_list):
    '''It will create a new record
    for the new employee and add it to the already existing records list.
    The employee should only be added if its id is not already present in the
    records list. This function should return true if successfully added
    and false if it was already present.'''

    # smaller employee record list
    employee_list = [name, id, salary, year]

    # if id passed in is already present, will return false
    if id in get_ids(records_list):
        return False

    # if id is not already present, will add to records_list and return true
    else:
        # still will not be exactly desired behavior
        records_list.append(employee_list)
        return True

def get_record(id, records_list):
    '''Takes an employee id and a list and returns the rest of the full employee
    record (the four parameters). The function should return the empty
    list if no record exists for the given id.'''

    # gets the employee record
    found_employee = [employee_list for employee_list in records_list if employee_list[1] == id]

    # if there is no employee, return the empty list
    if len(found_employee) == 0:
        return []

    else:
        # return sthe rest of the full employee record
        return found_employee[0]


def remove_employee(id, records_list):
    '''Removes the record with the given id from the employee records
    list. The function should return True if it was able to remove the record,
    and False if the record didn't exist.'''

    #if id does match, should know what list it belongs to
    employee_index = get_employee_index(id, 0, records_list)

    # check to see if the index is -1
    if employee_index == -1:
        return False

    #remove the employee if it exists!!
    records_list.remove(records_list[employee_index])
    return True

def earning_ratio(records_list):
    '''Should return a list of lists. These mini lists should contain an employee
    ID and that employee's salary divided by their year of service. Any employee
    who has worked 5 years or less should not be included.'''

    #at this point we have a list of the employees who have worked for over 5 years- want a list with ratio
    salary_list = [[employee_list[1], employee_list[2] / employee_list[3]] for employee_list in records_list if employee_list[3] > 5]
    return salary_list

def get_employee_index(id, n, records_list):
    '''Recursive method to get the index of the employee list in the
    records_list, else -1 if it is not found.'''
    #base case: if records list is empty
    if len(records_list) == 0:
        return -1

    #next base case: found the item we're looking for, return n
    employee_list = records_list[0]
    if employee_list[1] == id:
        return n

    else:
        # recursive step: get the index
        return get_employee_index(id, n+1, records_list[1:])

def worst_payed(records_list):
    '''Should return name of employee who has the lowest earning ratio.'''

    # list with the lowest salary
    lowest_salary_list = reduce(lambda x, y: x if x[1] < y[1] else y, earning_ratio(records_list))
    # get the id from lowest salary list
    id = lowest_salary_list[0]
    # call get record to get the name
    record = get_record(id, records_list)
    # now that we have the record, get the name
    name = record[0]

    # return the name of employee with lowest earning ratio
    return name
