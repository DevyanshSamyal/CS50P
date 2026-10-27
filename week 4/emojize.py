from emoji import emojize

str = input("Input: ")
print(f"Output: {emojize(str, language='alias')}")