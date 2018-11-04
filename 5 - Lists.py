#lists begins and ends with []
#comma delimited items

animals = ['cat', 'rat', 'bat', 'elephant']

list_list = [['car', 'cat', 'bat'], [12, 23, 34, 56, 87]]

#last item in the list
last_item = animals[-1]

sentence = 'The ' + animals[-1] + ' is afraid of ' + animals[1]

#list concatenation with + operator
[2, 34, 12, 1] + [12, 34, 5, 222, 59]

# list function returns list of whatever you pass. 
# in and not in operator for searching in list. 

print('hel' in ['hello', 'hel','hell', 'helloworld'])
words = ['some', 'words', 'here', 'what', 'not']

# print(words.index('some')) =? index method. returns index

# .append method append shit like
words.append("somevalue")
words.insert(1, "insert this value at <-that index")
words.remove("not")

# remove method uses `value` to delete first occurance found
# you can use `del` keyword to delete using index
 
#  sort the list using sort()
words.sort()
# it would start sorting with what in mind/logic?
# alphabetical order from [o] index
# what if alphabet is capital A rather than a.
# capital A would come first. Z, z, A, b => A and Z come first.
# reverse_sort please?
words.sort(reverse=True)

# NOTE : can't sort mixed data-type list
# Just sort normally .... ASCII-belitcal

words.sort(key=str.lower)

friends = ["manual", 'david', 'ashley', 'selena', 'john']
print(friends)