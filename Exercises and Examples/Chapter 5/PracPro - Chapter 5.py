# CHAPTER 5 Exercises

# exercise number 5

if x == abs(x):
    result = True
else:
    result = False


# exercise number 6

def different(a, b):
    if a != b:
        return False
    else:
        return True


# exercise number 7

# 7a
if population < 10000000:
    print(population)

# 7b
if (population > 10000000) and (population < 35000000):
    print(population)


# exercise number 10
# original

ph = float(input("Enter the ph level: "))
if ph < 7.0:
    print("It's acidic!")
elif ph < 4.0:
    print("It's a strong acid!")

# With the original statement you will never see "strong acid" since
#   it never reaches that

# question asks how to change it to see both messages

#   if you want both
ph = float(input("Enter the ph level: "))
if ph < 7.0:
    print("It's acidic!")
if ph < 4.0:
    print("It's a strong acid!")


#   if you want one
ph = float(input("Enter the ph level: "))
if ph < 4.0:
    print("It's a strong acid!")
elif ph < 7.0:
    print("It's acidic!")







    
