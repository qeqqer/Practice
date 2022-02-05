#2525
h, m = map(int,input().split()) #A=hour B=min
cook_min = int(input()) #need min

time = m+cook_min

if (time<=59):
	print(h,time)
elif(time>59):
	
	plus_h = int(time/60)
	final_h = h+plus_h

	final_h=plus_h+h
	if(final_h>=24):
		final_h -= 24
	
	
	plus_m = time%60
	final_m = plus_m
	if(final_m==60):
		final_h+=1
		final_m==0


	print(final_h,final_m)

