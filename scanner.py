def codeFilter(code: str) -> bool:
    #code filter function
    return type(code) == str and code is not None and code != ""

while True:
    code = input()
    #remaining code will only run when a code is scanned
    if code == "exit":
        break
    if codeFilter(code):
        print(code)