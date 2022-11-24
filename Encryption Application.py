# encryption.py
# Celine Yeung, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.

def encode_dict(values):
    """Makes a dictionary for the intial process for encoding
       
       Parameter:
       values -- a list of string elements that are going to be the values in the dictionary (arguement - users cipher text)

       Function:
       Makes a dictionary where the cipher text elements inputted by the user becomes the values of the dictionary and a list of 26 letters 
       of the alphabet become the keys which is then returned to be used in the next steps in the encoding process
    """
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dict_1 = dict(zip(keys, values))
    return dict_1

def decode_dict(keys):
    '''Makes a dictionary for the inital process for decoding
       
       Parameter:
       keys -- a list of string elements that are going to be keys in a dictionary (arguement - users cipher text)

       Function:
       Makes a dictionary where the cipher text elements inputted by the user becomes the keys of the dictionary and the 26 letters of the
       alphabet become the values which is then returned to be used in the next step in the decoding process
    '''
    values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dict_2 = dict(zip(keys, values))
    return dict_2

def main_process(text, dict):
    """ Encodes or decodes the text the user wants to be processed depending on their selection of the encryption program and the
        dictionary that is is passed through the function and prints the new text. 
        
        Arguement:
        text -- string to be encoded or decoded
        dict -- dictionary that will be used to encode or decode the text

        Function:
        Using the dictionary returned from either the first or the second defined function: For every element of the text the user wants to
        be encoded or decoded it is looked through the dictionary as a key and its corresponding value in the dictionary is added to 
        the string variable 'output'. Once the entire text has been looked through then the function prints 'output' which is the 
        encoded or decoded text. 
    """
    output = ''
    r = 0
    while r < len(text):
        output += dict[text[r]]
        r += 1
    print('Your output is:', output)
    
#Loop the main menu to ask user if they want to encode or decode until they end the program. 
print("ENDG 233 Encryption Program")
i = 0
while i == 0:
    user_selection = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit: '))
    if user_selection == 0: #If user chooses zero, the loop breaks and the encryption program ends
        break

    text_to_be_processed = input('Please enter the text to be processed: ')
    cipher = input('Please enter a cipher text of elements of a-z or 0-9: ')

    #Check if cipher is alphanumeric. If it is make a new cipher where there are no duplicates and each letter of the cipher is made into lowercase
    new_cipher = []
    if (cipher.isalnum()) == True:
        new_cipher = sorted(set((cipher.lower())), key=(cipher.lower()).index)

        #Check if cipher is 26 elements 
        if len(new_cipher) == 26:
            print('Your cipher is valid.')
    
            #Make string input into a list for it to used in the zip() function in the defined functions
            if user_selection == 1 or 2:
                cipher_elements = list(new_cipher) 

                #Calling functions to make dictionary, encode and decode.
                if user_selection == 1:
                    encoding_dict = encode_dict(cipher_elements)
                    main_process(text_to_be_processed, encoding_dict)
                else: 
                    decoding_dict = decode_dict(cipher_elements)
                    main_process(text_to_be_processed, decoding_dict)

        #This print statement states to the user that their cipher doesn't meet the criteria
        else:
            print('Your cipher is invalid. It must contain 26 unique elements of a-z or 0-9.')
    else:
        print('Your cipher is invalid. It must contain 26 unique elements of a-z or 0-9.') 

print('Thank you for using the encryption program.')