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
        #self.transfer_funds = ""
        self.USR = {}
    def create_customer(self):
        self.cid = input("Enter Customer ID: ")
        self.cname = input("Enter Customer Name: ")
        self.acc_no = input("Enter Account Number: ")
        self.USR["User"] = {"CID": self.cid, "Cname": self.cname, "acc_no": self.acc_no, "Credit Cards": self.credit_card, "Balance": self.balance}
    def display_customer(self):
        print("User ID: "+self.cid)
        print("User Name: "+self.cname)
        print("User Account Number: "+self.acc_no)
        print("User Balance: "+self.balance)
        print("User's Credit Cards: "+self.credit_card)
    def assign_card(self, creditC):
        self.credit_card.append(creditC)
        for i in range(len(RCL)):
            if (RCL[i].card_no == creditC):
                self.balance = RCL[i].balance

    def transfer_funds(self, Transfer_to_Account, Amount, SAccount_Num, CardOP):
        for i in range(len(RCL)):
                if (RL[i].cid == SAccount_Num):
                    for b in range(len(RCL)):
                        if (RCL[b].card_no == RL[i].credit_card[CardOP]):
                            RCL[b].balance -= Amount
                            RL[i].balance = RCL[b].balance
                            for c in range(len(RL)):
                                if (RL[c].cid == Transfer_to_Account):
                                    RL[c].balance += Amount
                                    for d in range(len(RCL)):
                                        if (RCL[d].card_no == RL[c].credit_card[CardOP]):
                                            RCL[d].balance += Amount
                        
                    
        

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
        print("Card Number: "+self.card_no)
        print("Card CVV: "+self.cvv)
        print("Card Expiration Date: "+self.expiry_date)
        print("Card Balance: "+self.balance)

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
                RL.append(NUser)
            elif(UI == "2"):
                UI = input("Enter Customer ID: ")
                for i in range(len(RL)):
                    if (RL[i].cid == UI):
                        print(RL[i].display_customer())
            elif(UI == "3"):
                SA = input("Enter your Customer ID: ")
                TTA = input("Enter Customer ID you wish to transfer money to: ")
                A = int(input("Enter the amount you wish to transfer: "))
                CO = int(input("Which card do you wish to use?(EX: 0 for first card, 1 for second card, etc.): "))
                for i in range(len(RL)):
                    if (RL[i].cid == SA):
                        print(RL[i])
                        RL[i].transfer_funds(TTA, A, SA, CO)
                
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
                RCL.append(NCard)
                
                
            elif(UI == "2"):
                UI = input("Enter Card Number: ")
                for i in range(len(RCL)):
                    if (RCL[i].card_no == UI):
                        print(RCL[i].display_card())
            elif(UI == "3"):
                UCS = input("Enter Card Number: ")
                UI = input("Enter Customer ID: ")
                for i in range(len(RL)):
                    if (RL[i].cid == UI):
                        for b in range(len(RCL)):
                            if (RCL[b].card_no == UCS):
                                RL[i].assign_card(UCS)
                                
                                
            elif(UI == "4"):
                break
                                
    elif(UC == "4"):
        break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
