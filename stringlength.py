'''
Use find and string slicing to extract the portion of the string after the colon
character and then use the float function to convert the extracted string into a
floating point number.
'''

'''strng = raw_input ('what is the string? ')
stp = strng.find(":")
new_value = strng[(stp+1):]
new_value = float(new_value)
print new_value
print type(new_value)
'''

##data = 'From stephen.marquard@uct.ac.za Sat Jan

data = raw_input ('what is the data? ')
strtpoint = data.find('@')
print strtpoint
endpoint = data.find(' ',strtpoint)
print endpoint
domain = data[strtpoint+1:endpoint]
print domain
