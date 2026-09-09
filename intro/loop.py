# we can make list and lists can have multiple elements (data types)
# uncomment the examples to see the output
letters = ["a", "c", "g"]
# len is how many or the total count of elements in a list
length = len(letters)

# in range means you loop up to a specific number
for i in range(length):
    print(i)

# you can use the indexing to get a character from a string
# the count starts with 0 so the total count is off by 1
# and using a negative number will make you start from the
# end. 
# print(letters[-3])

txt = "Hello"

# you can also print each letter of the string by using
# a for loop
for lttr in range(len(txt)):
    print(lttr)

for letter in letters:
    print(letter)

# fruits is a list the contain strings
fruits = ["apple", "mango", "banana", "grape", "orange"]

# print a specifi fruit
print(fruits[3])

# print the fruits with some tweaking
for frt in fruits:
    if frt == "banana":
        # break
        print("Minion")
    else:
        print(frt)
    print("\n")
