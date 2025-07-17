#Dictionairies

band={
    'vocals':'Plant',
    'guitar':'Page'
}

band2=dict(vocals="Plant",guitar="Page")

print(band)
print(band2)

print(type(band))
print(len(band))

#access items

print(band['vocals'])
print(band.get('guitar'))

#list all keys

print(band.keys())

print(band.values())

print(band.items())

print("guitar" in band)
print("triangle" in band)

print("")
#change values
band["vocals"]="Coverdale"
band.update({"bass":"JPJ"})

print(band)

#remove items
print(band.pop("bass"))
print(band)

band["drums"]="Bonham"
print (band)

print(band.popitem()) #tuple
print(band)

#delete and clear

band["drums"]="Bonham"
del band["drums"]
print(band)

band2.clear
print (band2)

del band2

#copy dictionairies

# band2=band #creates a reference, refers to the same place in memory

# print("Bad Copy")
# print(band2)
# print(band)

# band2["drums"]="Dave"
# print(band)

band2=band.copy()
band2["drums"]="Dave"

print(band)
print(band2)

#copy using dictionary constructor function

band3=dict(band)
print(band3)

#nested dictionairies

member1={
    "name":"Plant",
    "instrument":"vocals"
}
member2={
    "name":"Page",
    "instrument":"guitar"
}
band4={
    "member1":member1,
    "member2":member2
}
print(band4)
print(band4["member1"]["name"])

#sets, Sort and de-dup
nums={1,2,3,4}
nums2=set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no dups allow

nums={1,2,2,4}
print(nums)

#True

nums={1, True, 2, False, 4,3,0}
print(nums)
#check if value in a set
print(2 in nums)

#add a new value ot a et

nums.add(8)
print(nums)

#add values from another set
morenums={5,6,7,8}
nums.update(morenums)
print(nums)

#merge sets
one={1,2,3}
two={4,5,6}
three={7,8,9}
mynewset=one.union(two)
print(mynewset)
myotherset=one.union(two.union(three))
print(myotherset)

#Keep only dups
one={1,2,3}
two={2,3,6}

one.intersection_update(two)
print(one)

#keep everthing except dups
one={1,2,3}
two={2,3,6}

one.symmetric_difference_update(two)
print(one)