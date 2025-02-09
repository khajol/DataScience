fread=open('C:/Users/khajo/Desktop/DataScience/Python/7_file_operation/files/read_write.txt','r')
fwrite=open('C:/Users/khajo/Desktop/DataScience/Python/7_file_operation/files/read_write_1.txt','w')

for i in fread:
    fwrite.write(i)