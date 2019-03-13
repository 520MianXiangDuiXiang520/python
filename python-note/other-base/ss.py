tabby_cat="\t I'm tabbed in."
persian_cat="I'm split\nnon a line."
backslash_cat="I'm \\ a \\ cat."
fat_cat="""
I'll do a list:
\t*Cat Food
\t*Fishes
\t*Catnip\n\t*Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print("How old are you?",end='')
age=input();
print("How tall are you?",end="")
height=input()
print("How much do you weight?",end="")
weight=input()
print(f"So,you're {age} old,{height} tall and {weight} heavy.")
