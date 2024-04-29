import numpy as np

#from numpy import random
my_list=[56,83,92,75]

print(type(my_list))
print(my_list)


print("-"*50)

my_arr = np.array(my_list)
print(type(my_arr))
print(my_arr)

print("-"*50)

my_arr3 = np.zeros((5,3))
print(my_arr3)
print(my_arr3.shape)

print("-"*50)

my_arr4 = np.ones((5,3))
print(my_arr4)
print(my_arr4.shape)

print("-"*50)

my_arr5 = np.random.randint(1,100,(10))
print(f"array={my_arr5}")
print(f"ortalama={np.mean(my_arr5)}")
print(f"toplam={np.sum(my_arr5)}")
print(f"çarpı 2={my_arr5*2}")

print("-"*50)

my_arr6 = np.random.randint(1,50,(5))
my_arr7 = np.random.randint(1,50,(5))
print(my_arr6)
print(my_arr7)
print(f"toplam={my_arr6 + my_arr7}")
