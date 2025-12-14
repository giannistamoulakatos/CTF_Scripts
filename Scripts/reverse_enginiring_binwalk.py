import os 
import subprocess as sb

image_in = input("give the image file = ")

with open("image_results.txt", "w", encoding="utf-8") as f:
    sb.run(["binwalk", "-E", "-W", image_in],stdout=f, stderr = sb.STDOUT, text=True)
    
with open("image_sign.txt", "w", encoding="utf-8") as f:
    sb.run(["binwalk", "-D",  image_in],stdout=f, stderr = sb.STDOUT, text=True)
