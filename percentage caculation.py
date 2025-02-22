#take marks as input from user from user
print("Enter marks obtained in 4 subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
urdu = int(input("urdu :"))
 
 #let's calculate the percentage of marks 
sum = math+english+science+urdu
print("sum of math,english,science and urdu")


perc = (sum/400)*100
print(end="Percentage mark =")
print(perc)