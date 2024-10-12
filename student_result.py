
'''
CSV format:
================================================================================================
Rollno  Name    English    Tmaths Pmaths subT   Tphy Pphy subT  Tchem Pchem subT    Total   Division    PC
_
_
_
================================================================================================
'''


'''
Rusult Out Format:
========================================================

           XYZ SCHOOL
Name :
Rollno:
sub_Name    Theory  Pracrical   Sub_total
English                             |
Maths                               |
Physis                              |
Chemistry                           |
    
Total                           Total_Mark
Division: _
PC:      _
========================================================
'''
#SapamSushilSingh
'''first mini Project'''
import csv
from typing import List, Dict, Union
from operator import itemgetter
def print_format(record):
    print('='*60)
    try:
        print('\t\t\t XYZ School','\nName: ',record['Name'],'\nRollno: ',record['Rollno'])
        print(f"{'Sub_Name.':<6}{'Theory':>13}  {'Practical':^12}{'Sub_total':^24}{'\nEnglish  ':<6}{record['English']:>13}{" ":^12}{record['English']:^24}{'\nMaths    ':<6}{record['Tmaths']:>13}{record['Pmaths']:^12}{record['M_SubT']:^24}{'\nPhysis   ':<6}{record['Tphy']:>13}{record['Pphy']:^12}{record['P_SubT']:^24}{'\nChemistry':<6}{record['Tchem']:>13}{record['Pchem']:^12}{record['C_SubT']:^24}")
        print(f"{"\nTotal"}{record['Total']:>44}{"\nDivision: "}{record['Division']}{"\nPC: "}{record['PC']}")
    except TypeError:
        print(record)
    print('='*60)
    
def load_record():
    students=[]
    try:
        with open("student_rusult.csv",mode='r',newline="") as file:
            reader=csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print("",end="")
    return students
def insert_rollno():
    students=load_record()
    store_rollno=[]
    for i in students:
        temp=(i['Rollno'])
        store_rollno.append(temp)
    while True:
            rollno=input("Enter Rollno no: ")    
            if rollno not in store_rollno:
                return rollno
                break
            else:
                print("REPEATED ROLLNO \n ENTER AGAIN")

def theory_mark():
    while True:
        try:
            mark=float(input("Enter Theory mark: "))
            if mark<=75:
                return mark
                break
            else:
                print( "THEORY FULL MARK IS ONLY 75 ! ")
        except ValueError:
            print("Enter Mark!")
def practical_mark():
    while True:
        try:
            mark=float(input("Enter Practical mark: "))
            if mark<=25:
                return mark
                break
            else:
                print( "PRACTICAL FULL MARK IS ONLY 25 ! ")
        except ValueError:
            print("Enter Mark!")


def student_result():
    students=load_record()
    rollno=input("Enter student Rollno: ")
    for student in students:
        temp=(student["Rollno"])
        if rollno == temp:
            return student
    return 'Student Not Found'
    
def top_student():
    students=load_record()
    total_list=[]
    top_student='0'
    for total_mark in students:
        total_mark=total_mark["Total"]
        total_list.append(total_mark)
    for top_mark in total_list:
        if top_student<top_mark:
            top_student=top_mark
    for student in students:
        if student['Total']==top_student:
            return student
        
def poor_student():
    students=load_record()
    total_list=[]
    for total_mark in students:
        total_mark=total_mark["Total"]
        total_list.append(total_mark)
    poor_student=total_list[0]
    for poor_mark in total_list:
        if poor_student>=poor_mark:
            poor_student=poor_mark
    for record in students:
        if record['Total']==poor_student:
            return record
        
def display_students():
    display=load_record()
    print(f"{"Name":<7}{"Rollno"}")
    for i in display:
        print(f"{i["Rollno"]:<7}{i["Name"]}")    

def add_students(data):
    students=load_record()
    students.append(data)
    sort=[]
    for i in sorted(students,key=itemgetter('Rollno')):
        sort.append(i)
    header=["Rollno","Name","English","Tmaths","Pmaths","M_SubT","Tphy","Pphy","P_SubT","Tchem","Pchem","C_SubT","Total","Division","PC"]
    with open("student_rusult.csv",'w',newline="") as file:
        writer=csv.DictWriter(file,fieldnames=header)
        writer.writeheader()
        writer.writerows(sort)


def main():
    while True:
        print("="*40)
        print("\t1. Add Student Record")
        print("\t2. Student Result")
        print("\t3. Top Student Result")
        print("\t4. Poor Student Result")
        print("\t5. Display Students")
        print("\t6. Exit")
        print("="*40)
        try:
            n=int(input("Enter Your Choose: "))
        
            if n==1:
                print("*"*40)

                rollno=insert_rollno()

                name=input("Enter Name of the Student: ")
                #1display_std(name,rollno)

                print("_"*30)
                print("English")
                t_eng=0
                while True:
                    try:
                        temp=float(input(" Enter English  Mark: "))
                        if temp>=101:
                            print("Theory Full is only 100!")                        
                        else:
                            t_eng=temp
                            break
                    except ValueError:
                        print("Enter Mark!")
                
                print("maths")
                t_maths=theory_mark()
                p_maths=practical_mark()
                
                print("physis")
                t_physis=theory_mark()
                p_physis=practical_mark()

                print("Chemistry")
                t_chemistry=theory_mark()
                p_chemistry=practical_mark()
                print("*"*40)

                eng_mark=t_eng

                math_mark=t_maths+p_maths

                phy_mark=t_physis+p_physis

                chem_mark=t_chemistry+p_chemistry

                total=eng_mark+math_mark+phy_mark+chem_mark
                
                division=''
                if total>=300:
                    division='1'
                elif total>=200:
                    division='2'
                elif total>=100:
                    division='3'
                else:
                    division='Nil'
                
                percentage=total/400*100
                data={"Rollno":rollno,"Name":name,
                    "English":t_eng,
                    "Tmaths":t_maths,"Pmaths":p_maths,"M_SubT":math_mark,
                    "Tphy":t_physis,"Pphy":p_physis,"P_SubT":phy_mark,
                    "Tchem":t_chemistry,"Pchem":p_chemistry,"C_SubT":chem_mark,
                    "Total":total,"Division":division,"PC":percentage}
                add_students(data)
            elif n==2:
                record=student_result()
                print_format(record)
            elif n==3:
                record=top_student()
                print_format(record)
            elif n==4:
                record=poor_student()
                print_format(record)
            elif n==5:
                display_students()
            elif n==6:
                break
            else:
                print("Press 1 to 6 Option")
        except ValueError:
            print("Invalid Option!")
if __name__=="__main__":
    main()