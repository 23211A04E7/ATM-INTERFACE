import tkinter as tk
from tkinter import messagebox,simpledialog


# Sample account data (can be replaced with database integration)
accounts = {
    '123456': {
        'name': 'John Doe',
        'balance': 5000
    },
    '654321': {
        'name': 'Jane Smith',
        'balance': 3000
    }
}

class ATMInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Interface")
        self.master.geometry("400x400")
        self.master.config(background='#102C57')
        
        self.title=tk.Label(master,text='WELCOME TO ATM',font=('Helvetica',24,'bold'),fg='black',bg='white',bd=6,width=40,relief='raised')
        self.title.pack()
        self.account_label = tk.Label(master, text="Enter Account Number:", font=('Helvetica',20,'bold'),fg='black',bg='white',bd=6,width=20,relief='solid')
        self.account_label.pack(pady=20)

        self.account_entry = tk.Entry(master,width=30,bd=10,relief="raised")
        self.account_entry.pack()

        self.pin_label = tk.Label(master, text="Enter PIN:", font=('Helvetica',20,'bold'),fg='black',bg='white',bd=6,width=20,relief='solid')
        self.pin_label.pack(pady=20)

        self.pin_entry = tk.Entry(master, show="*",width=30,bd=10,relief="raised")
        self.pin_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login, fg="black", bg="white",bd=10,relief="raised")
        self.login_button.pack(pady=20)

        # Frame for ATM operations
        self.operations_frame = tk.Frame(master,bd=10,relief="raised",width=30)

        self.balance_button = tk.Button(self.operations_frame, text="Check Balance", command=self.check_balance, fg="black", bg="white")
        self.balance_button.pack(pady=10)

        self.withdraw_button = tk.Button(self.operations_frame, text="Withdraw", command=self.withdraw, fg="black", bg="white")
        self.withdraw_button.pack(pady=10)

        self.deposit_button = tk.Button(self.operations_frame, text="Deposit", command=self.deposit, fg="black", bg="white")
        self.deposit_button.pack(pady=10)

        self.transfer_button = tk.Button(self.operations_frame, text="Transfer", command=self.transfer, fg="black", bg="white")
        self.transfer_button.pack(pady=10)

        self.operations_frame.pack(pady=20)

        self.logout_button = tk.Button(master, text="Logout", command=self.logout, fg="black", bg="white",bd=10,relief="raised")
        self.logout_button.pack(pady=10)

        # Initially hide the operations frame
        self.operations_frame.pack_forget()

        self.current_account = None

    def login(self):
        account_number = self.account_entry.get()
        pin = self.pin_entry.get()

        if account_number in accounts and pin == '1234':  # Simulated PIN verification
            self.current_account = account_number
            messagebox.showinfo("Success", "Login successful!")
            self.account_entry.delete(0, tk.END)
            self.pin_entry.delete(0, tk.END)
            self.show_operations()
        else:
            messagebox.showerror("Error", "Invalid account number or PIN!")

    def show_operations(self):
        self.account_label.pack_forget()
        self.account_entry.pack_forget()
        self.pin_label.pack_forget()
        self.pin_entry.pack_forget()
        self.login_button.pack_forget()

        self.operations_frame.pack(pady=20)

    def check_balance(self):
        balance = accounts[self.current_account]['balance']
        messagebox.showinfo("Balance", f"Balance: ₹{balance}")

    def withdraw(self):
        withdraw_amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:")
        if withdraw_amount is not None:
            if withdraw_amount > 0:
                current_balance = accounts[self.current_account]['balance']
                if withdraw_amount <= current_balance:
                    accounts[self.current_account]['balance'] -= withdraw_amount
                    messagebox.showinfo("Success", f"Withdraw successful! Remaining balance: ₹{accounts[self.current_account]['balance']}")
                else:
                    messagebox.showerror("Error", "Insufficient balance!")
            else:
                messagebox.showerror("Error", "Please enter a valid amount!")

    def deposit(self):
        deposit_amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:")
        if deposit_amount is not None:
            if deposit_amount > 0:
                accounts[self.current_account]['balance'] += deposit_amount
                messagebox.showinfo("Success", f"Deposit successful! Current balance: ${accounts[self.current_account]['balance']}")
            else:
                messagebox.showerror("Error", "Please enter a valid amount!")

    def transfer(self):
        transfer_amount = simpledialog.askinteger("Transfer", "Enter amount to transfer:")
        if transfer_amount is not None:
            if transfer_amount > 0:
                transfer_to = simpledialog.askstring("Transfer", "Enter account number to transfer to:")
                if transfer_to in accounts and transfer_to != self.current_account:
                    current_balance = accounts[self.current_account]['balance']
                    if transfer_amount <= current_balance:
                        accounts[self.current_account]['balance'] -= transfer_amount
                        accounts[transfer_to]['balance'] += transfer_amount
                        messagebox.showinfo("Success", f"Transfer successful! Remaining balance: ₹{accounts[self.current_account]['balance']}")
                    else:
                        messagebox.showerror("Error", "Insufficient balance!")
                else:
                    messagebox.showerror("Error", "Invalid account number!")
            else:
                messagebox.showerror("Error", "Please enter a valid amount!")

    def logout(self):
        self.operations_frame.pack_forget()

        self.account_label.pack()
        self.account_entry.pack()
        self.pin_label.pack()
        self.pin_entry.pack()
        self.login_button.pack()

        self.current_account = None


def main():
    root = tk.Tk()
    atm_interface = ATMInterface(root)
    root.mainloop()
if __name__ == "__main__":
    main()