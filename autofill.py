import pyautogui
import time
#screenWidth, screenHeight = pyautogui.size()
#pyautogui.position()
time.sleep(5)  #

for i in range(38):
	# fill amount page
	pyautogui.click(x=895, y=580, button='left')
	pyautogui.typewrite('15\n') 

	pyautogui.click(x=723,y=656,button='left')

	time.sleep(4) 
	# check out page 
	pyautogui.click(x=1185,y=301,button='left')
	time.sleep(4) 
	#place order 
	pyautogui.click(x=1149,y=292,button='left')

	#back to the oder 
	time.sleep(4) 
	pyautogui.click(x=1217,y=135,button='left')


	#back to the item 
	time.sleep(4)
	pyautogui.click(x=512,y=541,button='left')
	time.sleep(4)
#pyautogui.typewrite('15')
