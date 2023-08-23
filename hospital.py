import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hosipital Management System")
        self.root.geometry("1540x800")

        self.nameOfTablets = StringVar()
        self.ref = StringVar()
        self.dose = StringVar()
        self.numberOfTablets = StringVar()
        self.lot = StringVar()
        self.issueDate = StringVar()
        self.expDate = StringVar()
        self.dailyDose = StringVar()
        self.sideEffect = StringVar()
        self.furtherInfo = StringVar()
        self.bloodPressure = StringVar()
        self.storageAdvice = StringVar()
        self.medication = StringVar()
        self.patientID = StringVar()
        self.nhsNumber = StringVar()
        self.patientName = StringVar()
        self.dob = StringVar()
        self.patientAddress = StringVar()
        self.prescription = StringVar()

        #****************************************************************************************************
        lb_title = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", 
                         foreground="red", background="white", font=("times new roman", 50, "bold"))
        lb_title.pack(side=TOP, fill=X)

        # *************************DataFrame*************************
        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft= LabelFrame(DataFrame, bd=10, padx=20, relief=RIDGE,
                             font=("arial", 15, "bold"), text="Patient Infomation")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(DataFrame, bd=10, padx= 20, relief=RIDGE,
                               font=("arial", 15, "bold"), text="Prescription")
        DataFrameRight.place(x=990,y=5, width=500, height=350)

        # *************************Button frame*************************
        ButtonFrame = Frame(self.root, bd=20,  relief=RIDGE)
        ButtonFrame.place(x=0, y=530, width=1530, height=70)

        # *************************Details frame*************************
        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailsFrame.place(x=0, y=600, width=1530, height=190)

        # *************************DataFrameLeft*************************
        lbl_Name_Tablet = Label(DataFrameLeft, text="Names of tablet", 
                               font=("times new roman", 13, "bold"), padx=2, pady=6)
        lbl_Name_Tablet.grid(row=0, column=0)

        com_Name_tablet = ttk.Combobox(DataFrameLeft,textvariable= self.nameOfTablets, font=("times new roman", 12, "bold"), width=33)
        com_Name_tablet["value"] =("Nice", "Corona Vacacine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        com_Name_tablet.grid(row=0, column=1)

        lbl_ref = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No: ", padx=2)
        lbl_ref.grid(row=1, column=0, sticky=W)
        txt_ref = Entry(DataFrameLeft, textvariable=self.ref,font=("arial", 13, "bold"), width=35)
        txt_ref.grid(row=1, column=1)

        lbl_Dose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dose: ", padx=2, pady=4)
        lbl_Dose.grid(row=2, column=0, sticky=W)
        txt_Dose = Entry(DataFrameLeft, textvariable=self.dose, font=("arial", 13, "bold"), width=35)
        txt_Dose.grid(row=2, column=1)

        lbl_No_of_tablet = Label(DataFrameLeft, font=("arial", 12, "bold"), text="No of Tablets: "
                                 , padx=2, pady=6)
        lbl_No_of_tablet.grid(row=3, column=0, sticky=W)
        txt_No_of_tablet = Entry(DataFrameLeft,textvariable=self.numberOfTablets, font=("arial", 13, "bold"), width=35)
        txt_No_of_tablet.grid(row=3, column=1)

        lbl_Lot = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot: ", padx=2, pady=6)
        lbl_Lot.grid(row=4, column=0, sticky=W)
        txt_Lot = Entry(DataFrameLeft, textvariable=self.lot, font=("arial", 13, "bold"), width=35)
        txt_Lot.grid(row=4, column=1)

        lbl_issue_date = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date: "
                               , padx=2, pady=6)
        lbl_issue_date.grid(row=5, column=0, sticky=W)
        txt_issue_date = Entry(DataFrameLeft, textvariable=self.issueDate, font=("arial", 13, "bold"), width=35)
        txt_issue_date.grid(row=5, column=1)

        lbl_exp_date = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date: ", padx=2, pady=6)
        lbl_exp_date.grid(row=6, column=0, sticky=W)
        txt_exp_date = Entry(DataFrameLeft, textvariable=self.expDate, font=("arial", 13, "bold"), width=35)
        txt_exp_date.grid(row=6, column=1)

        lbl_daily_dose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Daily Dose: ", padx=2, pady=4)
        lbl_daily_dose.grid(row=7, column=0, sticky=W)
        txt_daily_dose = Entry(DataFrameLeft,textvariable=self.dailyDose, font=("arial", 13, "bold"), width=35)
        txt_daily_dose.grid(row=7, column=1)

        lbl_side_effect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect: ", padx=2, pady=4)
        lbl_side_effect.grid(row=8, column=0, sticky=W)
        txt_side_effect = Entry(DataFrameLeft,textvariable=self.sideEffect, font=("arial", 13, "bold"), width=35)
        txt_side_effect.grid(row=8, column=1)

        lbl_further_info= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Further Information:", padx=2,pady=4)
        lbl_further_info.grid(row=0, column=2, sticky=W)
        txt_further_info = Entry(DataFrameLeft,textvariable=self.furtherInfo, font=('arial', 13, "bold"), width=35)
        txt_further_info.grid(row=0, column=3)

        lbl_blood_pressure= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2,pady=4)
        lbl_blood_pressure.grid(row=1, column=2, sticky=W)
        txt_blood_pressure = Entry(DataFrameLeft, textvariable=self.bloodPressure, font=('arial', 13, "bold"), width=35)
        txt_blood_pressure.grid(row=1, column=3)

        lbl_storage_advices= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2,pady=4)
        lbl_storage_advices.grid(row=2, column=2, sticky=W)
        txt_storage_advices = Entry(DataFrameLeft,textvariable=self.storageAdvice, font=('arial', 13, "bold"), width=35)
        txt_storage_advices.grid(row=2, column=3)

        lbl_medication= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medication:", padx=2,pady=4)
        lbl_medication.grid(row=3, column=2, sticky=W)
        txt_medication = Entry(DataFrameLeft,textvariable=self.medication, font=('arial', 13, "bold"), width=35)
        txt_medication.grid(row=3, column=3)

        lbl_patient_id= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient ID:", padx=2,pady=4)
        lbl_patient_id.grid(row=4, column=2, sticky=W)
        txt_patient_id = Entry(DataFrameLeft,textvariable=self.patientID, font=('arial', 13, "bold"), width=35)
        txt_patient_id.grid(row=4, column=3)

        lbl_lhs_number= Label(DataFrameLeft, font=("arial", 12, "bold"), text="LHS Number:", padx=2,pady=4)
        lbl_lhs_number.grid(row=5, column=2, sticky=W)
        txt_lhs_number = Entry(DataFrameLeft, textvariable=self.nhsNumber, font=('arial', 13, "bold"), width=35)
        txt_lhs_number.grid(row=5, column=3)

        lbl_patient_name= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2,pady=4)
        lbl_patient_name.grid(row=6, column=2, sticky=W)
        txt_patient_name = Entry(DataFrameLeft,textvariable=self.patientName, font=('arial', 13, "bold"), width=35)
        txt_patient_name.grid(row=6, column=3)

        lbl_dob= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date of Birth:", padx=2,pady=4)
        lbl_dob.grid(row=7, column=2, sticky=W)
        txt_dob = Entry(DataFrameLeft,textvariable=self.dob, font=('arial', 13, "bold"), width=35)
        txt_dob.grid(row=7, column=3)

        lbl_address= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2,pady=4)
        lbl_address.grid(row=8, column=2, sticky=W)
        txt_address = Entry(DataFrameLeft, textvariable=self.patientAddress, font=('arial', 13, "bold"), width=35)
        txt_address.grid(row=8, column=3)

        # *************************Data Frame Right*************************
        self.txtPrescription = Text(DataFrameRight, font=("arial", 12, "bold"), width=61, height=20, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # *************************Buttons*************************
        bt_Prescription = Button(ButtonFrame, text="Prescription", bg="green",
                                 fg="red",font=("arial", 12, "bold"), width=30, padx=2, pady=4, command=self.iPrescription)
        bt_Prescription.grid(row=0, column=0)

        bt_Prescription_data = Button(ButtonFrame, text="Prescription Data", bg="green",
                                 fg="red", font=("arial", 12, "bold"), width=30, padx=2, pady=4, command=self.iPresciptionData)
        bt_Prescription_data.grid(row=0, column=1)

        bt_update = Button(ButtonFrame, text="Update", bg="green",
                                 fg="red", font=("arial", 12, "bold"), width=30, padx=2, pady=4, command=self.iUpdate)
        bt_update.grid(row=0, column=2)

        bt_delete = Button(ButtonFrame, text="Delete", bg="green",
                                 fg="red", font=("arial", 12, "bold"), width=30, padx=2, pady=4, command=self.iDelete)
        bt_delete.grid(row=0, column=3)

        bt_reset = Button(ButtonFrame, text="Reset", bg="green",
                                 fg="red", font=("arial", 12, "bold"), width=30, padx=2, pady=4, command=self.iReset)
        bt_reset.grid(row=0, column=4)

        bt_exit = Button(ButtonFrame, text="Exit", bg="green",
                                 fg="red", font=("arial", 12, "bold"), width=30, padx=2, pady=4, command=self.iExit)
        bt_exit.grid(row=0, column=5)

        # *************************Table*****************************
        # *************************Scrollbar*************************
        scroll_x = ttk.Scrollbar(DetailsFrame, orient= HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient= VERTICAL)
        self.hospital_table = ttk.Treeview(DetailsFrame, columns=("nameOfTable", "referenceNo", "dose", "noOfTablets", "lot",
                                                                  "issueDate", "expDate", "dailyDate", "storage", "NHS_Number",
                                                                  "patientName", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM,fill =X)
        scroll_y.pack(side=RIGHT, fill= Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameOfTable", text="Name of Table")
        self.hospital_table.heading("referenceNo", text="Reference No")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("noOfTablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issueDate", text="Issue Date")
        self.hospital_table.heading("expDate", text="Exp Date")
        self.hospital_table.heading("dailyDate", text="Daily date")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("NHS_Number", text="NHS Number")
        self.hospital_table.heading("patientName", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table.column("nameOfTable", width=100)
        self.hospital_table.column("referenceNo", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("noOfTablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issueDate", width=100)
        self.hospital_table.column("expDate", width=100)
        self.hospital_table.column("dailyDate", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("NHS_Number", width=100)
        self.hospital_table.column("patientName", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)


        self.hospital_table["show"] = "headings"

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fatch_data()


    # *************************Functionality Declaration*************************
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Hospital Management Systerm", "confirm if you want to exit")
        if iExit > 0:
            root.destroy()
            return

    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of tablets:\t\t\t" + self.nameOfTablets.get()+ "\n")
        self.txtPrescription.insert(END, "Reference No:\t\t\t" + self.ref.get()+ "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.dose.get()+ "\n")
        self.txtPrescription.insert(END, "Number of tablets:\t\t\t" + self.numberOfTablets.get()+ "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.lot.get()+ "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.issueDate.get()+ "\n")
        self.txtPrescription.insert(END, "Exp Date:\t\t\t" + self.expDate.get()+ "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + self.dailyDose.get()+ "\n")
        self.txtPrescription.insert(END, "Slide Effect:\t\t\t" + self.sideEffect.get()+ "\n")
        self.txtPrescription.insert(END, "Further Information:\t\t\t" + self.furtherInfo.get()+ "\n")
        self.txtPrescription.insert(END, "Patien ID:\t\t\t" + self.patientID.get()+ "\n")
        self.txtPrescription.insert(END, "NHS Number:\t\t\t" + self.nhsNumber.get()+ "\n")
        self.txtPrescription.insert(END, "Patient Name:\t\t\t" + self.patientName.get()+ "\n")
        self.txtPrescription.insert(END, "Date of Birth:\t\t\t" + self.dob.get()+ "\n")
        self.txtPrescription.insert(END, "Patient Address:\t\t\t" + self.patientAddress.get()+ "\n")

    def iPresciptionData(self):
        if self.nameOfTablets.get()=="" or self.ref.get() =="":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="19112002", database="sys")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                            self.nameOfTablets.get(),
                                                                                            self.ref.get(),
                                                                                            self.dose.get(),
                                                                                            self.numberOfTablets.get(),
                                                                                            self.lot.get(),
                                                                                            self.issueDate.get(),
                                                                                            self.expDate.get(),
                                                                                            self.dailyDose.get(),
                                                                                            self.storageAdvice.get(),
                                                                                            self.nhsNumber.get(),
                                                                                            self.patientName.get(),
                                                                                            self.dob.get(),
                                                                                            self.patientAddress.get()                                                
                                                                                                    ))

            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")
    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="19112002", database="sys")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall() #lay tat ca cac dong luu vao rows
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children()) #xoa tat ca cac dong hien co trong bang
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row=content["values"] #lay cac gia tri trong content gan vao row
        self.nameOfTablets.set(row[0])
        self.ref.set(row[1])
        self.dose.set(row[2])
        self.numberOfTablets.set(row[3])
        self.lot.set(row[4])
        self.issueDate.set(row[5])
        self.expDate.set(row[6])
        self.dailyDose.set(row[7])
        self.storageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.patientName.set(row[10])
        self.dob.set(row[11])
        self.patientAddress.set(row[12])

    def iUpdate(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="19112002", database="sys")
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital set nameOftablets=%s, reference_No=%s, dose=%s, numberOfTablets=%s, lot=%s, issueDate=%s, expDate=%s, dailyDose=%s, storage=%s, nhsNumber=%s, patientName=%s, dob=%s, patientAddress=%s",(
                                                                                            self.nameOfTablets.get(),
                                                                                            self.ref.get(),
                                                                                            self.dose.get(),
                                                                                            self.numberOfTablets.get(),
                                                                                            self.lot.get(),
                                                                                            self.issueDate.get(),
                                                                                            self.expDate.get(),
                                                                                            self.dailyDose.get(),
                                                                                            self.storageAdvice.get(),
                                                                                            self.nhsNumber.get(),
                                                                                            self.patientName.get(),
                                                                                            self.dob.get(),
                                                                                            self.patientAddress.get()  
                                                                                                                        ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success", "Record has been updated")
    def iDelete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="19112002", database="sys")
        my_cursor = conn.cursor()
        query = "delete from hospital where reference_No=%s"
        value=(self.ref.get(), )
        my_cursor.execute(query, value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete", "Patient has been delete successfully")
    def iReset(self):
        self.nameOfTablets.set("")
        self.ref.set("")
        self.dose.set("")
        self.numberOfTablets.set("")
        self.lot.set("")
        self.issueDate.set("")
        self.expDate.set("")
        self.dailyDose.set("")
        self.sideEffect.set("")
        self.furtherInfo.set("")
        self.bloodPressure.set("")
        self.storageAdvice.set("")
        self.medication.set("")
        self.patientID.set("")
        self.nhsNumber.set("")
        self.patientName.set("")
        self.dob.set("")
        self.patientAddress.set("")
        self.txtPrescription.delete("1.0", END)
        return



root = Tk()
ob = Hospital(root)
root.mainloop()