#from Test import DHCauseList
#from Test import DHCaseCategorization
#from Test import DHCaseStatus
#causeList = DHCauseList.funcCauseList("7","6","2019")
#print(causeList)

#caseStatusByType = DHCaseStatus.funcCaseType("http://delhihighcourt.nic.in/case.asp")
#print(caseStatusByType)
#caseStatusByPet = DHCaseStatus.funcPetRes("http://delhihighcourt.nic.in/case.asp")
#print(caseStatusByPet)
#caseStatusByAdvocate = DHCaseStatus.funAdvocate("http://delhihighcourt.nic.in/case.asp")
#print(caseStatusByAdvocate)

#caseCategoryList = DHCaseCategorization.funcCaseCategory()
#print(caseCategoryList)




from MAIN import updateHearing
retrieveID = updateHearing.retriveRecord()



for item in retrieveID:
    id = item[0]
    courtid = int(item[1])
    if courtid == 1:
        updateHearing.updateRecordDHC(id)
    elif courtid == 2:
        updateHearing.updateRecordRERA(id)

