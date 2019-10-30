import sys
import ftplib
import argparse
import lib 
import ntpath

#Upload directory on the server
u_path = "/upload/"
#download directory on the server
d_path = "/"

def main(args):
	
	#handle the argument passed on the command line
	parser = argparse.ArgumentParser(description='FTP client for download and upload')

	parser.add_argument('-f', '--name',  type=str, nargs='+', help="file_name")
	parser.add_argument('-s', '--server',default="speedtest.tele2.net", type=str,help='host_server')
        parser.add_argument('-o', '--output',default='Downloads', type=str, help="destination")
	parser.add_argument('-d', '--down', action='store_true', help="download mode")
	parser.add_argument('-u', '--upload', action='store_true', help="upload mode")
        parser.add_argument('-l', '--listing', action='store_true', help="listing files")
        

	args = parser.parse_args()
	# create an ftp object
	ftp = ftplib.FTP(args.server)
	#login with anonymous mode
	ftp.login()
	#get files in the download directory
	files = ftp.nlst(d_path)
        #printing files in the download directory
        if args.listing:
		print "Listing Files:"
                for f in files:
			print f
	#download mode        
	if args.down:
		files = ftp.nlst(d_path)
		for f in args.name:
			#check if the file exist in the download directory
			if d_path+f in files :
				lib.download(f, ftp,args.output,d_path)
			else:
				print f+" doesn't exist "
				print "use python -B ftp_client -l to list files"
	#upload mode
        if args.upload:
		for f in args.name:
                        #extract the file name from the path, 
			#in anonymous mode the server prevent creating directories in upload just files 
			f= ntpath.basename(f)  
			lib.upload(f, ftp,u_path)
	#close the ftp connection object       
	ftp.quit()

if __name__ == '__main__':
    from sys import argv

    try:
        main(argv)
    #Control-C to exist
    except KeyboardInterrupt:
        pass
    sys.exit()