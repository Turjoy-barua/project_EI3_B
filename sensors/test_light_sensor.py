


from grove.adc import ADC
import time 

adc = ADC(address=0x08)

while True:
	light = adc.read(0)
	print('light levels: ', light)
	time.sleep(1)
