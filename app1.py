import tkinter
from tkinter import messagebox
from time import gmtime, strftime
from PIL import ImageTk, Image
import csv


def update_index(account_number, data_file):
    with open(str(account_number) + "-index.txt", "w", newline="") as index_file:
        writer = csv.writer(index_file)
        writer.writerow([account_number, data_file])


def get_data_file_address(account_number):
    with open(str(account_number) + "-index.txt", "r") as index_file:
        reader = csv.reader(index_file)
        for row in reader:
            if row[0] == account_number:
                return row[1]
    return None


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0


def db_amt_write(master, amount, account, name):
    file_name = str(account) + ".txt"
    file1_address = id(file_name)
    print(file1_address)

    if is_number(amount) == 0:
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    fdet = open(account + ".txt", 'r')
    pin = fdet.readline()
    camt = int(fdet.readline())
    fdet.close()
    if int(amount) > camt:
        messagebox.showinfo("Error!!", "You dont have that amount left in your account\nPlease try again.")
    else:
        amti = int(amount)
        cb = camt - amti
        fdet = open(account + ".txt", 'w')
        fdet.write(pin)
        fdet.write(str(cb) + "\n")
        fdet.write(account + "\n")
        fdet.write(name + "\n")
        fdet.close()
        frec = open(str(account) + "-rec.txt", 'a+')
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + "              " + str(
            amti) + "              " + str(cb) + "\n")
        frec.close()
        messagebox.showinfo("Operation Successfull!!", "Amount Debited Successfully!!")
        update_index(account, file1_address)
        master.destroy()
        return


def cr_amt_write(master, amount, account, name):
    file_name = str(account) + ".txt"
    file1_address = id(file_name)
    print(file1_address)
    if is_number(amount) == 0:
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    fdet = open(account + ".txt", 'r')
    pin = fdet.readline()
    print(pin)
    camt = int(fdet.readline())
    print(camt)
    fdet.close()
    amti = int(amount)
    cb = amti + camt
    fdet = open(account + ".txt", 'w')
    fdet.write(pin)
    fdet.write(str(cb) + "\n")
    fdet.write(account + "\n")
    fdet.write(name + "\n")
    fdet.close()
    frec = open(str(account) + "-rec.txt", 'a+')
    frec.write(
        str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + str(amti) + "                    " + str(cb) + "\n")
    frec.close()
    messagebox.showinfo("Operation Successfull!!", "Amount Credited Successfully!!")
    update_index(account, file1_address)
    master.destroy()
    return


def cr_amt(acct, name):
    cr_window = tkinter.Tk()
    cr_window.title("credit form")
    cr_window.geometry('340x440')
    cr_window.configure(bg='#333333')
    frame1 = tkinter.Frame(cr_window, bg='#333333')
    cr_amt_label = tkinter.Label(
        frame1, text="enter the amount to be credited", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    cr_amt_entry = tkinter.Entry(frame1, font=("Arial", 16))
    c = cr_amt_entry
    cr_button = tkinter.Button(
        frame1, text="Credit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: cr_amt_write(cr_window, c.get().strip(), acct, name))

    cr_amt_label.grid(row=1, column=0)
    cr_amt_entry.grid(row=2, column=0, pady=20)
    cr_button.grid(row=3, column=0, pady=30)
    frame1.pack()


def db_amt(acct, name):
    db_window = tkinter.Tk()
    db_window.title("Debit form")
    db_window.geometry('340x440')
    db_window.configure(bg='#333333')
    frame1 = tkinter.Frame(db_window, bg='#333333')
    db_amt_label = tkinter.Label(
        frame1, text="enter the amount to be debited", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    db_amt_entry = tkinter.Entry(frame1, font=("Arial", 16))
    d = db_amt_entry
    db_button = tkinter.Button(
        frame1, text="Debit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: db_amt_write(db_window, d.get().strip(), acct, name))

    db_amt_label.grid(row=1, column=0)
    db_amt_entry.grid(row=2, column=0, pady=20)
    db_button.grid(row=3, column=0, pady=30)
    frame1.pack()


"""def balance(acct):
    fdet = open(acct + ".txt", 'r')
    fdet.readline()
    bal = fdet.readline()
    fdet.close()
    messagebox.showinfo("Balance", bal)"""


def balance(acct):
    # Read the index file
    with open(str(acct) + "-index.txt", 'r') as findex:
        for line in findex:
            account_number, address = line.strip().split(',')
            if account_number == acct:
                # Found the account number in the index file
                # Read the balance from the corresponding data file
                with open(str(account_number) + ".txt", 'r') as fdata:
                    fdata.readline()  # Skip the first line (account number)
                    bal = fdata.readline().strip()  # Read the balance
                # Display the balance
                messagebox.showinfo("Balance", bal)
                return

    # If the account number is not found in the index file
    messagebox.showinfo("Error", "Account not found.")


"""
def history(acct):
    ds_window = tkinter.Tk()
    ds_window.geometry('340x440')
    ds_window.title("display menu")
    ds_window.configure(bg='#333333')
    tkinter.Frame(ds_window, bg='#333333')
    l_title = tkinter.Message(ds_window, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600, pady=0,
                              fg="white", bg="#333333", justify="center", anchor="center")
    l_title.config(font=("Arial", "50", "bold"))
    l_title.pack(side="top")
    fr1 = tkinter.Frame(ds_window)
    fr1.pack(side="top")
    l1 = tkinter.Message(ds_window, text="Your Transaction History:", font=("Times", 16), padx=100, pady=20, width=1000,
                         bg="black", fg="white", relief="raised")
    l1.pack(side="top")
    fr2 = tkinter.Frame(ds_window)
    fr2.pack(side="top")
    frec = open(acct + "-rec.txt", 'r')
    for line in frec:
        l = tkinter.Message(ds_window, anchor="w", text=line, relief="raised", width=2000)
        l.pack(side="top")
    b = tkinter.Button(ds_window, text="Quit", relief="raised", command=ds_window.destroy)
    b.pack(side="top")
    frec.close()"""
"""def balance(acct):
    data_file = get_data_file_address(acct)
    if data_file is not None:
        fdet = open(data_file, 'r')
        #fdet = open(acct + ".txt", 'r')
        fdet.readline()
        bal = fdet.readline()
        fdet.close()
        messagebox.showinfo("Balance", bal)
        fdet.close()
    else:
        messagebox.showinfo("Error", "Account not found.")"""


def history(acct):
    data_file = get_data_file_address(acct)
    if data_file is not None:
        ds_window = tkinter.Tk()
        ds_window.geometry('340x440')
        ds_window.title("display menu")
        ds_window.configure(bg='#333333')
        tkinter.Frame(ds_window, bg='#333333')
        l_title = tkinter.Message(ds_window, text="BANK MANAGEMENT SYSTEM", relief="raised", width=2000, padx=600,
                                  pady=0,
                                  fg="white", bg="#333333", justify="center", anchor="center")
        l_title.config(font=("Arial", "50", "bold"))
        l_title.pack(side="top")
        fr1 = tkinter.Frame(ds_window)
        fr1.pack(side="top")
        l1 = tkinter.Message(ds_window, text="Your Transaction History:", font=("Times", 16), padx=100, pady=20,
                             width=1000,
                             bg="black", fg="white", relief="raised")
        l1.pack(side="top")
        fr2 = tkinter.Frame(ds_window)
        fr2.pack(side="top")
        free = open(acct + "-rec.txt", 'r')
        for line in free:
            l = tkinter.Message(ds_window, anchor="w", text=line, relief="raised", width=2000)
            l.pack(side="top")
        b = tkinter.Button(ds_window, text="Quit", relief="raised", command=ds_window.destroy)
        b.pack(side="top")
        free.close()
    else:
        messagebox.showinfo("Error", "Account not found.")


"""def login(account_entry, name_entry):
    login_menu = tkinter.Tk()
    login_menu.title("Login form")
    login_menu.geometry('340x440')
    login_menu.configure(bg='#333333')
    frame1 = tkinter.Frame(login_menu, bg='#333333')
    frame1.grid(row=0, column=0)
    title = tkinter.Message(frame1, text="Banking management system", justify="center", anchor="center")
    title.config(font=("Arial", "25", "bold"))
    label = tkinter.Label(frame1, text="Logged in as: " + name_entry, relief="raised", bg="blue3", font=("Times", 16),
                          fg="white",
                          anchor="center", justify="center")

    credit_button = tkinter.Button(
        frame1, text="Credit Amount", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: cr_amt(account_entry, name_entry))

    debit_button = tkinter.Button(
        frame1, text="Debit Amount", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: db_amt(account_entry, name_entry))

    balance_button = tkinter.Button(
        frame1, text="Display Balance", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: balance(account_entry))

    transaction_button = tkinter.Button(
        frame1, text="Display transaction", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: history(account_entry))

    label.grid(row=0, column=0)
    title.grid(row=1, column=0)

    credit_button.grid(row=3, column=0, columnspan=2, pady=12, padx=10)
    debit_button.grid(pady=12, padx=10)
    balance_button.grid(row=3, column=1, columnspan=2, pady=12, padx=10)
    transaction_button.grid(pady=12, padx=10)"""


def login(account_entry, name_entry):
    login_menu = tkinter.Tk()
    login_menu.title("Login form")
    login_menu.geometry('340x440')
    login_menu.configure(bg='#333333')

    frame1 = tkinter.Frame(login_menu, bg='#333333')
    frame1.grid(row=0, column=0)

    title = tkinter.Message(frame1, text="Banking management system", justify="center", anchor="center")
    title.config(font=("Arial", "25", "bold"))
    label = tkinter.Label(frame1, text="Logged in as: " + name_entry, relief="raised", bg="blue3", font=("Times", 16),
                          fg="white",
                          anchor="center", justify="center")

    credit_button = tkinter.Button(
        frame1, text="Credit Amount", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: cr_amt(account_entry, name_entry))

    debit_button = tkinter.Button(
        frame1, text="Debit Amount", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: db_amt(account_entry, name_entry))

    balance_button = tkinter.Button(
        frame1, text="Display Balance", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: balance(account_entry))

    transaction_button = tkinter.Button(
        frame1, text="Display transaction", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: history(account_entry))

    label.grid(row=0, column=0, columnspan=2)
    title.grid(row=1, column=0, columnspan=2)

    credit_button.grid(row=2, column=0, padx=10, pady=10)
    debit_button.grid(row=2, column=1, padx=10, pady=10)
    balance_button.grid(row=3, column=0, padx=10, pady=10)
    transaction_button.grid(row=3, column=1, padx=10, pady=10)

    login_menu.mainloop()


def check_account_no(num):
    try:
        fpin = open(num + ".txt", 'r')
    except FileNotFoundError:
        messagebox.showinfo("Error", "Invalid Credentials!\nTry Again!")
        return 0
    fpin.close()
    return


def check_login(master, name_entry, account_entry, pin_entry):
    if not account_entry:
        messagebox.showinfo("Error", "Please enter an account number.")
        return

    try:
        fin = open(str(account_entry) + ".txt", 'r')
        pin = fin.readline().strip()
        print(pin)
        bal = fin.readline().strip()
        print(bal)
        acct = fin.readline().strip()
        print(acct)
        name = fin.readline().strip()
        print(name)

        fin.close()

        if check_account_no(account_entry) == 0:
            master.destroy()
            main_menu()
            return
        elif name_entry == name and account_entry == acct and pin_entry == pin:
            messagebox.showinfo(title="Success", message="Login successful")
            master.destroy()
            login(account_entry, name_entry)
        else:
            messagebox.showinfo("Error", "Invalid credentials. Please try again.")
            master.destroy()
            main_menu()
    except FileNotFoundError:
        messagebox.showinfo("Error", "Invalid account number. Please try again.")
        return


def logininpage(master):
    master.destroy()
    login_in_page = tkinter.Tk()
    login_in_page.configure(bg='#333333')

    try:
        image = Image.open("images/pattern1.png")
        image_reference = ImageTk.PhotoImage(image)
        l2 = tkinter.Label(login_in_page, image=image_reference)
        l2.pack()
    except Exception as e:
        print("Error loading image:", e)

    frame = tkinter.Frame(l2, width=320, height=360)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # Creating widgets
    login_label = tkinter.Label(
        frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
    name_label = tkinter.Label(
        frame, text="Enter Name:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    name_entry = tkinter.Entry(frame, font=("Arial", 16))
    n = name_entry
    account_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    a = account_entry
    account_label = tkinter.Label(
        frame, text="Enter Account Number:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    pin_label = tkinter.Label(
        frame, text="Enter Pin:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    pin_entry = tkinter.Entry(frame, font=("Arial", 16))
    p = pin_entry
    login_button = tkinter.Button(
        frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: check_login(login_in_page, n.get().strip(), a.get().strip(), p.get().strip()))
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    name_label.grid(row=1, column=0)
    name_entry.grid(row=1, column=1, pady=20)
    account_label.grid(row=2, column=0)
    account_entry.grid(row=2, column=1, pady=20)
    pin_label.grid(row=3, column=0)
    pin_entry.grid(row=3, column=1, pady=20)
    login_button.grid(row=4, column=0, columnspan=2, pady=30)

    frame.pack()


def write(master, name, credit, pin):
    if (is_number(name)) or (is_number(credit) == 0) or (is_number(pin) == 0) or name == "":
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        return

    f1 = open("Accnt_Record.txt", 'r')
    accnt_no = int(f1.readline())
    accnt_no += 1
    f1.close()

    f2=open("record.txt","a")
    f2.write(str(accnt_no)+"\n")
    f2.close()

    f1 = open("Accnt_Record.txt", 'w')
    f1.write(str(accnt_no))
    f1.close()

    fdet = open(str(accnt_no) + ".txt", "w")
    fdet.write(pin + "\n")
    fdet.write(credit + "\n")
    fdet.write(str(accnt_no) + "\n")
    fdet.write(name + "\n")
    fdet.close()

    frec = open(str(accnt_no) + "-rec.txt", 'w')
    frec.write("Date                       Credit        Debit        Balance\n")
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",
                            gmtime())) + "     " + credit + "                      " + credit + "\n")
    frec.close()

    file_name = str(accnt_no) + ".txt"
    file1_address = id(file_name)
    print(file1_address)

    update_index(accnt_no, file1_address)

    messagebox.showinfo("Details", "Your Account Number is:" + str(accnt_no))
    master.destroy()
    main_menu()
    return


def create(master):
    master.destroy()
    create_page = tkinter.Tk()
    create_page.configure(bg='#333333')

    frame = tkinter.Frame(create_page, bg='#333333')
    create_label = tkinter.Label(
        frame, text="Create", bg='#333333', fg="#FF3399", font=("Arial", 30))
    name_label = tkinter.Label(
        frame, text="Enter Name", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    name_entry = tkinter.Entry(frame, font=("Arial", 16))
    n = name_entry
    credit_label = tkinter.Label(
        frame, text="Enter opening credit", bg='#333333', fg="#FFFFFF", font=("Arial", 16))

    credit_entry = tkinter.Entry(frame, font=("Arial", 16))
    c = credit_entry
    pin_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    p = pin_entry
    pin_label = tkinter.Label(
        frame, text="Enter Desired Pin", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    create_button = tkinter.Button(
        frame, text="Create", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: write(create_page, n.get().strip(), c.get().strip(), p.get().strip()))

    create_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    name_label.grid(row=1, column=0)
    name_entry.grid(row=1, column=1, pady=20)
    credit_label.grid(row=2, column=0)
    credit_entry.grid(row=2, column=1, pady=20)
    pin_label.grid(row=3, column=0)
    pin_entry.grid(row=3, column=1, pady=20)
    create_button.grid(row=4, column=0, columnspan=2, pady=30)

    frame.pack()


def main_menu():
    window = tkinter.Tk()
    window.title("banking management system")
    window.geometry('640x440')

    image = Image.open("images/pattern.png")

    image_reference = ImageTk.PhotoImage(image)

    l1 = tkinter.Label(window, image=image_reference)
    l1.pack()

    frame = tkinter.Frame(l1, width=320, height=360)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    login_button = tkinter.Button(
        frame, text="Login", width=220,
        command=lambda: logininpage(window))

    create_button = tkinter.Button(
        frame, text="Create", width=220,
        command=lambda: create(window))

    login_button.place(x=50, y=110)
    create_button.place(x=50, y=165)

    login_button.grid(row=3, column=0, columnspan=2, pady=12, padx=10)
    create_button.grid(pady=12, padx=10)

    window.mainloop()


main_menu()
