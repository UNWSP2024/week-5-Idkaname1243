# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):
    miles = 0.0
    miles = kilometers * 0.6214
    miles = str(miles)
    print("your distance in miles is "+ miles)

    return miles
kilometers = int(input("enter distance in kilometers:   "))
kilometer_conversion(kilometers)
#### This piece of the code has been done for you,
#### you only need to worry about the actual temp 
#### conversion logic in the temp_conversion function
#if __name__ == '__main__':
    # Get User Input
    #print('in main')
    # Call kilometer_conversion
    # Display the miles
