import os
#import matplotlib.pyplot as plt
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


main_choice = int(raw_input(" Choose sorting criteria:\n 1. Overall Ranks(All Branches)  2. ENTC  3. IT  4. COMP\n"))

if main_choice == 1:
    sorted_list = sorted(student_db, key=lambda k: k['Marks']['TOTAL'])
    total_students = len(sorted_list)
    rank = 0
    for i in sorted_list :
        print(" %s %25s         Branch: %4s  Rank : %d" %(i['RollNum'], i['Name'], i['Branch'],total_students - rank))
        rank += 1
        for sub in i['Marks'] :
            print("       %12s : %s " %(sub, i['Marks'][sub]))
    '''
    #### MATPLOTLOB COMMIT 1.
    #### Author: xennygrimmato

    # This commit tries to plot the distribution of Total Scores of students for the overall result

    # plt.plot ( [list_x_axis], [list_y_axis] )

    len_x_axis = 751 # There exist 751 possible scores --> [0,750]
    len_y_axis = total_students

    list_x_axis=[]
    list_y_axis=[]

    for i in range(0,751):
        list_x_axis.append(i)
    
    all_scores_cnt = Counter() # { score: number_of_students_with_that_score }

    all_totals = []

    for entry in student_db:
        all_totals.append(int(entry['Marks']['TOTAL']))

    for ith in all_totals:
        all_scores_cnt[ith]+=1

    #print all_scores_cnt

    number_of_students_with_that_score = [] # Mapping index to number of students

    for i in range(0,751):
        number_of_students_with_that_score.append(all_scores_cnt[i])

    temp_list = number_of_students_with_that_score
    list_y_axis = temp_list

    #print list_y_axis

    plt.plot(list_x_axis, list_y_axis, 'r')
    plt.ylabel('No. of students')
    plt.xlabel('Marks')
    plt.axis([0, 750, 0, 12])
    plt.grid(True)
    plt.show()

    #### END OF MATPLOTLIB COMMIT 1.
    '''
    
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
        sorted_list = sorted(entc_db, key=lambda k: k['Marks'][choiceMap[choice]])
        total_students = len(sorted_list)
        rank = 0
        for i in sorted_list :
            print(" %s %35s     Rank : %d" %(i['RollNum'], i['Name'], total_students - rank))
            rank += 1
            for sub in i['Marks'] :
                print("       %12s : %s " %(sub, i['Marks'][sub]))
    

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
        sorted_list = sorted(it_db, key=lambda k: k['Marks'][choiceMap[choice]])
        total_students = len(sorted_list)
        rank = 0
        for i in sorted_list :
            print(" %s %35s     Rank : %d" %(i['RollNum'], i['Name'], total_students - rank))
            rank += 1
            for sub in i['Marks'] :
                print("       %12s : %s " %(sub, i['Marks'][sub]))
    

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
        sorted_list = sorted(comp_db, key=lambda k: k['Marks'][choiceMap[choice]])
        total_students = len(sorted_list)
        rank = 0
        for i in sorted_list :
            print(" %s %35s     Rank : %d" %(i['RollNum'], i['Name'], total_students - rank))
            rank += 1
            for sub in i['Marks'] :
                print("       %12s : %s " %(sub, i['Marks'][sub]))
    
else:
    print "Invalid Option"

