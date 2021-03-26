import os
import csv
from os.path import isfile, join

'''I have added comments where necessary'''
'''If you need help in configuring this for your assignment, drop an email at 22100136@lums.edu.pk. -Anna Mazhar '''

def nesting(path):
    """ counts how often `os.path.split` works on `path` """
    c = 0
    head = tail = path
    while head and tail:
        head, tail = os.path.split(head)
        c +=1
    return c

def longest_path( paths ):
        return max(paths, key=nesting)

def find_leaves( root ):
    """ finds folders with no subfolders """
    for root, dirs, files in os.walk(root):
        if not dirs: # can't go deeper
            yield root


'''use this to set the path to the submission of every student. This will give a list of paths of all students' submissions'''
def get_paths():
    path = "/home/anna/Downloads/PA1/ALL/"  #direct it to the folder which has all the zips extracted

    list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir()]

    paths_needed = []

    for i in list_subfolders_with_paths:
        #I had the name of the deepest folder as PA-1 so you can set the following as per your setting. In my case the directory was like .../ALL/22100136/PA-1/all_cpp_stuff
        p = longest_path(find_leaves(i)).partition('PA-1')[0] + 'PA-1/' 
        paths_needed.append(p)
  
    return paths_needed



def run_test(roll_num):
    
    marks = []     # this stores the marks for each part for a single student. This is appended to the csv file
    print(roll_num)
    marks.append(roll_num)
    marks.append('')

    '''PART 1'''
    if os.system('g++ test1.cpp') == 0:                       #catches uncompiled files
        print("Part 1 compiled!\n")
        if os.system('timeout 400 ./a.out > x') == 0:              #catches infinite loops, seg faults and exceptions
            f = open("x", "r")
            #the following string manipulation needs to be tweaked according to your test files output
            for i in f:                         
                if "Passed!" in i or "Failed!" in i or "Total Points:" in i:
                    marks.append((i.split()[-3]))
            f.close()
        else:
            print("Part 1 Seg fault or infinite loop.\n")
            f = open("x", "r")
            for i in f:
                if "Passed!" in i or "Failed!" in i or "Total Points:" in i:
                    marks.append((i.split()[-3]))
            f.close()
    else:
        print('Part 1 Compilation error\n')

    if len(marks) != 10:
        while(len(marks) < 10):
            marks.append(0)

    marks.append("")

    '''PART 2'''
    if os.system('g++ test2.cpp') == 0:
        print("Part 2 compiled!")
        if os.system('timeout 300 ./a.out > x') == 0:
            f = open("x", "r")
            for i in f:
                if "Passed!" in i or "Failed!" in i:
                    marks.append((i.split()[-3]))
            f.close()
        else:
            print("Part 2 Seg fault or infinite loop.")
            f = open("x", "r")
            for i in f:
                if "Passed!" in i or "Failed!" in i:
                    marks.append((i.split()[-3]))
            f.close()
    else:
        print('Part 2 Compilation error')

    if len(marks) != 13:
        while(len(marks) < 13):
            marks.append(0)

    marks.append("")

    '''PART 3'''
    if os.system('g++ test3.cpp') == 0:
        print("Part 3 compiled!")
        if os.system('timeout 50 ./a.out 197 > x') == 0:
            f = open("x", "r")
            for i in f:
                if "passed!" in i or "failed!" in i:
                    marks.append((i.split()[-1].split('/')[0]))
            f.close()
        else:
            print("Part 3 Seg fault or infinite loop.")
            f = open("x", "r")
            for i in f:
                if "passed!" in i or "failed!" in i:
                    marks.append((i.split()[-1].split('/')[0]))
            f.close()
    else:
        print('Part 3 Compilation error')

    if len(marks) != 16:
        while(len(marks) < 16):
            marks.append(0)

    marks.append("")

    '''PART 4'''
    if os.system('g++ test4.cpp') == 0:
        print("Part 4 compiled!")
        if os.system('timeout 50 ./a.out 100 > x') == 0:
            f = open("x", "r")
            for i in f:
                if "score:" in i:
                    marks.append((i.split()[-1].split('/')[0]))
            f.close()
        else:
            print("Part 4 Seg fault or infinite loop.")
            f = open("x", "r")
            for i in f:
                if "score:" in i:
                    marks.append((i.split()[-1].split('/')[0]))
            f.close()

    else:
        print('Part 4 Compilation error')

    if len(marks) != 18:
        while(len(marks) < 18):
            marks.append(0)

    with open("/home/anna/Semester_6/[TAship]DS/marks_sheet.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(marks)


'''copy the original tests and other files to every students' folders before running the tests'''
'''These og files must be in the current directory of this python script''' 
def copy_og_files(paths):
    for i in paths:
        os.system('cp test1.cpp ' + i)
        os.system('cp test2.cpp ' + i)
        os.system('cp test3.cpp ' + i)
        os.system('cp test4.cpp ' + i)
        os.system('cp assembly.txt ' + i) 
        os.system('cp takeaway.txt ' + i) 
        os.system('cp takeaway100.txt ' + i)
        os.system('cp topping_priority.txt ' + i)


def main():

    paths = get_paths()    #this requires manual uniforming of directories
    copy_og_files(paths)
 
    for i in paths:  
        os.chdir(i)  
        roll_num = i.split('/')[-3]
        run_test(roll_num)
        
main()