searchfile = open("test.txt", "r")
for line in searchfile:
  if "test" in line: print(line)
searchfile.close()
