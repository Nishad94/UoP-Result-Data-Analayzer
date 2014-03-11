import os

MATH_PLOT = True
try:
    import matplotlib.pyplot as plt
except ImportError, e:
    MATH_PLOT = False

from collections import Counter

CURRENT_DIR = os.path.dirname(__file__)

PDF_FILE_ItEntc_PICT = "result_itentc_pict.pdf"
PDF_FILE_COMP_PICT = "result_comp_pict.pdf"
PDF_FILE_ItEntc_MIT = "result_itentc_mit.pdf"
PDF_FILE_COMP_MIT = "result_comp_mit.pdf"
OUT_FILE_ItEntc_MIT = "out_it_MIT.txt"
OUT_FILE_COMP_MIT = "out_comp_MIT.txt"
OUT_FILE_ItEntc_PICT = "out_it_PICT.txt"
OUT_FILE_COMP_PICT = "out_comp_PICT.txt"

'''os.system(("ps2ascii %s %s") %(PDF_FILE_ItEntc_PICT, OUT_FILE_ItEntc_PICT))
os.system(("ps2ascii %s %s") %(PDF_FILE_COMP_PICT, OUT_FILE_COMP_PICT))
os.system(("ps2ascii %s %s") %(PDF_FILE_ItEntc_MIT, OUT_FILE_ItEntc_MIT))
os.system(("ps2ascii %s %s") %(PDF_FILE_COMP_MIT, OUT_FILE_COMP_MIT))

filenames = ['out_it_PICT.txt', 'out_comp_PICT.txt', 'out_it_MIT.txt', 'out_comp_MIT.txt']
with open(os.path.join(CURRENT_DIR, 'out_combined_PICT_MIT.txt'), 'w') as outfile:
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
                    student_record = student
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
            for field in student_record['Marks'] :
                print("       %12s : %s " %(field, student_record['Marks'][field]))
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
                if student['RollNum'] == query:
                    student_record = student
                rank += 1
            print '\n---------------------------'
            print 'Roll No: ' + str(query) + '    ' + ranklist[query][1]
            print 'Your rank in {0} is {1}'.format(filter_field, ranklist[query][0])
            for field in student_record['Marks'] :
                print("       %12s : %s " %(field, student_record['Marks'][field]))
            print '---------------------------'
        except KeyError:
            print 'You entered an invalid Roll Number.\n'
    else:
        print 'Invalid choice!'
    exit()

####

### Generalized graph plotting function
def plotGraph(xRange, yRange, student_db, subField, customLabel):
    xRange += 1
    len_x_axis = xRange
    len_y_axis = yRange

    list_x_axis=[]
    list_y_axis_pict=[]
    list_y_axis_mit=[]

    for i in range(len_x_axis):
        list_x_axis.append(i)

    all_scores_cnt_pict = Counter() # { score: number_of_students_with_that_score }
    all_scores_cnt_mit = Counter() # { score: number_of_students_with_that_score }

    all_totals_pict = []
    all_totals_mit = []

    for student in student_db:
        marks = int(student['Marks'][subField])
        if student['College'] == 'PICT' :
            all_scores_cnt_pict[marks] += 1
        elif student['College'] == 'MIT':
            all_scores_cnt_mit[marks] += 1

    number_of_students_with_that_score = [] # Mapping index to number of students

    for i in range(xRange):
        number_of_students_with_that_score.append(all_scores_cnt_pict[i])

    list_y_axis_pict = number_of_students_with_that_score

    number_of_students_with_that_score = []

    for i in range(xRange):
        number_of_students_with_that_score.append(all_scores_cnt_mit[i])

    list_y_axis_mit = number_of_students_with_that_score
    
    plt.plot(list_x_axis, list_y_axis_pict, 'r', label='PICT')
    plt.plot(list_x_axis, list_y_axis_mit, 'b', label='MIT')
    plt.title(customLabel)
    plt.ylabel('No. of students')
    plt.xlabel('Marks')
    plt.axis([0, xRange, 0, yRange])
    plt.grid(True)
    plt.legend()
    plt.show()

    #### END OF MATPLOTLIB Function



f = open('out_combined_PICT_MIT.txt','r')
pdf = f.read()

IT_Roll_PICT = 'S120058'
IT_Roll_MIT = 'S120028'
''' Subject Codes'''
DS = '214441'
CO = '214442'
DELD = '214443'
FDS = '214444'
PSOOP = '214445'
DELD_ORAL_PRAC = '214446'
PL = '214447'
CLL = '214448'

COMP_Roll_PICT = 'S120054'
COMP_Roll_MIT = 'S120024'
''' Subject Codes'''
COMP_DS = '210241'
DSPS = '210242'
COMP_DELD = '210243'
OSA = '210244'
MPA = '210245'
SS = '210246'

ENTC_Roll_PICT = 'S120053'
ENTC_Roll_MIT = 'S120023'
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
def extractEntcData(Entc_Roll_Pattern, College):
    global student_db
    global current_pos
    while True :
        rec_start = pdf.find(Entc_Roll_Pattern, current_pos)
        if rec_start == -1:
            break
        # Find end of current record
        rec_end = pdf.find(RECORD_DELIM, rec_start)
        # Dictionary to map roll number, name, marks...
        student = {}
        student['College'] = College
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



#IT
def extractItData(IT_Roll_Pattern, College):
    global student_db
    global current_pos
    while True :
        rec_start = pdf.find(IT_Roll_Pattern, current_pos)
        if rec_start == -1:
            break
        # Find end of current record
        rec_end = pdf.find(RECORD_DELIM, rec_start)
        # Dictionary to map roll number, name, marks...
        student = {}
        student['College'] = College
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
        Marks['PL_TW'] = int(marks)

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
        Marks['PL_PRAC'] = int(marks)

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
def extractCompData(COMP_Roll_Pattern, College):
    global student_db
    global current_pos
    while True :
        rec_start = pdf.find(COMP_Roll_Pattern, current_pos)
        if rec_start == -1:
            break
        # Find end of current record
        rec_end = pdf.find(RECORD_DELIM, rec_start)
        # Dictionary to map roll number, name, marks...
        student = {}
        student['College'] = College
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



# Process Data
extractEntcData(ENTC_Roll_PICT, 'PICT')
extractItData(IT_Roll_PICT, 'PICT')
extractCompData(COMP_Roll_PICT, 'PICT')
extractEntcData(ENTC_Roll_MIT, 'MIT')
extractItData(IT_Roll_MIT, 'MIT')
extractCompData(COMP_Roll_MIT, 'MIT')



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
            print(" %s %25s   %4s    Branch: %4s  Rank : %d" %(i['RollNum'], i['Name'], i['College'], i['Branch'], total_students-rank))
            for sub in i['Marks'] :
                print("       %12s : %s " %(sub, i['Marks'][sub]))
            rank += 1
        if(MATH_PLOT == True):
            plotGraph(750, 11, student_db, 'TOTAL', 'UoP Sem 3[Comp + IT + Entc]')


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
                print(" %s %35s  %4s   Rank : %d" %(i['RollNum'], i['Name'], i['College'], total_students-rank))
                rank += 1
                for sub in i['Marks'] :
                    print("       %12s : %s " %(sub, i['Marks'][sub]))
            if MATH_PLOT == True:
                if choiceMap[choice] == 'TOTAL' :
                    plotGraph(750,5,entc_db,'TOTAL', 'UoP Sem 3 [Entc]')
                else:
                    plotGraph(100,20,entc_db,choiceMap[choice], 'UoP Sem 3 [Entc]')    
    

elif main_choice == 3:
    it_db = []
    for entry in student_db :
        if entry['Branch'] == "IT" :
            it_db.append(entry)

    choice = int(raw_input(" Choose sorting criteria: \n 1. DS  2. FDS  3. CO  4. DELD  5. PSOOP  6.PL Prac  7.PL TW  8. DELD Prac  9. DELD Oral 10. CLL 11. Overall Score\n"))

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
        10 : 'CLL',
        11 : 'TOTAL'
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
                print(" %s %35s  %4s   Rank : %d" %(i['RollNum'], i['Name'], i['College'], total_students-rank))
                rank += 1
                for sub in i['Marks'] :
                    print("       %12s : %s " %(sub, i['Marks'][sub]))
            if MATH_PLOT == True:
                if choiceMap[choice] == 'TOTAL' :
                    plotGraph(750,5,it_db,'TOTAL','UoP Sem 3 [IT]')
                else:
                    plotGraph(100,20,it_db,choiceMap[choice],'UoP Sem 3 [IT]')

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
                print(" %s %35s  %4s   Rank : %d" %(i['RollNum'], i['Name'], i['College'], total_students-rank))
                rank += 1
                for sub in i['Marks'] :
                    print("       %12s : %s " %(sub, i['Marks'][sub]))
            if MATH_PLOT == True:
                if choiceMap[choice] == 'TOTAL' :
                    plotGraph(750,6,comp_db,'TOTAL','UoP Sem 3 [Comp]')
                else:
                    plotGraph(100,20,comp_db,choiceMap[choice],'UoP Sem 3 [Comp]')
    
else:
    print "Invalid Option"

