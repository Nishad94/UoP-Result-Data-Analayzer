import os
import matplotlib.pyplot as plt
from collections import Counter

CURRENT_DIR = os.path.dirname(__file__)

'''PDF_FILE_ItEntc = "result_itentc.pdf"
PDF_FILE_COMP = "result_comp.pdf"
OUT_FILE_ItEntc = "out_it.txt"
OUT_FILE_COMP = "out_comp.txt"

os.system(("ps2ascii %s %s") %(PDF_FILE_ItEntc, OUT_FILE_ItEntc))
os.system(("ps2ascii %s %s") %(PDF_FILE_COMP, OUT_FILE_COMP))

filenames = ['out_it.txt', 'out_comp.txt']
with open(os.path.join(CURRENT_DIR, 'out_combined.txt'), 'w') as outfile:
    for fname in filenames:
        with open(fname) as inFile:
            outfile.write(inFile.read())'''

#### Function to find user's rank in a given database

def getRank(database, filter_field):
    choice=int(raw_input("1. Find by name  2. Find by roll number : "))
    if choice == 1 :
        query = raw_input("Enter name : ")
        query = query.upper()
        # changed from reversed(), it returns a reverse iterator which can be traversed only once! Avoid using that!
        sorted_list = sorted(database, key = lambda k : k['Marks'][filter_field], reverse=True)
        match_found = False
        ranklist = {}
 
        for student in sorted_list:
            if student['Name'].find(query) != -1 :
                ch = int(raw_input('Did you mean \'' + student['Name'] + '\' ?\n 1. Yes  2. No : '))
                if(ch == 1):
                    NAME = student['Name']
                    match_found = True
                    break
        if match_found == False:
            print 'No match found!'
            exit()
        total_students = len(database)
        rank = 1
        try:
            for student in sorted_list :
                ranklist[student['Name']] = (rank, student['RollNum'])
                rank += 1
            print '\n---------------------------'
            print 'Roll No: ' + ranklist[NAME][1] + '    ' + NAME
            print 'Your rank in {0} is {1}'.format(filter_field, ranklist[NAME][0])
            print '---------------------------'
        except KeyError:
            print 'You entered an invalid name.\n'               
        
    elif choice == 2 :
        query = raw_input("Enter roll number: ")
        ranklist={}
        sorted_list = sorted(database, key=lambda k: k['Marks'][filter_field], reverse=True)
        total_students = len(database)
        rank = 1
        try:
            for student in sorted_list :
                ranklist[student['RollNum']] = (rank, student['Name'])
                rank += 1
            print '\n---------------------------'
            print 'Roll No: ' + str(query) + '    ' + ranklist[query][1]
            print 'Your rank in {0} is {1}'.format(filter_field, ranklist[query][0])
            print '---------------------------'
        except KeyError:
            print 'You entered an invalid Roll Number.\n'
    else:
        print 'Invalid choice!'
    exit()

####

### Generalized graph plotting function
def plotGraph(xRange, yRange, student_db, subField):
    xRange += 1
    len_x_axis = xRange
    len_y_axis = yRange

    list_x_axis=[]
    list_y_axis=[]

    for i in range(len_x_axis):
        list_x_axis.append(i)

    all_scores_cnt = Counter() # { score: number_of_students_with_that_score }

    all_totals = []

    for student in student_db:
        marks = int(student['Marks'][subField])
        all_scores_cnt[marks] += 1

    number_of_students_with_that_score = [] # Mapping index to number of students

    for i in range(xRange):
        number_of_students_with_that_score.append(all_scores_cnt[i])

    list_y_axis = number_of_students_with_that_score
    
    plt.plot(list_x_axis, list_y_axis, 'r')
    plt.ylabel('No. of students')
    plt.xlabel('Marks')
    plt.axis([0, xRange, 0, yRange])
    plt.grid(True)
    plt.show()

    #### END OF MATPLOTLIB Function



f = open('out_combined.txt','r')
pdf = f.read()

IT_Roll = 'S120058'
''' Subject Codes'''
DS = '214441'
CO = '214442'
DELD = '214443'
FDS = '214444'
PSOOP = '214445'
DELD_ORAL_PRAC = '214446'
PL = '214447'
CLL = '214448'

COMP_Roll = 'S120054'
''' Subject Codes'''
COMP_DS = '210241'
DSPS = '210242'
COMP_DELD = '210243'
OSA = '210244'
MPA = '210245'
SS = '210246'

ENTC_Roll = 'S120053'
''' Subject Codes'''
SS_ENTC = '204181'
EDC = '204182'
NT = '204183'
DSA = '204184'
DE = '204185'
EMIT = '204186'




RECORD_DELIM = '....'
NAME_DELIM = '    '

student_db = []

current_pos = 0


# ENTC
while True :
    rec_start = pdf.find(ENTC_Roll, current_pos)
    if rec_start == -1:
        break
    # Find end of current record
    rec_end = pdf.find(RECORD_DELIM, rec_start)
    # Dictionary to map roll number, name, marks...
    student = {}
    student['Branch'] = 'ENTC'
    # Slice student data from pdf and move current_pos to next student position
    student_data = pdf[rec_start : rec_end]
 #   print student_data
    current_pos = rec_end
    # Get roll
    roll_num = ""
    i = 0
    while student_data[i] != ' ' :
        roll_num += student_data[i]
        i += 1
    student['RollNum'] = roll_num

    # Get full name
    # Skip whitespaces
    while not student_data[i].isalpha() :
        i += 1
    name_start = i
    name_end = student_data.find(NAME_DELIM, name_start)
    name = student_data[name_start : name_end]
    student['Name'] = name
    i = name_end
 #   print name
    # Get marks 
    Marks = {}
    # SS_ENTC
    subCode_start = student_data.find(SS_ENTC, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['SS_ENTC'] = int(marks)
  #  print marks
    #SS_TW
    subCode_start = student_data.find(SS_ENTC, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "10"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['SS_TW'] = int(marks)
  #  print marks   
    #EDC
    subCode_start = student_data.find(EDC, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['EDC'] = int(marks)

    #EDC_PRAC
    subCode_start = student_data.find(EDC, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "20"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['EDC_PRAC'] = int(marks)

    #NT
    subCode_start = student_data.find(NT, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['NT'] = int(marks)

    #NT TW
    subCode_start = student_data.find(NT, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "10"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['NT_TW'] = int(marks)

    #DSA
    subCode_start = student_data.find(DSA, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['DSA'] = int(marks)
    
    #DSA_OR
    subCode_start = student_data.find(DSA, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "20"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['DSA_ORAL'] = int(marks)

    #DE
    subCode_start = student_data.find(DE, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['DE'] = int(marks)

    #DE Prac
    subCode_start = student_data.find(DE, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "20"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['DE_PRAC'] = int(marks)
  #  print marks
    #EMIT
    subCode_start = student_data.find(EMIT, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "20"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
 #   print marks
    Marks['EMIT'] = int(marks)
    
    total = 0
    for sub in Marks :
        total += Marks[sub]
    Marks['TOTAL'] = total

    # Add Marks[] to student[]
    student['Marks'] = Marks

    #Add student to db
    student_db.append(student)




while True :
    rec_start = pdf.find(IT_Roll, current_pos)
    if rec_start == -1:
        break
    # Find end of current record
    rec_end = pdf.find(RECORD_DELIM, rec_start)
    # Dictionary to map roll number, name, marks...
    student = {}
    student['Branch'] = 'IT'
    # Slice student data from pdf and move current_pos to next student position
    student_data = pdf[rec_start : rec_end]
    current_pos = rec_end
    # Get roll
    roll_num = ""
    i = 0
    while student_data[i] != ' ' :
        roll_num += student_data[i]
        i += 1
    student['RollNum'] = roll_num

    # Get full name
    # Skip whitespaces
    while not student_data[i].isalpha() :
        i += 1
    name_start = i
    name_end = student_data.find(NAME_DELIM, name_start)
    name = student_data[name_start : name_end]
    student['Name'] = name
    i = name_end

    # Get marks 
    Marks = {}
    # DS
    subCode_start = student_data.find(DS, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['DS'] = int(marks)
   
    #CO
    subCode_start = student_data.find(CO, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['CO'] = int(marks)
        
    #DELD
    subCode_start = student_data.find(DELD, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['DELD'] = int(marks)

    #FDS
    subCode_start = student_data.find(FDS, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['FDS'] = int(marks)

    #PSOOP
    subCode_start = student_data.find(PSOOP, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['PSOOP'] = int(marks)

    #DELD Prac
    subCode_start = student_data.find(DELD_ORAL_PRAC, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "20"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['DELD_PRAC'] = int(marks)

    #DELD Oral
    subCode_start = student_data.find(DELD_ORAL_PRAC, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "20"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['DELD_ORAL'] = int(marks)
    
    #PL TermWork
    subCode_start = student_data.find(PL, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "20"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['PL_PRAC'] = int(marks)

    #PL Prac
    subCode_start = student_data.find(PL, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "20"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['PL_TW'] = int(marks)

    #Communication TW
    subCode_start = student_data.find(CLL, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "20"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['CLL'] = int(marks)

    total = 0
    for sub in Marks :
        total += Marks[sub]
    Marks['TOTAL'] = total

    # Add Marks[] to student[]
    student['Marks'] = Marks

    #Add student to db
    student_db.append(student)






# COMP
while True :
    rec_start = pdf.find(COMP_Roll, current_pos)
    if rec_start == -1:
        break
    # Find end of current record
    rec_end = pdf.find(RECORD_DELIM, rec_start)
    # Dictionary to map roll number, name, marks...
    student = {}
    student['Branch'] = 'COMP'
    # Slice student data from pdf and move current_pos to next student position
    student_data = pdf[rec_start : rec_end]
    current_pos = rec_end
    # Get roll
    roll_num = ""
    i = 0
    while student_data[i] != ' ' :
        roll_num += student_data[i]
        i += 1
    student['RollNum'] = roll_num

    # Get full name
    # Skip whitespaces
    while not student_data[i].isalpha() :
        i += 1
    name_start = i
    name_end = student_data.find(NAME_DELIM, name_start)
    name = student_data[name_start : name_end]
    student['Name'] = name
    i = name_end

    # Get marks 
    Marks = {}
    # COMP_DS
    subCode_start = student_data.find(COMP_DS, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['COMP_DS'] = int(marks)
   
    # DSPS
    subCode_start = student_data.find(DSPS, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['DSPS'] = int(marks)
        
    #DSPS PR
    subCode_start = student_data.find(DSPS, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "20"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['DSPS_PRAC'] = int(marks)

    #COMP_DELD
    subCode_start = student_data.find(COMP_DELD, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['COMP_DELD'] = int(marks)

    #DELD_TW
    subCode_start = student_data.find(COMP_DELD, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "10"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['COMP_DELD_TW'] = int(marks)

    #OSA
    subCode_start = student_data.find(OSA, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['OSA'] = int(marks)

    #OSA TW
    subCode_start = student_data.find(OSA, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "10"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['OSA_TW'] = int(marks)
    
    #OSA Prac
    subCode_start = student_data.find(OSA, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "20"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['OSA_PRAC'] = int(marks)

    #MPA
    subCode_start = student_data.find(MPA, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "40"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['MPA'] = int(marks)

    #MPA TW
    subCode_start = student_data.find(MPA, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "10"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['MPA_TW'] = int(marks)

    #MPA Oral
    subCode_start = student_data.find(MPA, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "20"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['MPA_ORAL'] = int(marks)

    #SS
    subCode_start = student_data.find(SS, i)
    subCode_end = student_data.find(' ', subCode_start)
    pass_marks = "10"
    i = student_data.find(pass_marks, subCode_end)
    #skip pass marks
    while student_data[i] != ' ':
        i += 1
    # now skip spaces and then save actual marks
    while student_data[i] == ' ':
        i += 1
    # Save
    marks = ""
    while student_data[i] != ' ':
        marks += student_data[i]
        i += 1
    if marks == 'AA':
        marks = '0'
    Marks['SS'] = int(marks)

    total = 0
    for sub in Marks :
        total += Marks[sub]
    Marks['TOTAL'] = total

    # Add Marks[] to student[]
    student['Marks'] = Marks

    #Add student to db
    student_db.append(student)


main_choice = int(raw_input("\nChoose filtering criteria:\n1. Overall Ranks(All Branches)\n2. ENTC\n3. IT\n4. COMP\n"))

if main_choice == 1:
    choices = '1. Find Your Rank\n2. View everyone\'s rank'
    print choices
    print 'Enter your choice: '
    initial_choice = int(raw_input())
    if initial_choice==1:
        getRank(student_db,'TOTAL')
    else:
        sorted_list = sorted(student_db, key=lambda k: k['Marks']['TOTAL'])
        total_students = len(student_db)
        rank = 0
        for i in sorted_list :
            for sub in i['Marks'] :
                print("       %12s : %s " %(sub, i['Marks'][sub]))
            print(" %s %25s         Branch: %4s  Rank : %d" %(i['RollNum'], i['Name'], i['Branch'], total_students-rank))
            rank += 1
        plotGraph(750, 12, student_db, 'TOTAL')


elif main_choice == 2:
    entc_db = []
    for entry in student_db :
        if entry['Branch'] == "ENTC" :
            entc_db.append(entry)

    choice = int(raw_input("\n Choose sorting criteria: \n 1. SS  2. SS Term Work  3. EDC  4. EDC_PRAC  5. NT  6.NT Term Work  \n 7.DSA  8. DSA Oral  9. DE 10. DE_PRAC Score  11. EMIT  12. Overall Score\n"))

    choiceMap = { 
        1 : 'SS_ENTC',
        2 : 'SS_TW',
        3 : 'EDC',
        4 : 'EDC_PRAC',
        5 : 'NT',
        6 : 'NT_TW',
        7 : 'DSA',
        8 : 'DSA_ORAL',
        9 : 'DE',
        10 : 'DE_PRAC',
        11 : 'EMIT',
        12 : 'TOTAL'
        }

    if choice < 1 or choice > 12 :
        print "wrong choice"
    else:
        choices = '1. Find Your Rank\n2. View everyone\'s rank'
        print choices
        print 'Enter your choice: '
        initial_choice = int(raw_input())
        if initial_choice==1:
            getRank(entc_db, choiceMap[choice])
        else:
            sorted_list = sorted(entc_db, key=lambda k: k['Marks'][choiceMap[choice]])
            total_students = len(entc_db)
            rank = 0
            for i in sorted_list :
                print(" %s %35s     Rank : %d" %(i['RollNum'], i['Name'], total_students-rank))
                rank += 1
                for sub in i['Marks'] :
                    print("       %12s : %s " %(sub, i['Marks'][sub]))
            if choiceMap[choice] == 'TOTAL' :
                plotGraph(750,12,entc_db,'TOTAL')
            else:
                plotGraph(100,20,entc_db,choiceMap[choice])    
    

elif main_choice == 3:
    it_db = []
    for entry in student_db :
        if entry['Branch'] == "IT" :
            it_db.append(entry)

    choice = int(raw_input(" Choose sorting criteria: \n 1. DS  2. FDS  3. CO  4. DELD  5. PSOOP  6.PL Prac  7.PL TW  8. DELD Prac  9. DELD Oral 10. Overall Score\n"))

    choiceMap = { 
        1 : 'DS',
        2 : 'FDS',
        3 : 'CO',
        4 : 'DELD',
        5 : 'PSOOP',
        6 : 'PL_PRAC',
        7 : 'PL_TW',
        8 : 'DELD_PRAC',
        9 : 'DELD_ORAL',
        10 : 'TOTAL'
    }

    if choice < 1 or choice > 11 :
        print "wrong choice"
    else:
        choices = '1. Find Your Rank\n2.  View everyone\'s rank'
        print choices
        print 'Enter your choice: '
        initial_choice = int(raw_input())
        if initial_choice==1:
            getRank(it_db, choiceMap[choice])
        else:
            sorted_list = sorted(it_db, key=lambda k: k['Marks'][choiceMap[choice]])
            total_students = len(it_db)
            rank = 0
            for i in sorted_list :
                print(" %s %35s     Rank : %d" %(i['RollNum'], i['Name'], total_students-rank))
                rank += 1
                for sub in i['Marks'] :
                    print("       %12s : %s " %(sub, i['Marks'][sub]))
            if choiceMap[choice] == 'TOTAL' :
                plotGraph(750,12,it_db,'TOTAL')
            else:
                plotGraph(100,20,it_db,choiceMap[choice])

elif main_choice == 4:
    comp_db = []
    for entry in student_db :
        if entry['Branch'] == "COMP" :
            comp_db.append(entry)
    choice = int(raw_input("\n Choose sorting criteria: \n 1. DS  2. DSPS  3. DSPS Practical  4. DELD  5. DELD TW  6. OSA  \n 7.OSA TW  8. OSA Prac  9. MPA 10. MPA TW  11. MPA Oral 12. SS  13. Overall Score\n"))

    choiceMap = { 
        1 : 'COMP_DS',
        2 : 'DSPS',
        3 : 'DSPS_PRAC',
        4 : 'COMP_DELD',
        5 : 'COMP_DELD_TW',
        6 : 'OSA',
        7 : 'OSA_TW',
        8 : 'OSA_PRAC',
        9 : 'MPA',
        10 : 'MPA_TW',
        11 : 'MPA_ORAL',
        12 : 'SS',
        13 : 'TOTAL'
    }

    if choice < 1 or choice > 13 :
        print "wrong choice"
    else:
        choices = '1. Find Your Rank\n2. View everyone\'s rank'
        print choices
        print 'Enter your choice: '
        initial_choice = int(raw_input())
        if initial_choice==1:
            getRank(comp_db, choiceMap[choice])
        else:
            sorted_list = sorted(comp_db, key=lambda k: k['Marks'][choiceMap[choice]])
            total_students = len(comp_db)
            rank = 0
            for i in sorted_list :
                print(" %s %35s     Rank : %d" %(i['RollNum'], i['Name'], total_students-rank))
                rank += 1
                for sub in i['Marks'] :
                    print("       %12s : %s " %(sub, i['Marks'][sub]))
            if choiceMap[choice] == 'TOTAL' :
                plotGraph(750,12,comp_db,'TOTAL')
            else:
                plotGraph(100,20,comp_db,choiceMap[choice])
else:
    print "Invalid Option"

