class DataValidator:
    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        return False
    
    @staticmethod
    def validate_url(url):
        if "http" in url or "https" in url:
            return True
        return False
    
    @staticmethod
    def validate_date(day, month, year):
        months31 = [1, 3, 5, 7, 8, 10, 12]
        months30 = [4, 6, 9, 11]
        
        if month <= 12 and month > 0:
            if month in months31 and 1 <= day <= 31:
                return True
            elif month in months30 and 1 <= day <= 30:
                return True
            elif month == 2:
                if (year % 4 == 0 and 1 <= day <= 29) or (year % 4 != 0 and 1 <= day <= 28):
                    return True
        return False
    
    @staticmethod
    def validate_number(number):
        try:
            int(number)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number) == 12 and phone_number[:4] == "+374":
            return True
        if len(phone_number) == 9 and phone_number[0] == "0" and phone_number[1] != "0":
            return True
        return False
    
    @staticmethod
    def validate_credit_card(card_number):
        if len(card_number) == 16:
            return True
        return False

def main():
    print("Select a data type to validate:")
    print("1. Email")
    print("2. URL")
    print("3. Date")
    print("4. Number")
    print("5. Phone number")
    print("6. Credit card")
    
    choice = int(input())
    
    if choice == 1:
        email = input("Enter email: ")
        if DataValidator.validate_email(email):
            print("Valid email address.")
        else:
            print("Invalid email address.")
    elif choice == 2:
        url = input("Enter URL: ")
        if DataValidator.validate_url(url):
            print("Valid URL.")
        else:
            print("Invalid URL.")
    elif choice == 3:
        day = int(input("Enter day: "))
        month = int(input("Enter month: "))
        year = int(input("Enter year: "))
        if DataValidator.validate_date(day, month, year):
            print("Valid date.")
        else:
            print("Invalid date.")
    elif choice == 4:
        number = input("Enter number: ")
        if DataValidator.validate_number(number):
            print("Valid number.")
        else:
            print("Invalid number.")
    elif choice == 5:
        phone_number = input("Enter phone number: ")
        if DataValidator.validate_phone_number(phone_number):
            print("Valid phone number.")
        else:
            print("Invalid phone number.")
    elif choice == 6:
        card_number = input("Enter credit card number: ")
        if DataValidator.validate_credit_card(card_number):
            print("Valid credit card number.")
        else:
            print("Invalid credit card number.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
