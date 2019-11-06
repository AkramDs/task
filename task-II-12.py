text = input()

for i in text:
    if i == 'f':
        print(text.find('f'), text.rfind('f'))
        break
        
