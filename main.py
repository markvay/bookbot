def count_words():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    i = 0
    for word in words:
         i+=1   
    
    return i
    
def char_count():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    lower_case_string = file_contents.lower()
    chardict = {}
    for char in lower_case_string:
        if char in chardict:
            chardict[char]+=1
        else:
            chardict.update({char:1})
    return chardict

def dic_to_list(original_dic):
    new_list = list(original_dic.items())
    #print(new_list)    
    return new_list

def sort_list(unsurted_list):
    new_list3 = []
    #print(unsurted_list)
    new_list3 = sorted(unsurted_list,key=lambda tup:tup[1],reverse=True)
    #print(new_list3)
    return new_list3  

def remove_nonalph(dirty_list):
    for char in dirty_list:
        if (char[0].isalpha()==False):
            dirty_list.remove(char)
    for char in dirty_list:
        if (char[0].isalpha()==False):
            dirty_list.remove(char)
    for char in dirty_list:
        if (char[0].isalpha()==False):
            dirty_list.remove(char)
    for char in dirty_list:
        if (char[0].isalpha()==False):
            dirty_list.remove(char)
    for char in dirty_list:
        if (char[0].isalpha()==False):
            dirty_list.remove(char)
    for char in dirty_list:
        if (char[0].isalpha()==False):
            dirty_list.remove(char)
    for char in dirty_list:
        if (char[0].isalpha()==False):
            dirty_list.remove(char)
    for char in dirty_list:
        if (char[0].isalpha()==False):
            dirty_list.remove(char)
            
    #print(dirty_list)
    return dirty_list

new_dic = char_count()    
new_list2 = dic_to_list(new_dic)
new_list3 = sort_list(new_list2)
CleanSorted_list = remove_nonalph(new_list3)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{count_words()} words found in the document")
print(" ")
for item in CleanSorted_list:
    print(f"The '{item[0]}' character was found {item[1]} times")
print("--- End report ---")






