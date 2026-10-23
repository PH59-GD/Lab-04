import pickle
RL = []
RCL = []
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
        self.USR["User"+str(len(RL))] = {"CID": self.cid, "Cname": self.cname, "acc_no": self.acc_no, "Credit Cards": self.credit_card}
    def display_customer(self):
        print(self.cid)
        print(self.cname)
        print(self.acc_no)
        print(self.balance)
        print(self.credit_card)
    def assign_card(self, creditC):
        self.credit_card.append(creditC)
        self.balance = creditC.CRD["Card"]["Balance"]

    #def transfer_funds(self, Transfer_to_Account, Amount):
        

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
        self.CRD["Card"+str(len(RCL))] = {"Card Num": self.card_no, "CVV": self.cvv, "Expiry Date": self.expiry_date, "Balance": self.balance}
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
    print("")
    print("WARNING! ''Customers.dat'' not found!")
    print("You must create a user!")
    
try:
    File6 = open("Cards.dat", "rb")
    while True:
        try:
            data = pickle.load(File6)
            #print(data.USR)
            RCL.append(data.CRD)
        except(EOFError):
            break
    File6.close()
except(FileNotFoundError):
    print("")
    print("WARNING! ''Cards.dat'' not found!")
    print("You must create a card!")
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
                try:
                    File9 = open("Customers.dat", "rb")
                    RL = []
                    while True:
                        try:
                            data = pickle.load(File9)
                            #print(data.USR)
                            RL.append(data.USR)
                        except(EOFError):
                            break
                    File9.close()
                    #print(RL)
                except(FileNotFoundError):
                    print("Error!")
            elif(UI == "4"):
                break
            elif(UI == "2"):
                
                try:
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
                    #print(RL)
                except(FileNotFoundError):
                    print("No Customers to display!")
            elif(UI == "4"):
                break
            

    elif(UC == "2"):
        while True:
            print("")
            print("[1] Create Card")
            print("[2] Display Card")
            print("[3] Assign card")
            print("[4] Exit")
            print("")
            UI = input("Input: ")
            if(UI == "1"):
                NCard = Card()
                NCard.create_card()
                File4 = open("Cards.dat", "ab")
                pickle.dump(NCard, File4)
                File4.close()
                try:
                    File10 = open("Cards.dat", "rb")
                    RL = []
                    while True:
                        try:
                            data = pickle.load(File10)
                            #print(data.USR)
                            RCL.append(data.CRD)
                        except(EOFError):
                            break
                    File10.close()
                    #print(RL)
                except(FileNotFoundError):
                    print("ERROR!")
            elif(UI == "2"):
                try:
                    File5 = open("Cards.dat", "rb")
                    RCL = []
                    while True:
                        try:
                            data = pickle.load(File5)
                            print(data.CRD)
                            RCL.append(data.CRD)
                        except(EOFError):
                            break
                    File5.close()
                    #print(RL)
                except(FileNotFoundError):
                    print("No Cards to display!")
            elif(UI == "3"):
                US = input("Enter Customer ID: ")
                UCS = input("Enter Card Number: ")
                for i in range(len(RL)):
                    if(RL[i]["User"+str(i)]["CID"] == US):
                        print("1")
                        for b in range(len(RCL)):
                            print("2")
                            if(RCL[b]["Card"+str(b)]["Card Num"] == UCS):
                                print("3")
                                #RL[i]["User"+str(i+1)]["Credit Cards"].append(RCL[b]["Card"+str(b+1)]["Card Num"])
                                
                                File7 = open("Customers.dat", "rb")
                                #while True:
                                    #try:
                                data = pickle.load(File7)
                                for c in range(len(RL)):
                                    print("4")
                                    if(data.USR["User"+str(c)]["CID"] == US):
                                        print("5")
                                        
                                        data.USR["User"+str(i)]["Credit Cards"].append(RCL[b]["Card"+str(b)]["Card Num"])
                                        print(data.USR["User"+str(i)]["Credit Cards"])
                                        #print(RL[i]["User"+str(i)]["Credit Cards"].append(RCL[b]["Card"+str(b)]["Card Num"]))
                                        File8 = open("Customers.dat", "wb")
                                        pickle.dump(data, File8)
                                        File8.close()
                                        
                                #RL.append(data.USR)
                                
                            #except(EOFError):
                                #break
                                File7.close()
            elif(UI == "4"):
                break
                                
    elif(UC == "4"):
        break
