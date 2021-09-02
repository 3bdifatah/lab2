
list_numbers = [0, 3, 4, 0, 22, 1, 32, 14, 0, 19]

non_zero = [n for n in list_numbers if n>0]
print(non_zero)


classes = ["ITEC 2900", "ITEC 1200", "MATH and ITEC 1200", "ITEC 1540", "BTEC 1100", "ATEC 1000"]
itec = [it for it in classes if it.startswith('ITEC')]
print(itec)
#another way
itec2 = [it.upper() for it in classes if "ITEC" in it]
print(itec2)


doubled_non_zero = [n*2 for n in list_numbers if n!=0]
print(doubled_non_zero)