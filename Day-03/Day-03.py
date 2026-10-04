print("Anna nan kayali agthilla anna")

boy_name = input("boy name: " )
boy_age = int(input("boy age: "))
girl_name = input("girl name: ")
girl_age = int(input("girl age: "))

#using abs because sometimes because boy might me younger
age_diff = abs(boy_age - girl_age)

'''
this is 
a multiline
comment
'''

print(boy_name +" loves "+ girl_name + ". age difference is" + str(age_diff ))
print(f"{boy_name} loves {girl_name} . age difference is {age_diff}")


name=input("Enter your name")
age=input("Enter your age")
print("Hello "+name+" you are "+ age +" year old")

measure=input("enter the sentence: ")
print(measure.upper())
print(measure.lower())
print(measure.strip())
print(measure.replace("Anna","Aunty"))

text = input("Enter a string: ")
count = text.replace(" ","")
size = len(count)
print("Number of characters:",size)