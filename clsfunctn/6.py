class Time(object):
	""" time """

def time_to_int(t):
	minutes = t.hour*60 + t.minute
	seconds = minutes*60 + t.second
	return seconds

def int_to_time(seconds):
	t=Time()
	t.minute,t.second = divmod(seconds,60)
	t.hour,t.minute = divmod(t.minute,60)
	return t

def mul_time(t,num):
	seconds=time_to_int(t)
	return int_to_time(seconds*num)

def avg_pace(t,dist):
	return mul_time(t,1.0/dist)

time=Time()
time.hour=10
time.minute=55
time.second=0

num=2

mtime=mul_time(time,num)
print '\n\n%.2d:%.2d:%.2d\n\n' %(mtime.hour,mtime.minute,mtime.second)

avg=avg_pace(mtime,10)
print '\n\n%.2d:%.2d:%.2d\n\n' %(avg.hour,avg.minute,avg.second)
