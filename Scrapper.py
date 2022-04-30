import cv2
import os
import numpy as np
import urllib.request
import time
import matplotlib.pyplot as plt


start_time = time.time()
time1=[]

for i in range(1, 41):
    try:
        req = urllib.request.Request(
            'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + '{:03d}'.format(i) + '.png')
        response = urllib.request.urlopen(req)
        rr = response.read()
        ba = bytearray(rr)
        time1.append(time.time() - start_time)
        image = np.asarray(ba, dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
        cv2.imwrite("images/" + '{:04d}'.format(i) + ".png", image)
        print("Saved " + '{:04d}'.format(i) + ".png")
        
        
    except Exception as e:
        print("Error Occured for Pokemon " + '{:04d}'.format(i))
        print(str(e))
        
end_time = time.time()
print("Done")
print("Time Taken = ", end_time - start_time, "sec")


  

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
  

plt.plot(x, time1)
  

plt.xlabel('x - axis')
plt.ylabel('y - axis')
  
plt.title('My first graph!')
  
plt.show()

os.system('pause')