from model import *
class app:
    choise=0
    catlist=[]
    expenlist=[]
    
    def startapp(self):
        while True:
            self.printoption()
            if app.choise==1:
                self.addcategory()
            elif app.choise==2:
                self.catlisting()
            elif app.choise==3:
                self.addexpense()
            elif app.choise==4:
                self.expenlisting()
            elif app.choise==5:
                self.reportmonthly()
            elif app.choise==6:
                self.reportcat()
            elif app.choise==7:
                self.reportmonthrange()
            elif app.choise==8:
                break

    def printoption(self):
        print("1. add category")
        print("2. category listing")
        print("3. expense enrty")
        print("4. expense listing")
        print("5. report(monthly)")
        print("6. report (cattegory-wise)")
        print("7. report (month range)")
        print("8. exit")
        


        app.choise= int(input("enter your choise: "))


    def addcategory(self):
        id =int(input("enter category id: "))
        nm =input(" enter category name: ")

        c= category()
        c.setcategoryid(id)
        c.setcatname(nm)
        app.catlist.append(c)
        print("category added successfully!")
        

    def addexpense(self):
        self.catlisting()
        n=int(input("enter the category num-"))
        am=int(input("enter the amount"))
        date=input("enter the date")
        remark=input("enter the remark")
        i=app.catlist[n-1].getcategoryid()

        c=expense()
        c.setammount(am)
        c.setdate(date)
        c.setremark(remark)
        c.setcatid(i)
        app.expenlist.append(c)

    def catlisting(self):
        j=1
        for i in app.catlist:
            #print(i.getcategoryid())
            print(j,i.getcatname())
            j+=1
            
        
        
    def expenlisting(self):

        for j in app.catlist:
            print(self.getingname(j))
        for i in app.expenlist:
            print(i.getammount())
            print(i.getdate())
            print(i.getremark())

           # print(i.getcatid())

    def getingname(self,ide):
        for i in app.expenlist:

            if ide.getcategoryid() == i.getcatid():
                return ide.getcatname()

    def reportmonthly(self):
        month= int(input("enter month (01-12)"))
        for i in app.expenlist:
            date= i.getdate()
            datelist=date.split("/")
            if int(datelist[1])==month:
                print(i.getammount(), i.getremark())

    def reportmonthrange(self):
        month=input("enter month range")
        month=month.split('-')
        for j in range(int(month[0]),int(month[1])+1):
            for i in app.expenlist:
                
                date=i.getdate()
                date=date.split('/')
                if int(date[1])==j:
                    print(i.getammount(),i.getremark())
            

    def reportcat(self):
        #for j in app.expenlist:
            #print(j.getcatname())
        self.catlisting()
        c=input("enter category name")
        for i in app.catlist:
            if c==i.getcatname():
                print(c)
                self.xyz(i)

    def xyz(self,i):
        
        for j in app.expenlist:
            
            if i.getcategoryid()==j.getcatid():
                
                print(j.getammount(),j.getdate(),j.getremark())


    

service=app()
service.startapp()

                    












