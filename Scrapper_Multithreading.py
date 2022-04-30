import cv2
import os
import numpy as np
import urllib.request
import time
import threading
import math
import matplotlib.pyplot as plt

time1=[]
def getPokemon(start, end):
    print("Started worker for range :", start, "to", end)
    for i in range(start, end):
        try:
            url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + '{:03d}'.format(i) + '.png'
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            binary_str = response.read()
            byte_array = bytearray(binary_str)
            numpy_array = np.asarray(byte_array, dtype="uint8")
            image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
            cv2.imwrite("images_multithreading/" + '{:04d}'.format(i) + '.png', image)
            print("Saved " + '{:04d}'.format(i) + '.png')
            time1.append(time.time() - start_time)
        except Exception as e:
            print(str(e))

print("Done")
start_time = time.time()
thread_count = 8
image_count = 40
thread_list = []


for i in range(thread_count):
    start = math.floor(i * image_count / thread_count) + 1
    end = math.floor((i + 1) * image_count / thread_count) + 1
    thread_list.append(threading.Thread(target=getPokemon, args=(start, end)))
    

for thread in thread_list:
    thread.start()

for thread in thread_list:
    
    thread.join()


end_time = time.time()
print("Done")
print("Time taken : " + str(end_time - start_time) + "sec")


x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
  

plt.plot(x, time1)
  

plt.xlabel('no. of images')
plt.ylabel('time')
  

plt.title('graph of time vs no.of images downloaded')
  
plt.show()
os.system('pause')