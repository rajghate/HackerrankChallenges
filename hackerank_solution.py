import time
#challenge 1
def leap_year():
      year=int(input("Enter Year:"))
      leap=False
      if year%4==0 and year%100 !=0 or year%400 == 0 :
            leap=True

      print(leap)

#challenge 2
def print1ton():
      n=int(input("enter n :"))
      print("".join([str(x) for x in range(1,n+1)]))

#challenge 3
def secondlowestgrade():
      n=int(input("Number of records"))
      records=[]
      for _ in range(n):
            name=input("")
            score=float(input())
            records.append([name,score])
      l=list(set([x[1] for x in records]))
      l.sort()
      l2=[x[0] for x in records if x[1]==l[1]]
      l2.sort()
      print(l2)

def findingThePercentage():
      n = int(input("Enter Number of Students:"))
      student_marks = {}
      for _ in range(n):
            name, *line = input("Enter Student name and marks seprated by spaces \n").split()
            scores = list(map(float, line))
            student_marks[name] = scores
      query_name = input()
      print("{: .2f}".format(sum(student_marks[query_name])/len(student_marks[query_name])))
            
            

challenges_dict={
1:"""Leap year or not conditions:
year is perfectly divisible by 4 then leap year
      unless year is perfectly divisible by 100 then not a leap year
            unless year is perfectly divisble by 400""",

2:"""The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
123...n""",

3:"""Given the names and gradesfor each student in a class of N students,
store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.
""",
4:"""The provided code stub will read in a dictionary containing key/value
pairs of name:[marks] for a list of students. Print the average of the marks
array for the student name provided, showing 2 places after the decimal.
""",
}


for i in challenges_dict.keys():
      print("Challenge number "+str(i)+":"+challenges_dict[i]+"\n")
      time.sleep(2)
number=int(input("enter challenge number:"))

if number==1:leap_year()
elif number==2:print1ton()
elif number==3:secondlowestgrade()
elif number==4:findingThePercentage()
else:
      print("Wrong Choice")
      







      
