

def logger(operation, duration, name, size, time):
	log = open("Log/logs.txt", "a+")
        log.write(operation+"\n")
	log.write("Filename: "+ name +"\n")
	log.write("Size: "+ str(size)+" Bytes\n")
        log.write("Date: "+ str(time)+"\n")
	log.write("Duration: "+ str(duration)+" Second\n")
        log.write("\n")