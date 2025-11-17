import os

os.system("lsblk")

rootpart = input("choose the root partion: ")
bootpart = input("choose the boot partion: ")
swapquest = input("Do you want to use swap partition? (yes\no): ")
 
if swapquest == "yes":
   swappart = input("chose the swap partition: ")
   os.system(f"mkswap {swappart}")
   os.system(f"swapon {swappart}")




