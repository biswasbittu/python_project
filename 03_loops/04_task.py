# Task -7
# total=0
# for i in range(2,11,2):
#     total =i+total;
# print(total)
    
    # Task -8
# fact=1  
# for i in range(1,6):
#     fact=fact*i
# print(fact)

# Task -9

# div=3;

# for i in range(1,101):
#     if i%3==0:
#         print(i)
    
    
# task-10
name="python";

# for ch in name[::-1]:
#     print(ch)
# Task -11 (vowel count)
# word=input("Enter Word: ");

# count =0;
# for ch in word:
#     if ch in 'aeiou':
#         count=count+1;
# print(count)

# Task -12 (print all list)

fruits =["Apple", "Banana", "Orange", "Mango"];

# for item in fruits:
#     print(item)
#     print(item.upper())

# count =0;
# for item in fruits:
#     count+=1;
# print(count)

# Task -13(pattern print)

# for i in range (1,11):
#     print("*"*i)

# for i in range(11,0,-1):
    # print("*"*i)
    
    # Task-13(Multiplication table)
# 
# Task -14
# nums=[3,7,2,9,5];
# largest= nums[0]

# for n in nums:
#     if n > largest:
#         largest=n;
# print(largest)

# Task-15

# nums = [1,2,2,3,4,4,7,9,7]
# seen =[]

# for n in nums:
#     if nums.count(n) > 1 and n not in seen:
#         print(n)
#         seen.append(n)
# Task-16(Password- digit count);
pwd='abc1235';
count=0;

for ch in pwd:
    if ch.isdigit():
        count+=1
        print(count)

    
    