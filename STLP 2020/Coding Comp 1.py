##Prompt User
employeeFile = "employees.csv"
transFile = "transactions.csv"

fEmployees = open(employeeFile, "r")
empLines = fEmployees.readlines()
#print(EmpLines)

fTrans = open(transFile, "r")
transLines = fTrans.readlines()
#print(transLines)
fEmployees.close()
fTrans.close()

transactionInfo = [[]] #Format [[categories], [transactions...]]
index = -1

##Process the Transactions
for item in transLines:
    stringVar = ""
    index += 1
    transactionInfo.append([])
    for char in item:
            if char == "[" or char == "'":
               continue
            elif char == ",":
                print(index)
                transactionInfo[index].append(stringVar)
                stringVar = ""
                continue
            else:
                stringVar += char
    transactionInfo[index].append(stringVar[0:-1])
transactionInfo.remove(transactionInfo[-1])

##Process the Employees
employeeInfo = [[]] #Format [[categories], [transactions...]]
index = -1

for item in empLines:
    stringVar = ""
    index += 1
    employeeInfo.append([])
    for char in item:
            if char == "[" or char == "'":
               continue
            elif char == ",":
                print(index)
                employeeInfo[index].append(stringVar)
                stringVar = ""
                continue
            else:
                stringVar += char
    if stringVar[-1] == "\n":
        stringVar = stringVar[:-1]
    employeeInfo[index].append(stringVar)
employeeInfo.remove(employeeInfo[-1])

print(transactionInfo)
print(employeeInfo)

def indexTrans(name):
    index = -1
    for item in transactionInfo[0]:
        index += 1
        if item == name:
            return index
    return -1

def indexEmp(name):
    index = -1
    for item in employeeInfo[0]:
        index += 1
        if item == name:
            return index
    return -1

customerInd = indexTrans("Customer")
jobInd = indexTrans("Job")
dateInd = indexTrans("Date")
employeeInd = indexTrans("Employee")
chargeInd = indexTrans("Charge")

print(jobInd)

empEmployeeInd = indexEmp("Employee")
empTitleInd = indexEmp("Title")
empCommissionInd = indexEmp("Commission")
empBaseSalaryInd = indexEmp("Base salary")

employeeList = []
customerList = []

##Get The values for the above lists
for item in transactionInfo:
    print(item)
    customerList.append(item[customerInd])

for item in employeeInfo:
    employeeList.append(item[empEmployeeInd])

customerList.remove(customerList[0])
employeeList.remove(employeeList[0])

print(employeeList)
print(customerList)

#Clear Redundant Names
for name in customerList:
    counter = 0
    for name2 in customerList:
        if name == name2:
            if counter == 0:
                counter+=1
            else:
                customerList.remove(name)
                continue
print(customerList)

customerDict = { ## customer : [[job, date, employee, charge]]
    }

def processCustomer(name):
    global customerDict,transactionInfo, customerInd, jobInd, dateInd, chargeInd, employeeInd
    cusList = []
    customerDict[name] = []
    for i in transactionInfo:
        if i[customerInd] == name:
            cusList.append(i[jobInd])
            cusList.append(i[dateInd])
            cusList.append(i[employeeInd])
            cusList.append(i[chargeInd])
            customerDict[name].append(cusList)
            cusList = []

for i in customerList:
    processCustomer(i)

maxLen = 0
for i in employeeList:
    if maxLen < len(i):
        maxLen = len(i)

maxLen += 1
print(customerDict)

def spaces(num):
    stringVar = ""
    for i in range(num):
        stringVar += " "
    return stringVar

def writeCustomerInvoice(name):
    global maxLen
    f = open(name + ".txt", "w+")
    f.write(name + ", here is your invoice.\n\nItemized charges:\n")
    f.write("Job     Date       Employee" + spaces(maxLen - 8) + "Charge\n")
    for item in customerDict[name]:
        f.write(item[0] + spaces(8-len(item[0])) + item[1] + spaces(11-len(item[1])) + item[2] + spaces(maxLen - len(item[2])) + item[3] + "\n")

    total = 0
    for item in customerDict[name]:
        total += float(item[3][1:])
    f.write("\nTotal for this invoice: $" + str(total) + "\n\nPayment due in 30 days\n\nThank you!")
    f.close()         

for i in customerList:
    writeCustomerInvoice(i)


print(employeeInfo)
print(empCommissionInd)
f = open("payroll.txt", "w+")
for name in employeeList:
    total = 0
    income = 0
    for item in transactionInfo:
        if item[employeeInd] == name:
            f.write(item[employeeInd] + "," + item[customerInd] + "," + item[jobInd]+ "," + item[dateInd] + "," + item[chargeInd] + "\n")
            total+= float(item[chargeInd][1:])
    for item in employeeInfo:
        if item[empEmployeeInd] == name:
            IIndex = employeeInfo.index(item)

    income += float(employeeInfo[IIndex][empBaseSalaryInd][1:])
    print(income)
    income += round(total * (float(employeeInfo[IIndex][empCommissionInd][:-1]) /100), 2)
    f.write(name + " weekly salary $" + str(income) + "\n\n")

f.close()





    
