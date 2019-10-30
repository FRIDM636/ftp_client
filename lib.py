import ftplib
import sys
import datetime
import time
import log
import os
	
def download(file_name, ftp, output, download_path):
	TempFile = open(output+'/'+file_name, "wb") 
	ftp.cwd(download_path)
	start = time.time()
	ftp.retrbinary('RETR '+ file_name, TempFile.write)
	end = time.time()
	TempFile.close()
        log.logger("*****Download operation*****", end-start,file_name, ftp.size(file_name), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	print file_name+" is downloaded!"

def upload(file_name, ftp, upload_path):
	ftp.cwd(upload_path)
	TempFile = open(file_name,"rb")
        start = time.time()
	ftp.storbinary("STOR "+file_name,TempFile)
        end = time.time()
	log.logger("*****Upload operation*****", end-start,file_name, os.stat(file_name).st_size, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	TempFile.close()
	print file_name + " is uploaded!"

if __name__ == "__main__":
	download(sys.argv[1])
        
