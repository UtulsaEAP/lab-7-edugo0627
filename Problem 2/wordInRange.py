'''
name: Emma Verdugo
lab:@2pm

'''

def wordInRange():
    #Type your code here
    file_name = input()
    lower_word = input()
    upper_word = input()
    
    with open(file_name) as file_object:
        lines = file_object.readlines()
        for line in lines:
            l =line.strip('\n')
            if (l >= lower_word) and (l <= upper_word):
                print(line.strip() + " - in range")
            else:
                print(line.strip() + " - not in range")
    return
if __name__ == '__main__':
    wordInRange()