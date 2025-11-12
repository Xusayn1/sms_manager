import json

def load_cardInfo () -> dict :
    try :
        with open("exam.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            return {k: v for k, v in data.items()}
    except (json.JSONDecodeError, KeyError, ValueError) :
        print("Error reading exam data file. Starting with empty exam data.")
        return {}

def save_cardInfo(c:dict) -> bool:
    try :
        with open("exam.json", 'w', encoding='utf-8') as file:
            json.dump(c, file,  indent=4)
            return True
    except :
        print("Error saving exam data file. Starting with empty exam data.")
        return False


def cardBalance (c:dict ) :
    for card_type,card_info in c.items():
        if "balance" in card_info :
            print(f" karta turi: card {card_type} \n sizning balansingiz : {card_info["balance"]}")


def deposit(c: dict, auth_card:str):
    if auth_card in c:
        if "balance" in c[auth_card]:
            try:
                amount = int(input("Enter amount to deposit: "))
                c[auth_card]["balance"] += amount
                print(f'Payment is done successfully! New balance: {c[auth_card]["balance"]}')
                return True
            except ValueError:
                print("Invalid amount entered.")
                return False
    else:
        print("Card not found.")
        return False

def withdraw(c: dict,auth_card:str):

    if auth_card in c:
        if "balance" in c[auth_card]:
            try:
                amount = int(input("Enter amount to withdraw: "))
                c[auth_card]["balance"] -= amount
                print(f'operation is done successfully! New balance: {c[auth_card]["balance"]}')
                return True
            except ValueError:
                print("Invalid amount entered.")
                return False
        else:
            print("Card not found.")
            return False

def smsMessage(c: dict, auth_card:str):
    if auth_card in c:
        if "sms info" in c[auth_card]:
            current_status = c[auth_card]["sms info"]
            print(f'current status is = {current_status}')
            print("Do you want to change SMS notification status?")
            print("1. Yes")
            print("2. No")

            request = input("Enter your choice: ")

            if request == '1' :
                if current_status == "off":
                    c[auth_card]["sms info"] = "on"
                    print(f'SMS operation is done successfully!')
                    return True
                elif current_status == "on":
                    c[auth_card]["sms info"] = "off"
                    print(f'SMS operation is done successfully!')
                    return True
            elif request == '2':
                return '-----main menu----'
    else:
        print("Card not found.")
        return False


def auth () :
    data = load_cardInfo()
    card_type = input("Enter card type: ")
    attemp = 3
    if card_type in data:
        while attemp > 0 :
            pin_code = input("Enter pin code: ")
            if data[card_type]["pin code"] == pin_code :
                print(f"Card {card_type} successfully authorized.")
                return card_type
            else :
                attemp -= 1
                if attemp > 0 :
                    print(f' your attemp {attemp} remained. Try again.')
                else:
                    print('pin code is invalid. No attemps left.')

                    print(f"Card {card_type} not authorized.")
                    return False
    else:
        print(f"Card type {card_type} not found.")
        return False

def manager_for_bank_machine():
    data = load_cardInfo()
    auth_card = auth()
    if auth_card :
        print('you are authorized ')
        while True:
            print(' 1. view balance \n 2. deposit \n 3. withdraw \n 4. smsMessage \n 5. exit')
            options = input("Enter your choice:=  ")
            if options == "1" :
                if "balance" in data[auth_card]:
                    print(f"Card balance: {data[auth_card]['balance']}")
            elif options == "2" :
                if deposit(data, auth_card) :
                    save_cardInfo(data)
            elif options == "3" :
                if withdraw(data, auth_card) :
                    save_cardInfo(data)
            elif options == "4" :
                if smsMessage(data, auth_card) :
                    save_cardInfo(data)
            elif options == "5" :
                print("Exiting...")
                break
            else :
                print("Invalid option entered. try again.")
                break
    else :
        print('you are not authorized.')


if __name__ == "__main__":
    print("=== BANK ATM SYSTEM ===")
    manager_for_bank_machine()