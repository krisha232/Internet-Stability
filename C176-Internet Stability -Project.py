import speedtest
import matplotlib.pyplot as plt
import time

download_speed=[]
upload_speed=[]

for i in range(5):
    st=speedtest.Speedtest()
    dload_speed=round(st.download()/1000000,2)   
    download_speed.append(dload_speed)
    
    uload_speed=round(st.download()/1000000,2)   
    upload_speed.append(uload_speed)
    time.sleep(60)
    print(download_speed)
    print(upload_speed)
    
x=[1,2,3,4,5]

plt.plot(x,download_speed,label="Download Speed ")
plt.plot(x,upload_speed,label="Upload Speed ")
plt.title("Internet Stability")
plt.legend()
plt.show()