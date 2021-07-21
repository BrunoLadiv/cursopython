from email.errors import MultipartInvariantViolationDefect
import json
#
# try:
#     file = open("abc.txt", "w+")
#     file.write('teste')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.closed
#
#
# with open("abc.txt", "a+") as file: #a+ adiciona ao arquivo, w+ apaga arquivo
#     file.write('teste')
#     file.seek(0)
#     print(file.read())




d1 = {
    'pessoa1': {
        'nome': 'Maria',
        'idade': 25,
        },
    'pessoa2':{
        'nome': 'Jose',
        'idade': 30,
    }
}




test = json.dumps(d1)
with open('jsonlist.txt', 'w+') as file:
    file.write(test)



print(test)

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exist
#
#
# In addition you can specify if the file should be handled as binary or text mode
#
# "t" - Text - Default value. Text mode
#
# "b" - Binary - Binary mode (e.g. images)