# FILE NAME - convert_C_to_F_02.py

# NAME: zahra romain
# DATE: 4-2-2026
# BRIEF DESCRIPTION:  This program allows the user to convert temperatures between Celsius and Fahrenheit
# by selecting an option from a menu and entering a temperature value.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
def main():
    print("===== Temperature Converter =====")
    print()
    print("  1. Convert from Celsius to Fahrenheit")
    print("  2. Convert from Fahrenheit to Celsius")
    print()
    
    choice = input("Please choose from the above menu: ")
    temperature = float(input("Enter a temperature to convert: "))
    print()
    
    if choice == "1":
        result = temperature * 9/5 + 32
        print(f"{temperature} degrees Celsius is {result} degrees Fahrenheit.")
    else:
        result = (temperature - 32) * 5/9
        print(f"{temperature} degrees Fahrenheit is {result} degrees Celsius.")

main()









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
One lesson I learned in this lab is how to use conditional statements to control the flow of a program based on user input
 By using an if statement, I can decide which temperature conversion formula to apply depending on 
 whether the user chooses Celsius to Fahrenheit or Fahrenheit to Celsius.






'''
