nums = [1, 2, 3, 4]
print(nums)


nums.append(5)
print(nums)


x = nums.pop(0)
print(x)
print(nums)
for x in nums:
    
    x+=1
    print(x)
print("done")

salaries = {"sud": 20 ,
            "vij": 30}

print(salaries)
del salaries["vij"]
salaries["sid"] = 50
print(salaries)
for i,j in salaries.items():
   print(i, j)



l =[]

for i in range(0,30):
    l.append(i)
print(l)
