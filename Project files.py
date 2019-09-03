import os
from pickle import *
from validDate import *
t = open("no.txt", 'w')
t.write('0')
t.close()

print "TIP: Open in fullscreen for better user experience."

print"""

\t\t\t\t\t\t   _____ _ _            _     _____        _        _                   
\t\t\t\t\t\t  / ____| (_)          | |   |  __ \      | |      | |                   
\t\t\t\t\t\t | |    | |_  ___ _ __ | |_  | |  | | __ _| |_ __ _| |__   __ _ ___  ___ 
\t\t\t\t\t\t | |    | | |/ _ \ '_ \| __| | |  | |/ _` | __/ _` | '_ \ / _` / __|/ _ \ 
\t\t\t\t\t\t | |____| | |  __/ | | | |_  | |__| | (_| | || (_| | |_) | (_| \__ \  __/
\t\t\t\t\t\t  \_____|_|_|\___|_| |_|\__| |_____/ \__,_|\__\__,_|_.__/ \__,_|___/\___|
                                                                         
                                                     
                                                   
"""

class client:
    """Creates the class Client and defines its data members through the input() function.
        Displays data members through display() function."""

    def input(self,cn):
        self.name = raw_input("Enter Name   ")[:20]
        try:
            self.dob = raw_input("Enter DOB in dd-mm-yyyy format   ")[:10]
            l = self.dob.split('-')
            if not validdate(int(l[0]), int(l[1]), int(l[2])):
                self.dob = raw_input("Enter valid DOB   ")
        except: print "Please enter date in the correct format."
        self.panno = raw_input("Enter PAN   ")[:10]
        try:
            f=open("client.dat","rb")
            s1=client()
            while True:
                s1=load(f)
                if s1.panno==self.panno:
                    self.panno = raw_input("PAN already exists. Enter unique PAN   ") 
                    break
        except EOFError: pass
        except: print "Some error occurred."
        finally:
            f.close()
        self.telno = raw_input("Enter contact number   ")[:10]
        self.email = raw_input("Enter Email ID   ")[:20]
        self.cno=cn
        print         
        
    def display(self):
        print '+'*(153)
        print '|','\t',str(self.cno)+' '*(3-len(str(self.cno))),
        print '\t','|','\t',self.name+' '*(20-len(self.name)),
        print '\t','|','\t',self.dob+' '*(10-len(self.dob)),
        print '\t','|','\t',self.panno+' '*(10-len(self.panno)),
        print '\t','|','\t',self.telno+' '*(10-len(self.telno)),
        print '\t','|','\t',self.email+' '*(20-len(self.email)),'\t','|'
    


def create():
    """Creates the client database."""
    f=open("client.dat","wb+")
    t=open("no.txt",'r')
    cn=int(t.read())
    t.close()
    s1=client()
    while True:
        cn=cn+1
        s1.input(cn)
        dump(s1,f)
        ch=raw_input("Stop adding new entries?   ")
        if ch.lower()=="yes" or ch.lower()=="y":
            print
            break
            
    f.close()
    t=open("no.txt","w")
    t.write(str(cn))
    t.close()


    
def add():
    """Adds entries to the client database."""
    f=open("client.dat","ab")
    t=open("no.txt",'r')
    cn=int(t.read())
    t.close()
    s1=client()
    while True:
        cn=cn+1
        s1.input(cn)
        dump(s1,f)
        ch=raw_input("Stop adding new entries?   ")
        if ch.lower()=="yes" or ch.lower()=="y":
            print
            break
    f.close()
    t=open("no.txt","w")
    t.write(str(cn))
    t.close()



def disp():
    """Displays entries in the client database."""
    if not os.path.isfile('client.dat'): print 'File not found.'
    else:
        f=open("client.dat","rb")
        s1=client()
        try:
            print '+'*(153)
            print '|','\t','CNo',
            print '\t','|','\t','Name'+' '*16,
            print '\t','|','\t','DOB'+' '*7,
            print '\t','|','\t','PAN'+' '*7,
            print '\t','|','\t','Tel'+' '*7,
            print '\t','|','\t','Email'+' '*15,'\t','|'
            while True:
                s1=load(f)
                s1.display()
        except EOFError: print '+'*(153)
        except : print "Some error occured."
        finally:
            f.close()
            print



def modify():
    """Modifies entries in the client database."""

    if not os.path.isfile('client.dat'):
        print 'File not found.'

    else:
        f=open('client.dat','rb+')
        s1=client()
        print "Modify by:\n1. Client No.\n2. Name\n3. PAN\n" 
        modby = int(raw_input("Enter choice   "))

        if modby == 1:
            cn=input("Enter Client number   ")
            flag=0
            try:
                while True:
                    pos=f.tell()
                    s1=load(f)
                    if s1.cno==cn:
                        k = s1
                        flag=1
                        s1.name=raw_input('Enter name   ')
                        s1.dob = raw_input("Enter DOB in dd-mm-yyyy format   ")
                        s1.panno = raw_input("Enter PAN number   ")
                        s1.telno = raw_input("Enter contact number   ")
                        s1.email = raw_input("Enter Email ID   ")
                        f.seek(pos)
                        dump(s1, f)
                        break
            except EOFError:
                if flag==0:
                    print 'Record not found.'
            finally:
                print
                f.close()
                
        elif modby == 2:
            nm=raw_input('Enter name   ')
            flag=0
            try:
                while True:
                    pos=f.tell()
                    s1=load(f)
                    if s1.name.lower()==nm.lower():
                        k = s1
                        flag=1
                        s1.name=raw_input('Enter name   ')
                        s1.dob = raw_input("Enter DOB in dd-mm-yyyy format   ")
                        s1.panno = raw_input("Enter PAN number   ")
                        s1.telno = raw_input("Enter contact number   ")
                        s1.email = raw_input("Enter Email ID   ")
                        f.seek(pos)
                        dump(s1, f)
                        break
            except EOFError:
                if flag==0:
                    print 'Record not found.'
            finally:
                print
                f.close()

        elif modby == 3:
            panno = raw_input("Enter PAN number   ")
            flag=0
            try:
                while True:
                    pos=f.tell()
                    s1=load(f)
                    if s1.panno.lower()==panno.lower():
                        k = s1
                        flag=1
                        s1.name=raw_input('Enter name   ')
                        s1.dob = raw_input("Enter DOB in dd-mm-yyyy format   ")
                        s1.panno = raw_input("Enter PAN number   ")
                        s1.telno = raw_input("Enter contact number   ")
                        s1.email = raw_input("Enter Email ID   ")
                        f.seek(pos)
                        dump(s1, f)
                        break
            except EOFError:
                if flag==0:
                    print 'Record not found.'
            finally:
                print
                f.close()



def search():
    """Searches entries in the database."""

    if not os.path.isfile('client.dat'):
        print 'File not found.'

    else:
        f=open("client.dat","rb")
        s1=client()
        l = []
        flag=0
        print "Search by:\n1. Client No.\n2. Name\n3. PAN\n" 
        searchby = int(raw_input("Enter choice   "))

        if searchby == 1:
            an=input('Enter Client number   ')
            try:
                while True:
                    s1=load(f)
                    if s1.cno==an:
                        l.append(s1)
                        flag=1
            except EOFError:
                if flag==0:
                    print 'Record not found.'
                else:
                    print '+'*(153)
                    print '|','\t','CNo',
                    print '\t','|','\t','Name'+' '*16,
                    print '\t','|','\t','DOB'+' '*7,
                    print '\t','|','\t','PAN'+' '*7,
                    print '\t','|','\t','Tel'+' '*7,
                    print '\t','|','\t','Email'+' '*15,'\t','|'
                    for i in l:
                        i.display()
                    print '+'*(153)
                
            except: print 'Some error occured.'
            finally:
                f.close()
                print

        elif searchby == 2:
            an=raw_input('Enter Client name   ').lower()
            try:
                while True:
                    s1=load(f)
                    if s1.name.lower()==an:
                        l.append(s1)
                        flag=1
            except EOFError:
                if flag==0:
                    print 'Record not found.'
                else:
                    print '+'*(153)
                    print '|','\t','CNo',
                    print '\t','|','\t','Name'+' '*16,
                    print '\t','|','\t','DOB'+' '*7,
                    print '\t','|','\t','PAN'+' '*7,
                    print '\t','|','\t','Tel'+' '*7,
                    print '\t','|','\t','Email'+' '*15,'\t','|'
                    for i in l:
                        i.display()
                    print '+'*(153)
                
            except: print 'Some error occured.'
            finally:
                f.close()
                print

        elif searchby == 3:
            an=raw_input('Enter PAN   ').lower()
            try:
                while True:
                    s1=load(f)
                    if s1.panno.lower()==an:
                        l.append(s1)
                        flag=1
            except EOFError:
                if flag==0:
                    print 'Record not found.'
                else:
                    print '+'*(153)
                    print '|','\t','CNo',
                    print '\t','|','\t','Name'+' '*16,
                    print '\t','|','\t','DOB'+' '*7,
                    print '\t','|','\t','PAN'+' '*7,
                    print '\t','|','\t','Tel'+' '*7,
                    print '\t','|','\t','Email'+' '*15,'\t','|'
                    for i in l:
                        i.display()
                    print '+'*(153)
                
            except: print 'Some error occured.'
            finally:
                f.close()
                print


        
def delete():
    """Deletes entries from the client database."""
    if not os.path.isfile('client.dat'):
        print 'File not found.'
    else:
        f1=open("client.dat","rb")
        t=open("temp.dat","wb")
        s1=client()
        flag=1
        ad=input('Enter Client number   ')
        try:
            while True:
                s1=load(f1)
                if s1.cno==ad:
                    flag=0
                else: dump(s1,t)
        except EOFError:
            if flag==1:
                print 'Record not found.'
            else: print 'Record has been deleted.'
        except: print 'Some error ocurred.'
        finally:
            f1.close()
            t.close()
            os.remove('client.dat')
            os.rename('temp.dat','client.dat')
            print


           
while True:
    """Loops through the options."""    
    print "\t1. Create log\t2. Add log entry\t3. Display log\t",
    print "4. Search log entry\t5. Delete log entry\t",
    print "6. Modify log entry\t7. Exit program"
    print 
    c=raw_input('Enter choice   ')
    if c=='1':
        print
        create()
    elif c=='2':
        print
        add()
    elif c=='3':
        print
        disp()
    elif c=='4':
        print
        search()
    elif c=='5':
        print
        delete()
    elif c=='6':
        print
        modify()
    elif c=='7':
        break



##    Code of validDate module:
##
##    def validdate(d,m,y):
##        c=0
##        if m in [1,3,5,7,8,10,12]:
##            if d>=1 and d<=31:
##                    c+=1
##            elif m==2:
##                    if ((y%4==0 and y%100<>0) or y%400==0):
##                        if d>=1 and d<=29:
##                            c+=1
##                        else:
##                            if d>=1 and d<=28:
##                                c+=1
##        else:
##            if d>=1 and d<=30:
##                c+=1
##
##        if c!=0:
##            return True
##        else:
##            return False

