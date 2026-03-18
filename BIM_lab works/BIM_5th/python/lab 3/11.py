name="shikshya"
age=21
height=5.7
print("=== String Formatting Examples ===\n")
print("1. Using % formatting:")
print("Name:%s,Age:%d,Height:%.1f ft"%(name,age,height))

print("\n2. Using str.format():")
print("Name:{},Age: {}, Height:{:.1f} ft,".format(name,age,height))

print("\n3. Using f-strings:")
print(f"Name: {name},Age:{age},Height:{height:.1f} ft")
