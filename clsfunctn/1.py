class Time(object):
	""" represent time of day """


def print_time(t):
	print '%.2d:%.2d:%.2d' %(t.hour,t.minute,t.second)

time=Time()
time.hour=10
time.minute=29
time.second=33

print_time(time)
