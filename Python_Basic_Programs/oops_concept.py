class laptop:
     price = ""
     processor = ""
     ram = ""

HP = laptop()
LENOVO = laptop()
DELL = laptop()

HP.price="RS.45,000"
LENOVO.price="RS.57,000"
DELL.price="RS.72,000"

HP.processor="Intel Core i3/i5/i7 "
LENOVO.processor="Intel Core i5 7th Gen"
DELL.processor="Intel® Core™ Ultra Processors"

HP.ram="16gb"
LENOVO.ram="16gb"
DELL.ram="18gb"

print(HP.price)
print(HP.processor)
print(HP.ram)



