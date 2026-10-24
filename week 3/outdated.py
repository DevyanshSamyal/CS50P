def main():
    print(date())    

def date():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December" ]

    while True:
        try:
            input_date = input("Date: ").strip()

            if "/" in input_date:    
                date=input_date.split("/")
                if int(date[0]) in range(1,13) and int(date[1]) in range(1,32):
                    return f"{date[2]}-{int(date[0]):02}-{int(date[1]):02}"
                else:
                    continue      
                
            elif "," in input_date:
                date = input_date.title().split(" ")
                if date[0] in months and int(date[1].strip(',')) in range(1,32):
                    return f"{date[2]}-{months.index(date[0])+1:02}-{int(date[1].strip(',')):02}"

        except (IndexError, ValueError):
            continue
    
main()