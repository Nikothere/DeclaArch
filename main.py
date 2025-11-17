import os

os.system("lsblk")

rootpart = input("choose the root partion: (dev/your_root_partition)")
bootpart = input("choose the boot partion: (dev/your_boot_partition)")

swapquest = input("Do you want to use swap partition? (yes/no): ")
 
if swapquest == "yes":
   swappart = input("chose the swap partition: ")
   os.system(f"mkswap {swappart}")
   os.system(f"swapon {swappart}")

bootformreq = input("Do you want to format the boot partition? (bootloader of other operating systems will be destroyed) (yes/no)")

if bootformreq == "yes":
   os.system(f"mkfs.fat -F32 -n EFI {bootpart}")

os.system(f"mkfs.ext4 {rootpart}")








