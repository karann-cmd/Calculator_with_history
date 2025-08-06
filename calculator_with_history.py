History_file = "History.txt"

def show_history():
    file = open(History_file, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No History Found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()
    
def clear_history():
    file = open(History_file,'w')
    file.close()
    print("History Cleared. ")
    
    
def save_to_history(equation, result):
    file = open(History_file, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    allowed_chars = "0123456789+-*/.() "
    
    result = eval(user_input)
    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)
                
    
def main():
    print('---SIMPLE CALCULATOR (type History, Clear or Exit)')
    while True:
        user_input =  input("Enter Calculation ( +,-,*,/) or command (history, clear or exit): ")
        
        if user_input == 'exit':
            print("Good Bye.")
            break
        if user_input == 'history':
            show_history()
        if user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)
main()
    