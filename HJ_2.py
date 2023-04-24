
# Вход: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBB

# Выход: A4B3C2XYZD4E3F3A6B26

strok = str(input("Введите строку: "))

bufer = list(strok[0])
result = []
index = 1    
inspec = strok.isalpha()

if inspec == False:
    print("Введены неверные значения!")
else:
    for i in range (1, len(strok)):
    
    
        if strok[i-1] != strok[i] or i == len(strok)-1:
            result = result + [bufer[0]]
        
            if index > 1:
                box = str(index)
                result = result + [box]
                index = 1
            bufer = strok[i]
        
        elif strok[i-1] == strok[i]:
            bufer = [strok[i]]
            index += 1
    

    print(f"Вывод {''.join(result)}")