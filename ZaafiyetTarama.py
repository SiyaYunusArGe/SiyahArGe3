#!/usr/bin/env python
import os
os.system ("apt.get install figlet")
os.system ("clear")
print("""
  ______                   __   _                  _     _______                                            
 |___  /                  / _| (_)                | |   |__   __|                                           
    / /    __ _    __ _  | |_   _   _   _    ___  | |_     | |      __ _   _ __    __ _   _ __ ___     __ _ 
   / /    / _` |  / _` | |  _| | | | | | |  / _ \ | __|    | |     / _` | | '__|  / _` | | '_ ` _ \   / _` |
  / /__  | (_| | | (_| | | |   | | | |_| | |  __/ | |_     | |    | (_| | | |    | (_| | | | | | | | | (_| |
 /_____|  \__,_|  \__,_| |_|   |_|  \__, |  \___|  \__|    |_|     \__,_| |_|     \__,_| |_| |_| |_|  \__,_|
                                     __/ |                                                                  
                                    |___/                                                                   

""")
print("""

Zaafiyet Analiz Aracina Hosgeldin created by.SiyahYunus

""")

hedefip = raw_input("Hedef IP Giriniz: ")
os.system("nikto -h " + hedefip)
