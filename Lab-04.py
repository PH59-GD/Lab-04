import pickle
RL = []
class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.balance = ""
        self.credit_card = []
        self.transfer_funds = ""
        self.USR = {}
    def create_customer(self):
        self.cid = input("Enter Customer ID: ")
        self.cname = input("Enter Customer Name: ")
        self.acc_no = input("Enter Account Number: ")
        self.USR["User"] = {"CID": self.cid, "Cname": self.cname, "acc_no": self.acc_no, "Credit Cards": self.credit_card}
    def display_customer(self):
        print(self.cid)
        print(self.cname)
        print(self.acc_no)
        print(self.balance)
        print(self.credit_card)
    def assign_card(self, creditC):
        self.credit_card.append(creditC)
        self.balance = creditC.CRD["Card"]["Balance"]

    def transfer_funds(self, Transfer_to_Account, Amount):
        

class Card:
    def __init__(self):
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = ""
        self.CRD = {}
    def create_card(self):
        self.card_no = input("Enter Card Number: ")
        self.cvv = input("Enter CVV Number: ")
        self.expiry_date = input("Enter Card expiration(EX: 01/26): ")
        self.balance = int(input("Enter Card Balance: "))
        self.CRD["Card"] = {"Card Num": self.card_no, "CVV": self.cvv, "Expiry Date": self.expiry_date, "Balance": self.balance}
    def display_card(self):
        print(self.card_no)
        print(self.cvv)
        print(self.expiry_date)
        print(self.balance)
try:
    File3 = open("Customers.dat", "rb")
    while True:
        try:
            data = pickle.load(File3)
            #print(data.USR)
            RL.append(data.USR)
        except(EOFError):
            break
    File3.close()
except(FileNotFoundError):
    print("No Accounts Created!")
while True:
    print("")
    print("[1] Customer")
    print("[2] Card")
    print("[3] Exit")
    print("")
    UC = input("Input: ")
    if (UC == "1"):
        while True:
            print("")
            print("[1] Create Customer")
            print("[2] Display Customer")
            print("[3] Transfer Funds")
            print("[4] Exit")
            print("")
            UI = input("Input: ")
            if(UI == "1"):
                NUser = Customer()
                NUser.create_customer()
                File1 = open("Customers.dat", "ab")
                pickle.dump(NUser, File1)
                File1.close()

            elif(UI == "2"):
                File2 = open("Customers.dat", "rb")
                RL = []
                while True:
                    try:
                        data = pickle.load(File2)
                        print(data.USR)
                        RL.append(data.USR)
                    except(EOFError):
                        break
                File2.close()
                print(RL)


    elif(UC == "2"):
        while True:
            print("")
            print("[1] Create Card")
            print("[2] Display Card")
            print("[3] Assign card")
            print("[4] Exit")
            print("")
    elif(UC == "3"):
        break
