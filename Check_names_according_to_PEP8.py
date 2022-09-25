#import packages
import sys
import os
import glob
import re
# Function returns indentation value of string if there is indentation else returns 4
def get_indentation(string):
    if (len(string) - len(string.lstrip())) > 0 and string != "\n":
        return len(string) - len(string.lstrip())
    else:
        return 4

# Function returns boolean value equal to True if length of string is greater than 79
def message_1(string):
    Mistake_Found = False
    if len(string) > 79:
        Mistake_Found = True
    return Mistake_Found

# Function returns boolean value equal to True if indentation not a multiple of 4
def message_2(string):
    Mistake_Found = False
    indentation = get_indentation(string)
    if indentation % 4 != 0:
        Mistake_Found = True
    return Mistake_Found

# Function returns boolean value equal to True if there is unnecessary semicolon after a statement (semicolons are acceptable in comments)
def message_3(string):
    Mistake_Found = False

    if "'" in string:
        index_first_one_quote = string.find("'", string.index("'") + 1)
        comments_start_one = string.find('#', index_first_one_quote + 1)
        comments_start_two = string.find('/*', index_first_one_quote + 1)
        if comments_start_one != -1 and comments_start_two != -1:
            end = min(comments_start_one, comments_start_two)
        if comments_start_one == -1 and comments_start_two == -1:
            end = -1
        if comments_start_one != -1 and comments_start_two == -1:
            end = comments_start_one
        if comments_start_one == -1 and comments_start_two != -1:
            end = comments_start_two
        semicolon_index = string.find(';', index_first_one_quote + 1, end)
        if semicolon_index != -1:
            Mistake_Found = True

    if '"' in string:
        index_first_two_quote = string.find('"', string.index('"') + 1)
        comments_start_one = string.find('#', index_first_two_quote + 1)
        comments_start_two = string.find('/*', index_first_two_quote + 1)
        if comments_start_one != -1 and comments_start_two != -1:
            end = min(comments_start_one, comments_start_two)
        if comments_start_one == -1 and comments_start_two == -1:
            end = -1
        if comments_start_one != -1 and comments_start_two == -1:
            end = comments_start_one
        if comments_start_one == -1 and comments_start_two != -1:
            end = comments_start_two
        semicolon_index = string.find(';', index_first_two_quote + 1, end)
        if semicolon_index != -1:
            Mistake_Found = True

    if "'" not in string and '"' not in string:
        comments_start_one = string.find('#')
        comments_start_two = string.find('/*')
        if comments_start_one != -1 or comments_start_two != -1:
            if comments_start_one != -1 and comments_start_two != -1:
                end = min(comments_start_one, comments_start_two)
            if comments_start_one != -1 and comments_start_two == -1:
                end = comments_start_one
            if comments_start_one == -1 and comments_start_two != -1:
                end = comments_start_two
            if ";" in string[0:end]:
                Mistake_Found = True
        else:
            if ";" in string:
                Mistake_Found = True

    return Mistake_Found

# Function returns boolean value equal to True if at least two spaces required before inline comments
def message_4(string):
    Mistake_Found = False

    if ('#' in string or '/*' in string) and (string[0] != "#" and string[0] != "/*"):

        if "'" in string:
            index_first_one_quote = string.find("'", string.index("'") + 1)
            comments_start_one = string.find('#', index_first_one_quote + 1)
            comments_start_two = string.find('/*', index_first_one_quote + 1)
            if comments_start_one != -1 and comments_start_two != -1:
                end = min(comments_start_one, comments_start_two)
            if comments_start_one != -1 and comments_start_two == -1:
                end = comments_start_one
            if comments_start_one == -1 and comments_start_two != -1:
                end = comments_start_two
            if comments_start_one == -1 and comments_start_two == -1:
                return Mistake_Found

            if string[end - 1] == " ":
                if string[end - 2] != " ":
                    Mistake_Found = True
            else:
                Mistake_Found = True

        if '"' in string:
            index_first_two_quote = string.find('"', string.index('"') + 1)
            comments_start_one = string.find('#', index_first_two_quote + 1)
            comments_start_two = string.find('/*', index_first_two_quote + 1)
            if comments_start_one != -1 and comments_start_two != -1:
                end = min(comments_start_one, comments_start_two)
            if comments_start_one == -1 and comments_start_two == -1:
                end = -1
            if comments_start_one != -1 and comments_start_two == -1:
                end = comments_start_one
            if comments_start_one == -1 and comments_start_two != -1:
                end = comments_start_two

            if string[end - 1] == " ":
                if string[end - 2] != " ":
                    Mistake_Found = True
            else:
                Mistake_Found = True

        if "'" not in string and '"' not in string:
            comments_start_one = string.find('#')
            comments_start_two = string.find('/*')
            if comments_start_one != -1 and comments_start_two != -1:
                end = min(comments_start_one, comments_start_two)
            if comments_start_one == -1 and comments_start_two == -1:
                end = -1
            if comments_start_one != -1 and comments_start_two == -1:
                end = comments_start_one
            if comments_start_one == -1 and comments_start_two != -1:
                end = comments_start_two
            if string[end - 1] == " ":
                if string[end - 2] != " ":
                    Mistake_Found = True
            else:
                Mistake_Found = True

    return Mistake_Found

# Function returns boolean value equal to True if to_do found (in comments only and case-insensitive)
def message_5(string):
    Mistake_Found = False

    if '#' in string or '/*' in string:

        if "'" in string:
            index_first_one_quote = string.find("'", string.index("'") + 1)
            comments_start_one = string.find('#', index_first_one_quote + 1)
            comments_start_two = string.find('/*', index_first_one_quote + 1)
            if comments_start_one != -1 and comments_start_two != -1:
                end = min(comments_start_one, comments_start_two)
            if comments_start_one != -1 and comments_start_two == -1:
                end = comments_start_one
            if comments_start_one == -1 and comments_start_two != -1:
                end = comments_start_two
            if comments_start_one == -1 and comments_start_two == -1:
                return Mistake_Found

            if "todo" in string[end:-1].lower():
                Mistake_Found = True

        if '"' in string:
            index_first_two_quote = string.find('"', string.index('"') + 1)
            comments_start_one = string.find('#', index_first_two_quote + 1)
            comments_start_two = string.find('/*', index_first_two_quote + 1)
            if comments_start_one != -1 and comments_start_two != -1:
                end = min(comments_start_one, comments_start_two)
            if comments_start_one == -1 and comments_start_two == -1:
                end = -1
            if comments_start_one != -1 and comments_start_two == -1:
                end = comments_start_one
            if comments_start_one == -1 and comments_start_two != -1:
                end = comments_start_two

            if "todo" in string[end:-1].lower():
                Mistake_Found = True

        if "'" not in string and '"' not in string:
            comments_start_one = string.find('#')
            comments_start_two = string.find('/*')
            if comments_start_one != -1 and comments_start_two != -1:
                end = min(comments_start_one, comments_start_two)
            if comments_start_one == -1 and comments_start_two == -1:
                end = -1
            if comments_start_one != -1 and comments_start_two == -1:
                end = comments_start_one
            if comments_start_one == -1 and comments_start_two != -1:
                end = comments_start_two

            if "todo" in string[end:-1].lower():
                Mistake_Found = True

    return Mistake_Found

# Function returns boolean value equal to True if more than two blank lines preceding a code line (applies to the first non-empty line).
def message_6(previous_line, second_previous_line, third_previous_line):
    Mistake_Found =False
    if previous_line == "\n" and second_previous_line == "\n" and third_previous_line == '\n':
        Mistake_Found = True
    return Mistake_Found

# Function returns boolean value equal to True if there is more than one space after 'class'
def message_class_7(string):
    Mistake_Found = False
    start_with_string = "class"
    check_0 = re.match(start_with_string,string)
    if check_0 is not None:
        class_template = "class[ ][^ ]"
        check = re.match(class_template,string)
        if check is None:
            Mistake_Found = True
    return Mistake_Found

# Function returns boolean value equal to True if there is more than one space after 'def'
def message_def_7(string):
    Mistake_Found = False
    start_with_string = "[ ]*def"
    check_0 = re.match(start_with_string, string)
    if check_0 is not None:
        def_template = "[ ]*def[ ][^ ]"
        check = re.match(def_template, string)
        if check is None:
            Mistake_Found = True
    return Mistake_Found
# Function returns boolean value equal to True if className not written in CamelCase
def message_8(string):
    Mistake_Found = False
    start_with_string = "class"
    check_0 = re.match(start_with_string, string)
    if check_0 is not None:
        start_with_upper = "class[ ]*([A-Z][a-z0-9]+)+"
        check_1 = re.match(start_with_upper,string)
        if check_1 is None :
            Mistake_Found = True
    return Mistake_Found

# Function returns boolean value equal to True if function_name not written in snake_case
def message_9(string):
    Mistake_Found = False
    start_with_string = "[ ]*def"
    check_0 = re.match(start_with_string, string)
    if check_0 is not None:
        start_with_upper = "[ ]*def[ ]*_*([a-z0-9]+[_]*)+_*"
        check_1 = re.match(start_with_upper, string)
        if check_1 is None:
            Mistake_Found = True
    return Mistake_Found

# Function returns function name or class name
def get_function_or_class_name(string):
    function_name = ''
    class_name = ''
    start_with_def="[ ]*def"
    start_with_class="[ ]*class"
    check_class = re.match(start_with_class,string)
    check_def = re.match(start_with_def,string)
    if check_def is not None:
        index_def = string.index('def')
        index_end = string.index('(')
        for i in range(index_def+3,index_end):
            if string[i] != ' ':
                function_name+=string[i]
        return function_name

    if check_class is not None:
        index_class = string.index('class')
        index_end = string.index(':')
        for i in range(index_class+5,index_end):
            if string[i] != ' ':
                class_name+=string[i]
        return class_name


#Function returns boolean value equal to True if the argument is a file
def check_file(file_or_directory):
    Check_File = False
    head = os.path.split(file_or_directory)[0]
    tail= os.path.split(file_or_directory)[1]
    if head == '':
        head = os.getcwd()
    if (os.path.isfile(head+os.sep+tail)):
         Check_File = True
    return Check_File

# Function returns boolean value equal to True if the argument is a directory
def check_directory(file_or_directory):
    Check_directory = False
    head = os.path.split(file_or_directory)[0]
    tail = os.path.split(file_or_directory)[1]
    if head == '':
        head = os.getcwd()
    if os.path.isdir(head+os.sep+tail):
         Check_directory = True

    return Check_directory

# Function return boolean value to True if the file is a python file
def check_python_file(file):
    Check_Extension = False
    if file.endswith(".py"):
        Check_Extension = True
    return Check_Extension

# Function prints output if a argument is a file
def analyse_single_file(path):
    with open(str(path), 'r') as file_input:
        # index parameter is index of line in file "file_input"
        index = 1
        lines_liste=[]
        for line in file_input:
            lines_liste.append(line)
            if (message_1(line)):
                print(message_output(1, index, path))

            if (message_2(line)):
                print(message_output(2, index, path))

            if (message_3(line)):
                print(message_output(3, index, path))

            if (message_4(line)):
                print(message_output(4, index, path))

            if (message_5(line)):
                print(message_output(5, index, path))

            if (len(lines_liste) >= 4) and (message_6(lines_liste[index-2], lines_liste[index-3], lines_liste[index-4])):
                print(message_output(6, index, path))

            if (message_class_7(line)):
                print(message_output(7, index, path,class_or_def='class'))

            if (message_def_7(line)):
                print(message_output(7, index, path, class_or_def='function'))

            if (message_8(line)):
                print(message_output(8, index, path, class_name=get_function_or_class_name(line)))

            if (message_9(line)):
                print(message_output(9, index, path, function_name=get_function_or_class_name(line)))


            index += 1

# Function prints output if a argument is a directory
def analyse_directory(path):
    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            # append the file name to the list
            if check_python_file(file):
                filelist.append(os.path.join(root, file))


    filelist = sorted(filelist)
    for file in filelist:
        analyse_single_file(file)



# Function returns message depending of innput "message_id"
def message_output(message_id, index, path, class_or_def = None ,class_name = None, function_name = None):
    if message_id == 1:
        message = f"{path}: Line {index}: S001 Too long"
    if message_id == 2:
        message = f"{path}: Line {index}: S002 Indentation is not a multiple of four"
    if message_id == 3:
        message = f"{path}: Line {index}: S003 Unnecessary semicolon"
    if message_id == 4:
        message = f"{path}: Line {index}: S004 At least two spaces required before inline comments"
    if message_id == 5:
        message = f"{path}: Line {index}: S005 TODO found"
    if message_id == 6:
        message = f"{path}: Line {index}: S006 More than two blank lines used before this line"
    if message_id == 7:
        message = f"{path}: Line {index}: S007 Too many spaces after {class_or_def}"
    if message_id == 8:
        message = f"{path}: Line {index}: S008 Class name '{class_name}' should use CamelCase"
    if message_id == 9:
        message = f"{path}: Line {index}: S009 Function name '{function_name}' should use snake_case"
    return message


# Main function
def main():
    args = sys.argv

    file_or_directory = args[1]

    if check_file(file_or_directory) == True and check_python_file(file_or_directory):
        analyse_single_file(file_or_directory)

    if check_directory(file_or_directory) == True:
        analyse_directory(file_or_directory)


# Call main function
if __name__ == "__main__":
    main()
