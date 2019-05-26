import fondersi
import time

file_names_list = []
file_names_list.append(["images/1.jpg", "images/2.jpg"])
file_names_list.append(["images/11.jpg", "images/22.jpg"])
file_names_list.append(["images/111.png", "images/222.png"])

times = 0

for file_names in file_names_list:
    t1 = time.time()
    result = fondersi.merge(file_names)
    t2 = time.time()
    times += t2-t1
    
print("Average Time for "+str(len(file_names_list))+" Process: "+str(times/len(file_names)))
