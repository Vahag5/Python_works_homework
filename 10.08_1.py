def chek_parametr():
    print("Ete uzum eq stugel parametr@ nsheq hamapatasxan tiv@`\n",
          "E-mail = '1'\n",
          "URL = '2'\n",
          "Date = '3'\n",
          "Number = '4'\n",
          "Phone_number = '5'\n",
          "Credit_Card_number = '6'\n"
          "Cragric durs galu hamar = '0'\n")
    
    while True:
        x = int(input())
        
        if x == 1:
            Email = input("Write Email: ")
            if '@' in Email and '.' in Email:
                return True
            return False
        elif x == 2:
            URL = input("Write WEBSITE URL: ")
            if "http" in URL or "https" in URL:
                return True 
            return False
        elif x == 4:
            Number = input("Write number: ")
            if Number.isdigit():
                return True
            return False
        elif x == 5:
            Phone_number = input("Write Phone number: ")
            if Phone_number[:4] == "+374" and len(Phone_number) == 12:
                return True
            elif Phone_number[0] == '0' and Phone_number[1] != '0' and len(Phone_number) == 9:
                return True  
            return False
        elif x == 3:
            months31 = "135781012"
            months30 = "46911"
            day = int(input("Write day: "))
            month = input("Write month (as a digit): ")
            year = int(input("Write year: "))
            
            if int(month) <= 12 and int(month) > 0:
                if month in months31 and 1 <= day <= 31:
                    print(f"{day}.{month}.{year}")
                    return True
                elif month in months30 and 1 <= day <= 30:
                    print(f"{day}.{month}.{year}")
                    return True
                elif int(month) == 2:
                    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and 1 <= day <= 29:
                        print(f"{day}.{month}.{year}")
                        return True
                    elif year % 4 != 0 and 1 <= day <= 28:
                        print(f"{day}.{month}.{year}")
                        return True
                return False
        elif x == 6:
            Credit_Card_number = input("Write Credit_Card_number (without space): ")
            if len(Credit_Card_number) == 16 and Credit_Card_number.isdigit():
                return True
            return False
        elif x == 7:
            return False
        

if chek_parametr() == True:
    print("is True parametr")
else:
    print("is False parametr")

