infile = input("Enter name of GTF file: ")

f = open(infile, 'r')

outfile = input("Enter name of output file: ")
out = open(outfile, 'a')

n = 0 # count number of lines
for i in f.readlines():
    linetype = i.split()[2]
    
    if linetype == "CDS":
        print(i, file=out)
        n+=1

f.close()
out.close()

print(f"{n} lines written.")
