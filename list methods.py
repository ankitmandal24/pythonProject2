# list methods

basket = [1,2,3,4,5]
# adding in list
basket.append(500)
basket.insert(3,100)
basket.extend([100 , 101])
#print(basket)

#removing

basket.pop(4) #remove from index
basket.remove(5) # remove particular number
basket.clear() # remove whole part
#print(basket)

# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list

# 2. Remove "Blueberries" from the list.

# 3. Put "Kiwi" at the end of the list.

# 4. Add "Apples" at the beginning of the list

# 5. Count how many apples in the basket

# 6. empty the basket
#1 basket.pop(0)
#2 basket.remove("Blueberries")
#3 basket.append("kiwi")
#basket.insert(0,"Apples")
#print(basket.count("Apples"))
#print(basket)


#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']
friends.extend(new_friend)
#print(sorted(friends))

# list unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(*other)
print(d)