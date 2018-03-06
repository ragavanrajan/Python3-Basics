student_names = ["Mike", "Bisset", "Clark","Ragavan"]

# imagine if you have 1000 list in array it will not execute once the match is found
for name in student_names:
    if name == "Bisset":
        print("Found him! " + name)
        print("End of Break program")
        break
    print("currently testing " + name)

# Continue Example
# Continue will work if match is found and then execute the rest

student_namesnew = ["Mike", "Bisset", "Clark","Ragavan","Milan","Graeme"]

# It will iterate for every single element except for Clark. Bcoz using continue keyword to skip executing the rest of the code
# to continue iteration directly
for namenew in student_namesnew:
    if namenew == "Clark":
        continue
        print("Found him Continue! " + namenew)

    print("currently testing-using continue " + namenew)