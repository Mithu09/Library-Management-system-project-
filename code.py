from  tkinter import *

class Multiple():
       def __init__ (self,root):
            self.root=root
            self.root.geometry("400x400")
            self.root.title ("Library mangement system")
            self.root.config(bg="powderblue")
             
            title=Label(self.root,text="Home page",bg="powderblue",font=('bold','25'))   
            title.pack()

            admin_button=Button(self.root,text="Admin",command=self.admin_page)
            admin_button.place(x=150,y=120)

            user_button=Button(self.root,text="user")
            user_button.place(x=150,y=180)

       def   admin_page(self):
             window  = Tk()
             window.title("Admin page")
             window.geometry("300x300")
             window.config(bg="powderblue")

             book_name_label = Label(window,text="Book Name",bg="powderblue",font=('bold','15'))
             book_name_label.place(x=20,y=40)

             author_label = Label(window,text="Author",bg="powderblue",font=('bold','15'))
             author_label.place(x=20,y=80)

             qty_label = Label(window,text="Quantity",bg="powderblue",font=('bold','15'))
             qty_label.place(x=20,y=160)

             book_entry=Entry(window)
             book_entry.place(x=150,y=40)

             author_entry=Entry(window)
             author_entry.place(x=150,y=100)

             qty_entry=Entry(window)
             qty_entry.place(x=150,y=40)
             
             admin_submit=Button(window,text="submit")
             admin_submit.place(x=120,y=200)

       def user_page(self):
             window1 = Tk()
             window1.title("Admin page")
             window1.geometry("300X300")
             window1.config(bg="powederblue")
           
             book_label = Label(window1,text="Book Name",bg="powderblue",font=('bold','15'))
             book_label.place(x=20,y=40)

             author_label = Label(window1,text="Author",bg="powderblue",font=('bold','15'))
             author_label.place(x=20,y=80)

             self.user_book_entry=Entry(window1)
             self.user_book_entry.place(x=100,y=40)

             self.author_book_entry=Entry(window1)
             self.author_book_entry.place(x=150,y=150)

             user_submit=Button(window1,text="submit",command=self.uder_data)
             user_submit.place(x=130,y=200)
       def admin_add(self):
            import mysql.connector

            mydb=mysql.connector.connect(host='localhost',port=3306,user='root',password='root',database='Library') 

            mycursor=mydb.cursor()

            bookname =self.bookname_entry.get()
            author=self.author_entry.get()
            qty=self.quantity_entry.get()

            
            mycursor.execute("insert into admin values(%s,%s,%s)",(book,author,qty))
            mydb.commit()
            msg.showinfo("Admin Books","Book added to stock")
      
       def user_data():
            import mysql.connector

            mydb=mysql.connector.connect(host='localhost',port=3306,user='root',password='root',database='Library mangement') 

            mycursor=mydb.cursor()
             
            book_name=self.user_book.get()
            author=self.user_book.get()
 
            mycursor.execute("select quantity from admin where Book_name=%s and author=%s",(book_name,author))
          
            q=0
            for i in mycursor:
               q=int(i[0])
            if a>=1:
               q=q-1
               mycursor.execute("update admin set quantity=%s where Book_name=%s and author=%s",(book_name,author))
               mycursor.execute("insert into user value(%s,%s)",(book_name,author))
               mydb.cpommit()
               msg.showinfo("Book Availabilty","Book available")
            else:
               msg.showerror("Book Availabilty","Book not found")
           
root = Tk()
obj = Multiple(root)
root.mainloop()
