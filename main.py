
def main(book_path):
    txt= file_opening(book_path)
    words= splitter(txt)
    print("The book contains "+ str(len(words)))
    characters= word_splitter(words)
    characters_nums= character_counting(characters)
    print("\n Occurences of different letters \n")
    print(characters_nums)
    


 #opening and reading the files text   
def file_opening(file):
    with open(file) as f:
        file_contents= f.read().replace("\n","")
    return file_contents 
   
#to split the entire text into a list of words
def splitter(txt):
    words_list = txt.split()
    return words_list  


# splits words into characters
def word_splitter(str_list):
    x= len(str_list)
    y=0
    characters=[]
    while y < x :
        string= str_list[y]
        lowered_string= string.lower()
        for letter in lowered_string:
            characters.append(letter) 
        y+=1
    return characters

# counting the characters in the text
# by using a dict with a string -> integer pair
def character_counting(characters):
    character_dict= {'a':0}
    for letter in characters:
        if letter not in character_dict and letter.isalpha():
            temporary_dict= {letter:1}
            character_dict.update(temporary_dict)
        elif letter in character_dict and letter.isalpha():
            character_dict[letter]+=1
        else:
            continue
    dict_keys= list(character_dict.keys())
    dict_keys.sort()
    sorted_dict= {i:character_dict[i] for i in dict_keys}
    return sorted_dict

        
main("books/frankenstein.txt")



