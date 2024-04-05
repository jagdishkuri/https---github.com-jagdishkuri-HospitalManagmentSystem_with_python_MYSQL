from tkinter import *
import random
import time
import datetime
from tkinter import messagebox
from tkinter import Tk
from tkinter import ttk
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        #variable to take data
        self.nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.Expdate = StringVar()
        self.DailtDose = StringVar()
        self.sideEfect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.Patientname = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()



        lbltitle = Label(
            self.root,
            bd=20,
            relief=RIDGE,
            text="HOSPITAL MANAGMENT SYSTEM",
            fg="blue",
            bg="white",
            font=("times new roman", 50, "bold"),
        )
        lbltitle.pack(side=TOP, fill=X)

  #data frame
        Dataframe = Frame(self.root,bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(Dataframe, bd =10, relief=RIDGE, padx=10,
                                   font=("times and roman", 12, "bold"), text="Patient information")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(Dataframe, bd =10, relief=RIDGE, padx=10,
                                   font=("times and roman", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=990, y=5, width=460, height=350)
  #button frame
        Buttonframe = Frame(self.root,bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)
  #details frame
        Detailsframe = Frame(self.root,bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

#DataframeLeft
        lblNameTablet = Label(DataFrameLeft, text="Name of Tablet",font=("times and roman", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0,sticky=W)
        comNametablet = ttk.Combobox(DataFrameLeft,textvariable=self.nameoftablets,state="readonly",font=("times and roman", 12, "bold"),width=33)
        comNametablet["values"]=("Nice", "Corona vacacine", "Ativan","Amlodipine")
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)
        


        lblref=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W) 
        txtref = Entry (DataFrameLeft,textvariable=self.ref, font=("arial", 13, "bold"), width=35) 
        txtref.grid(row=1,column=1)

        lblDose = Label (DataFrameLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4) 
        lblDose.grid(row=2,column=0, sticky=W)
        txtDose = Entry (DataFrameLeft,textvariable=self.Dose, font=("arial", 13, "bold"), width=35) 
        txtDose.grid(row=2,column=1)

        lblNoOftablets = Label(DataFrameLeft, font=("arial", 12, "bold"), text="No Of Tablets::", padx=2, pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W) 
        txtNoOftablets = Entry (DataFrameLeft,textvariable=self.NumberofTablets, font=("arial", 13, "bold"), width=35) 
        txtNoOftablets.grid(row=3,column=1)

        lblLot =  Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot =  Entry(DataFrameLeft, textvariable=self.Lot,font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4,column=1)

        IblissueDate= Label (DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=5) 
        IblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate =  Entry(DataFrameLeft,textvariable=self.Issuedate ,font=("arial", 13, "bold"), width=35) 
        txtissueDate.grid(row = 5,column=1)

        lblExpDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6) 
        lblExpDate.grid(row=6,column =0, sticky=W)
        txtExpDate =  Entry(DataFrameLeft,textvariable=self.Expdate ,font=("arial", 13, "bold"), width=35) 
        txtExpDate.grid(row=6,column=1)

        lblDailyDose = Label (DataFrameLeft, font = ("arial", 12, "bold"), text ="Daily Dose:",padx=2, pady =4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry (DataFrameLeft,textvariable=self.DailtDose ,font=("arial", 13, "bold"), width=35) 
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect =Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:",padx=2,pady=6) 
        lblSideEffect.grid(row = 8,column = 0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft,textvariable=self.sideEfect ,font=("arial", 13, "bold"), width=35)
        txtSideEffect.grid(row = 8,column = 1)

        lblFurtherinfor = Label (DataFrameLeft, font =("arial", 12, "bold"), text =" Further Information", padx=2)
        lblFurtherinfor.grid(row = 0,column =2, sticky =W)
        txtfurtherinfo = Entry(DataFrameLeft,textvariable=self.FurtherInformation ,font =("arial", 12, "bold"), width=35)
        txtfurtherinfo.grid(row =0,column =3)

        lblBloodPressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Blood Pressure", padx=2, pady=6)
        lblBloodPressure.grid(row=1,column=2, sticky=W)
        txtBloodPressure =  Entry(DataFrameLeft,textvariable=self.DrivingUsingMachine, font=("arial", 12, "bold"), width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage = Label (DataFrameLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2,column=2, sticky =W) 
        txtStorage =Entry (DataFrameLeft,textvariable=self.StorageAdvice ,font=("arial", 12, "bold"), width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine  = Label (DataFrameLeft, font=("arial", 12, "bold"), text="Medication", padx=2, pady=6)
        lblMedicine.grid(row=3,column=2, sticky=W)
        txtMedicine  = Entry (DataFrameLeft, textvariable=self.HowToUseMedication,font=("arial", 12, "bold"), width=35)
        txtMedicine.grid(row=3,column=3, sticky =W)

        lblPatientId=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Patient Id", padx=2, pady=6)
        lblPatientId.grid(row=4,column=2, sticky =W) 
        txtPatientId=Entry (DataFrameLeft,textvariable=self.PatientId ,font=("arial", 12, "bold"), width=35) 
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber = Label (DataFrameLeft, font=("arial", 12, "bold"), text="NHS Number", padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2, sticky=W)
        txtNhsNumber =  Entry (DataFrameLeft, textvariable=self.nhsNumber,font=("arial", 12, "bold"), width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname =Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name", padx=2, pady=6)
        lblPatientname.grid(row =6,column=2, sticky =W)
        txtPatientname  = Entry(DataFrameLeft,textvariable=self.Patientname,font=("arial", 12, "bold"), width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth  = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Of Birth", padx=2, pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth = Entry (DataFrameLeft,textvariable=self.DateOfBirth ,font=("arial", 12, "bold"), width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address", padx=2,pady =6)
        lblPatientAddress.grid(row=8,column=2, sticky =W)
        txtPatientAddress = Entry(DataFrameLeft, textvariable=self.PatientAddress,font=("arial", 12, "bold"), width=35) 
        txtPatientAddress.grid(row=8,column=3)

       #presecription
        self.txtPresecription = Text(DataFrameRight, font=("arial",12,"bold"),width=46,height=16,padx=2, pady=6)
        self.txtPresecription.grid(row=0, column=0)


        #button
        btnpresecription = Button(Buttonframe, text="Prescription",bg ="green",fg="white", font=("arial",12,"bold"),width=23,padx=2, pady=6)
        btnpresecription.grid(row=0,column=0)

        btnpresecriptionData = Button(Buttonframe, text="Prescription Data",bg ="green",fg="white", font=("arial",12,"bold"),width=23,padx=2, pady=6,command=self.iPrescriptionData)
        btnpresecriptionData.grid(row=0,column=1)

        btnUpdate = Button(Buttonframe, text="Update",bg ="green",fg="white", font=("arial",12,"bold"),width=23,padx=2, pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete = Button(Buttonframe, text="Delete",bg ="green",fg="white", font=("arial",12,"bold"),width=23,padx=2, pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear = Button(Buttonframe, text="Clear",bg ="green",fg="white", font=("arial",12,"bold"),width=23,padx=2, pady=6)
        btnClear.grid(row=0,column=4)

        btnExit = Button(Buttonframe, text="Exit",bg ="green",fg="white", font=("arial",12,"bold"),width=23,padx=2, pady=6)
        btnExit.grid(row=0,column=5)


        #Table-------------------------
        #scrollbar x and y in table
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe, column = ("nameoftables","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","nhsnumber","storage",'pname',"dob","address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftables", text = "Name Of Tablets")
        self.hospital_table.heading("ref", text = "Refrence No.")
        self.hospital_table.heading("dose", text = "Dose")
        self.hospital_table.heading("nooftablets", text = "NO Of Tablets")
        self.hospital_table.heading("lot", text = "LOT")
        self.hospital_table.heading("issuedate", text = "Issue Date")
        self.hospital_table.heading("expdate", text = "Exp Date")
        self.hospital_table.heading("dailydose", text = "Daily Dose")
        self.hospital_table.heading("storage", text = "Storage")
        self.hospital_table.heading("nhsnumber", text = "NHS Number")
        self.hospital_table.heading("pname", text = "Patient name")
        self.hospital_table.heading("dob", text = "DOB")
        self.hospital_table.heading("address", text = "Address")

        self.hospital_table["show"] = "headings"
        self.hospital_table.column("nameoftables", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.fatch_data()

#functionality Declaration
    def iPrescriptionData(self):
        if self.nameoftablets.get()=="" or self.ref.get()=="":
          messagebox.showerror("error", "all fields are required")
        else:
            conn= mysql.connector.connect(host = "localhost", user = "root", password = "********" , database = "student")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                 self.nameoftablets.get(),
                                                                                                 self.ref.get(),
                                                                                                 self.Dose.get(),
                                                                                                 self.NumberofTablets.get(),
                                                                                                 self.Lot.get(),
                                                                                                 self.Issuedate.get(),
                                                                                                 self.Expdate.get(),
                                                                                                 self.DailtDose.get(),
                                                                                                 self.StorageAdvice.get(),
                                                                                                 self.nhsNumber.get(),
                                                                                                 self.Patientname.get(),
                                                                                                 self.DateOfBirth.get(),
                                                                                                 self.PatientAddress.get(),
                                                                                                 self.sideEfect.get(),
                                                                                                 self.FurtherInformation(),
                                                                                                 self.DrivingUsingMachine.get(),


                                                                                                 self.PatientId.get(),
                                                                                                 self.HowToUseMedication.get()

                                                                                                 ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("success"," Record has been inserted")
    def fatch_data(self):
         conn= mysql.connector.connect(host = "localhost", user = "root", password = "**********" , database = "student")
         my_cursor = conn.cursor()
         my_cursor.execute("select * from hospital")
         rows= my_cursor.fetchall()
         if len(rows)!=0:
             self.hospital_table.delete(*self.hospital_table.get_children())
             for i in rows:
                 self.hospital_table.insert("", END, values=i)
             conn.commit()
         conn.close()
            
         




        

root = Tk()
ob = Hospital(root)
root.mainloop()
