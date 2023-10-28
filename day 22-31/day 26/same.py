
def read_from_file(filename):
    with open (filename) as file:
        num=[int(line.strip()) for line in file]
    return num

num1=read_from_file(filename="/home/salsabeel/Desktop/Python-udemy/day 22-31/day 26/file1.txt")
num2=read_from_file(filename="/home/salsabeel/Desktop/Python-udemy/day 22-31/day 26/file2.txt")

new_list=[n for n in num1 if n in num2]
not_list=[n for n in num1 if n not in num2]
print(new_list)
print(not_list)