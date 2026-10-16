def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha():
            return True
        if s[0].isalpha() and s[1].isalpha():

            for char in s:
                if char.isdigit():
                    if char == "0":
                        return False
                    if s[s.index(char):].isdigit():
                        return True
                                            
main()