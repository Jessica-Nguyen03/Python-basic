
#read file
f = open("test.txt","r")
data = f.read()
f.close()
print(data)


# write file
f = open("test.txt","w")
f.write("DHKHMT17A")
f.close()


# # Read File
# with open (" test .txt ", "r") as f :
#     data = f . read ()
#     print ( data )

# # Write File
# with open (" test .txt ", "w") as f :
#     f . write ("I Love AI Vietnam ")