s_kdm = "hello world"
print("First char:", s_kdm[0])
for c_kdm in s_kdm:
 print(c_kdm, end=" ")
 s2_kdm = s_kdm + "!!!"
print("\nConcatenated:", s2_kdm)
print("Contains 'world'?", "world" in s_kdm)