import os

os.system("lsblk")

rootpart = input("choose the root partion: (e.g /dev/your_root_partition)")
bootpart = input("choose the boot partion: (e.g /dev/your_boot_partition)")

swapquest = input("Do you want to use swap partition? (yes/no): ")
 
if swapquest.lower() == "yes":
   swappart = input("chose the swap partition: ")
   os.system(f"mkswap {swappart}")
   os.system(f"swapon {swappart}")

bootformreq = input("Do you want to format the boot partition? (bootloader of other operating systems will be destroyed) (yes/no)")

if bootformreq.lower() == "yes":
   os.system(f"mkfs.fat -F32 {bootpart}")

print("formating the root partion to ext4...")
os.system(f"mkfs.ext4 {rootpart}")


os.system(f"mount {rootpart} /mnt")
os.system(f"mount --mkdir {bootpart} /mnt/boot")

print("Congratulations! The disk setup is complete)")










