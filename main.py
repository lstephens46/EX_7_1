# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for ln in fh:
    print(ln.rstrip().upper())