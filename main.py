import random # need to generate random numbers for the slot machine

MAX_LINES = 3 # the maximum number of lines that a player can bet on # its a constant variable  because its value will not change throughout the program
MAX_BET = 20
MIN_BET = 1

ROWS = 3
COLS= 3

# we want the symbols to be generated randomly and we want to have a certain number of each symbol in the slot machine # we can use a dictionary to store the symbols and their count
symbol_count = {   
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
      symbol = columns[0][line]
      for column in columns:
          symbol_to_check = column[line]
          if symbol != symbol_to_check:
              break
      else:
          winnings += values[symbol] * bet
          winnings_lines.append(line + 1)

    return winnings, winnings_lines
  
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    #easy way to select the random values and randomly choose the values 
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []      
    for _ in range(cols): # loop through the number of values needed for each column
        column = [] # empty list to store the symbols for the current column
        current_symbols = all_symbols[:] # copy all_symbols so we can modify it without affecting the original list
        for row in range(rows):
            value = random.choice(current_symbols) # randomly select a symbol from the current_symbols list
            current_symbols.remove(value) # remove the selected symbol so it cannot be selected again
            column.append(value) # add the selected symbol to our column list
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): # loop through each column and its index
            end_char = " | " if i < len(columns) - 1 else ""
            print(column[row], end=end_char)
        print()


def deposit():
    while True:
      
        amount = input("What should you like to deposit? $ ")
        if amount.isdigit(): # the amount should  be a number # the negative number wont be valid 
            amount = int(amount) # by depault its a string 
            if amount > 0:
                break # ends the loop if the amount is valid
            else:
                print("Amount must be greater than 0.") ## the amount is  not valid if its less than 0
        else:
            print("Please enter a number.")

    return amount


def get_numnber_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+ str(MAX_LINES) + ")? ") # concatenation is done #  added a max line 
        if lines.isdigit():
             lines = int(lines)
             if 1 <= lines <= MAX_LINES:
                 break
             else:
                 print("Enter a valid number of lines.")

        else:
                print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line ? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
              break
            else:
              print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") # can be converted asa string by using f string 
        else: # no need to convert it will be a string by default
                print("Please enter a number.")

    return amount
    
    
def spin(balance):
        lines = get_numnber_of_lines()# can rereum the value of the get_numnber_of_lines function to the lines variable
        while True:
            bet = get_bet() # can rereum the value of the get_bet function to the bet function
            total_bet = bet * lines # the total bet is equal to the bet on each line multiplied by the number of lines
            if total_bet > balance:
                print(f"You do not have enough balance to bet that amount, your current balance is: ${balance}") # can be converted as a string by using f string
            else:
                break
        print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}") # can be converted asa string by using f string
        
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count) # can return the value of the get_slot_machine_spin function to the slots variable
        print_slot_machine(slots) # can pass the slots variable to the print_slot_machine function to print the slot machine
        winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_count) # can return both winnings and winning lines
        print(f"You won ${winnings}.") # can be converted asa string by using f
        if winnings_lines:
            print("You won on lines:", *winnings_lines)
        else:
            print("You won on lines:")
        return winnings - total_bet # the total winnings is equal to the winnings minus the total bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}  ")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance) # spin will returm the winnings minus the total bet, so we add it to the balance to update it after each spin
        print(f"you left with ${balance}.")
        
main()