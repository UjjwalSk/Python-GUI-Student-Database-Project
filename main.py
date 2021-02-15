from tkinter import *
from tkinter import ttk 
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import tix
import json

win=Tk()
win.title("Student Record Keeping Application") 
win.configure(background='black')  
students_list_main={'Students':[]}
courses_list_main={'Courses':[]}
allocation_list_main={'Stu_Course':[]}
style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Black',11))
style.configure("Treeview",font=('Calibri', 12))  
temp3=[] 
temp4=[] 
temp5=[]
temp6=[]

#--Creating JSON files--

#----Students-file----

try :
    f= open ('Student.json','x')
    with open ('Student.json','w') as st_file:
        json.dump(students_list_main,st_file)
except:
    pass

with open ('Student.json','r') as st_file:
    temp6=json.load(st_file)
temp6=temp6['Students']
temp7=[]
for i in temp6:
    temp7.append(i['Rollno'])        

#----Courses-file----

try :
    f= open ('Courses.json','x')
    with open ('Courses.json','w') as st_file:
        json.dump(courses_list_main,st_file)
except:
    pass

with open ('Courses.json','r') as st_file:
            temp_data=json.load(st_file)
temp_data=temp_data['Courses']
for i in temp_data: 
    temp4.append(i['CourseID']) 
for i in temp_data: 
    temp5.append(i['CourseName']) 

#----Allocation-file----

try :
    f= open ('Allocation.json','x')
    with open ('Allocation.json','w') as st_file:
        json.dump(allocation_list_main,st_file)
except:
    pass

#--Functions for whole program--

#--Functions for Tab1,Tab2(New Student , Display Tab)--
def saved():
    if e1.get()=='' or e2.get()=='' or e3.get()=='' or e4.get()=='':
        messagebox.showinfo('Incorrect','Please fill information properly!!!')
        pass 
    elif (e2.get() in temp7):
        messagebox.showinfo('Already','RollNo. Already Exists')
        pass    
    else:
        messagebox.showinfo('Save','Your record has been saved')
        temp=var.get()
        temp2=CheckVar1.get()
        if (temp==1):
            temp='Male'
        else:
            temp='Female'
        if (temp2==0):
            temp2='False'
        else:
            temp2='True'
        students_tree.insert('',0,values=(e2.get(),e1.get(),temp,e3.get(),e4.get(),batch.get(),temp2))
        with open ('Student.json','r') as st_file:
            data=json.load(st_file)
        data['Students'].append({'Rollno':e2.get(),'Name':e1.get(),'Gender':temp,'Address':e3.get(),'PhoneNo':e4.get(),'Batch':batch.get(),'Hostel':temp2})
        with open ('Student.json','w') as st_file:
            json.dump(data,st_file,indent=4)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END) 
        batch.set('')
        C1.deselect() 

def cleared():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END) 
    batch.set('')
    C1.deselect() 

def show_students():
    students_tree.pack(fill=X)
    show.pack_forget()
    hide.pack(side=BOTTOM)

def hide_students():
    students_tree.pack_forget()
    show.pack(side=BOTTOM)
    hide.pack_forget()

#--Functions for Tab3,Tab4(Course Creation , Display Courses)--
 
def course_saved():
    if e5.get()=='' or e6.get()=='':
        messagebox.showinfo('Incorrect','Please fill information properly!!!')
        pass
    elif (e5.get() in temp4):
        messagebox.showinfo('Already','CourseID Already Exists')
        pass
    else:
        messagebox.showinfo('Save','Course Created')
        courses_tree.insert('',0,values=(e5.get(),e6.get()))  
        with open ('Courses.json','r') as st_file:
            data=json.load(st_file)
        data['Courses'].append({'CourseID':e5.get(),'CourseName':e6.get()})
        with open ('Courses.json','w') as st_file:
            json.dump(data,st_file,indent=4) 
        temp5.append(e6.get())
        courses['values'] = temp5  
        e5.delete(0,END)
        e6.delete(0,END) 

def course_cleared():
    e5.delete(0,END)
    e6.delete(0,END)

def show_courses():
    courses_tree.pack()
    show_course.pack_forget()
    hide_course.pack(side=BOTTOM)

def hide_courses():
    courses_tree.pack_forget()
    show_course.pack(side=BOTTOM)
    hide_course.pack_forget()

#--Functions for Tab5,Tab6(Course Allocation , Display Allocated Courses)--

def allocate_courses():
    if e7.get()=='':
        messagebox.showinfo('Incorrect','Please fill information properly!!!')
        pass
    else:
        messagebox.showinfo('Save','Course Allocated') 
        allocated_courses_tree.insert('',0,values=(e7.get(),courses.get())) 
        with open ('Allocation.json','r') as st_file:
            data=json.load(st_file)
        with open ('Courses.json','r') as st_file:
            courseID=json.load(st_file)
        courseID=courseID['Courses']
        for i in courseID:
            if (i['CourseName']==courses.get()):
                Id=i['CourseID']
        data['Stu_Course'].append({'Rollno':e7.get(),'CourseID':Id})
        with open ('Allocation.json','w') as st_file:
            json.dump(data,st_file,indent=4)
        e7.delete(0,END)
        courses.set('') 

def allocate_cleared():
    e7.delete(0,END)
    courses.set('') 

def show_allocated_courses():
    allocated_courses_tree.pack()
    show_allocated_course.pack_forget()
    hide_allocated_course.pack(side=BOTTOM)

def hide_allocated_courses():
    allocated_courses_tree.pack_forget()
    show_allocated_course.pack(side=BOTTOM)
    hide_allocated_course.pack_forget()


# Top-Section with university name

f1=Frame(win,height=50,bg='black')
f1.pack(fill=X)

for i in range(2):
    f1.rowconfigure(i,weight=1)
for i in range(3):
    f1.columnconfigure(i,weight=1)

feyp=Frame(f1,bg='black')
feyp.grid(row=0,column=0,sticky=W,padx=(10,0),pady=10)

l1=Label(feyp,text='EXPLORE',font=('arial',12,'bold'),fg='red',bg='black')
l1.pack(anchor=W)
l2=Label(feyp,text='YOUR',font=('arial',12,'bold'),fg='white',bg='black')
l2.pack(anchor=W)
l3=Label(feyp,text='POTENTIAL',font=('arial',12,'bold'),fg='red',bg='black')
l3.pack(anchor=W)

l4=Label(f1,text='Chitkara University',font=('arial',25),fg='white',bg='black')
l4.grid(row=0,column=1,sticky=N)

l5=Label(f1,text='STUDENT DATABASE',font=('Times New Roman',18),fg='white',bg='black')
l5.grid(row=1,column=1)

try:
    side_logo_img=Image.open('.\Chitkara University logo.jpg')
    resized_side_logo_img=side_logo_img.resize((160,60),Image.ANTIALIAS)
    side_logo_new_img=ImageTk.PhotoImage(resized_side_logo_img)
    Label(f1,image=side_logo_new_img).grid(row=0,column=2,sticky=NE)
except:
    Label(f1,text='📸Logo Image \nHere',fg='white',bg='black').grid(row=0,column=2,sticky=NE)


#-- Creating Tabs --

f2=Frame(win,bg='black')
f2.pack()

try:
    side_logo_img2=Image.open('.\python project logo.jpg')
    resized_side_logo_img2=side_logo_img2.resize((130,80),Image.ANTIALIAS)
    side_logo_new_img2=ImageTk.PhotoImage(resized_side_logo_img2)
    Label(f2,image=side_logo_new_img2).pack(side=LEFT)
except:
    Label(f2,text='📸Logo Image \nHere',fg='white',bg='black').pack(side=LEFT)

fTabs=Frame(f2)
fTabs.pack(fill ="both",side=LEFT,padx=(0,80)) 

tabControl = ttk.Notebook(fTabs) 
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='New Student') 
tabControl.add(tab2, text ='Display') 
tabControl.add(tab3, text ='Course Creation')
tabControl.add(tab4, text ='Display Courses')
tabControl.add(tab5, text ='Course Allocation')
tabControl.add(tab6, text ='Display Courses Allocated')
tabControl.pack(padx=8,pady=8)

#---New Student Tab---

for i in range (8):
    tab1.rowconfigure(i,weight=1)
for i in range (5):
    tab1.columnconfigure(i,weight=1)

Label(tab1,text ="Enter Your Name",font=("Calibri",14),pady=8).grid(row = 0,column = 0,sticky='E') 
e1=ttk.Entry(tab1,width=50,font=('Calibri', 12))
e1.grid(row=0,column=3,columnspan=2,sticky='E')
Label(tab1,text ="Enter Your Rollno",font=("Calibri",14),pady=8).grid(row = 1,column = 0,sticky='E') 
e2=ttk.Entry(tab1,width=50,font=('Calibri', 12))
e2.grid(row=1,column=3,columnspan=2,sticky='E')

Label(tab1,text ="Choose your Gender",font=("Calibri",14),pady=8).grid(row = 2,column = 0,sticky='E') 

var = IntVar()
rb1=Radiobutton(tab1,text='Male',variable=var,value=1)
rb1.grid(row=2,column=3,sticky=W)
rb2=Radiobutton(tab1,text='Female',variable=var,value=2)
rb2.grid(row=2,column=4,sticky=E)

Label(tab1,text ="Address for Correspondance",font=("Calibri",14),pady=8).grid(row = 3,column = 0,sticky='E') 
e3=ttk.Entry(tab1,width=50,font=('Calibri', 12))
e3.grid(row=3,column=3,columnspan=2,sticky='E')

Label(tab1,text ="Phone No",font=("Calibri",14),pady=8).grid(row = 4,column = 0,sticky='E') 
e4=ttk.Entry(tab1,width=50,font=('Calibri', 12))
e4.grid(row=4,column=3,columnspan=2,sticky='E')

Label(tab1,text ="Your Batch",font=("Calibri",14)).grid(row = 5,column = 0,sticky='E')  
n = StringVar()  
batch = ttk.Combobox(tab1, width = 27,textvariable = n,state="readonly",font=('Calibri', 12))  
batch['values'] = ('Batch 2018','Batch 2019','Batch 2020')      
batch.grid(row=5,column=3,columnspan=2,sticky='E')

Label(tab1,text='Hostel[Y/N]',font=("Calibri",14),pady=8).grid(row = 6,column = 0,sticky='SE')
CheckVar1 = IntVar() 
C1 = Checkbutton(tab1,text = "Click if you need Hostel Facility",variable = CheckVar1,onvalue = 1, offvalue = 0,font=('Calibri', 12),pady=8)
C1.grid(row = 6,column = 4,sticky='E')

btn=Button(tab1,text='Save',font=("Calibri",11),width=14,command=saved)
btn.grid(row=7,column=1,pady=(23,1),padx=60) 

Button(tab1,text='Clear',font=("Calibri",12),width=14,command=cleared).grid(row=7,column=2,pady=(20,1))
 
Label(tab1,text='').grid(row=8,column=0)  


#---Display Tab---

col=('Rollno','Name','Gender','Address','PhoneNo','Batch','Hostel')
students_tree=ttk.Treeview(tab2,height=15,show='headings',columns=col)

students_tree.column('Rollno',width=50,anchor=W)
students_tree.column('Name',width=100,anchor=E)
students_tree.column('Gender',width=70,anchor=W)
students_tree.column('Address',width=100,anchor=W)
students_tree.column('PhoneNo',width=100,anchor=W)
students_tree.column('Batch',width=100,anchor=W)
students_tree.column('Hostel',width=60,anchor=E)

students_tree.heading('Rollno',text='Rollno',anchor=W)
students_tree.heading('Name',text='Name   ',anchor=E)
students_tree.heading('Gender',text='Gender',anchor=W)
students_tree.heading('Address',text='Address',anchor=W)
students_tree.heading('PhoneNo',text='PhoneNo',anchor=W)
students_tree.heading('Batch',text='Batch',anchor=W)
students_tree.heading('Hostel',text='Hostel',anchor=E) 

with open ('Student.json','r') as st_file:
        display=json.load(st_file)
display=display['Students'] 
for i in display:
    k=0
    for j in i.values() : 
        temp3.append(j)
    students_tree.insert('',k,values=(temp3[0],temp3[1],temp3[2],temp3[3],temp3[4],temp3[5],temp3[6]))
    k+=1
    temp3=[] 

show=Button(tab2,text='Show Students',font=(12),bg='black',fg='white',padx=30,command=show_students)
show.pack(side=BOTTOM)
hide=Button(tab2,text='Hide Students',font=(12),bg='black',fg='white',padx=30,command=hide_students)

#---Course Creation Tab---

f3=Frame(tab3,width=700,height=200)
f3.pack()
f4=Frame(tab3,width=700,height=200)
f4.pack()
f5=Frame(tab3,width=700,height=200)
f5.pack()
Label(f3,text='Course ID',font=("Calibri",14),padx=100).pack(side=LEFT,anchor=CENTER,pady=(100,10))
e5=ttk.Entry(f3,width=50,font=('Calibri', 12))
e5.pack(side=RIGHT,anchor=CENTER,pady=(100,10))

Label(f4,text='Course Name',font=("Calibri",14),padx=86).pack(side=LEFT,anchor=CENTER,pady=10)
e6=ttk.Entry(f4,width=50,font=('Calibri', 12))
e6.pack(side=RIGHT,anchor=CENTER,pady=10)
Button(f5,text='Save',font=("Calibri",11),width=14,command=course_saved).pack(side=LEFT,anchor=CENTER,pady=(23,1),padx=60)
Button(f5,text='Clear',font=("Calibri",12),width=14,command=course_cleared).pack(side=RIGHT,anchor=CENTER,pady=(20,1),padx=60)

#--Display Courses Tab--

col=('CourseID','CourseName')
courses_tree=ttk.Treeview(tab4,height=15,show='headings',columns=col)

courses_tree.column('CourseID',width=200,anchor=W)
courses_tree.column('CourseName',width=400,anchor=E)

courses_tree.heading('CourseID',text='CourseID',anchor=W)
courses_tree.heading('CourseName',text='CourseName',anchor=E)

with open ('Courses.json','r') as st_file:
        course_display=json.load(st_file)
course_display=course_display['Courses'] 
for i in course_display: 
    k=0
    for j in i.values() : 
        temp3.append(j)
    courses_tree.insert('',k,values=(temp3[0],temp3[1]))
    k+=1
    temp3=[] 

show_course=Button(tab4,text='Show Courses',font=(12),bg='black',fg='white',padx=30,command=show_courses)
show_course.pack(side=BOTTOM)
hide_course=Button(tab4,text='Hide Courses',font=(12),bg='black',fg='white',padx=30,command=hide_courses)

#---Course Allocation Tab---

f6=Frame(tab5,width=700,height=200)
f6.pack()
f7=Frame(tab5,width=700,height=200)
f7.pack()
f8=Frame(tab5,width=700,height=200)
f8.pack()
Label(f6,text='Student Rollno',font=("Calibri",14),padx=100).pack(side=LEFT,anchor=CENTER,pady=(100,10))
e7=ttk.Entry(f6,width=50,font=('Calibri', 12))
e7.pack(side=RIGHT,anchor=CENTER,pady=(100,10))

Label(f7,text='Course Name',font=("Calibri",14),padx=105).pack(side=LEFT,anchor=CENTER,pady=10)
m = StringVar() 
courses = ttk.Combobox(f7, width = 48,textvariable = m,state="readonly",font=('Calibri', 12))  
courses['values'] = temp5      
courses.pack(side=RIGHT,anchor=CENTER,pady=10)

Button(f8,text='Allocate',font=("Calibri",12),width=14,command=allocate_courses).pack(side=LEFT,anchor=CENTER,pady=(23,1),padx=60)
Button(f8,text='Clear',font=("Calibri",12),width=14,command=allocate_cleared).pack(side=RIGHT,anchor=CENTER,pady=(20,1),padx=60)

#--Display Courses Allocated Tab--

col=('Rollno','CourseName')
allocated_courses_tree=ttk.Treeview(tab6,height=15,show='headings',columns=col)

allocated_courses_tree.column('Rollno',width=200,anchor=W)
allocated_courses_tree.column('CourseName',width=400,anchor=E)

allocated_courses_tree.heading('Rollno',text='Rollno',anchor=W)
allocated_courses_tree.heading('CourseName',text='CourseName',anchor=E)

try:
    temp10={}
    with open ('Allocation.json','r') as st_file:
        courseID=json.load(st_file)
    courseID=courseID['Stu_Course']   
    for i in courseID:
        temp10.update(i) 
        with open ('Courses.json','r') as st_file:
            courseTitle=json.load(st_file)
        courseTitle=courseTitle['Courses']
        for j in courseTitle:
            if (j['CourseID']==temp10['CourseID']):
                temp10['CourseName']=j['CourseName']
        allocated_courses_tree.insert('','end',values=(temp10['Rollno'],temp10['CourseName']))
        temp10={}
except:
    pass

show_allocated_course=Button(tab6,text='Show Allocated Courses',font=(12),bg='black',fg='white',padx=30,command=show_allocated_courses)
show_allocated_course.pack(side=BOTTOM)
hide_allocated_course=Button(tab6,text='Hide Allocated Courses',font=(12),bg='black',fg='white',padx=30,command=hide_allocated_courses)

#--Bottom Title--

Label(text='Department of Computer Science & Engineering',font=('Impact',12),bg='black',fg='white').pack(pady=(30,50))

win.mainloop()  
