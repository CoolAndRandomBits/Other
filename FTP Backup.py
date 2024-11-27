import time
import tarfile
import os
from ftplib import FTP



def CreateArchive():
	# This function will create an archive file with the name composing
	# of the date and time

	strDateTime = time.strftime("%Y%m%d_%H%M%S")
	strItemToArchive = "backup6"

	strArchiveFilename = "namePrefix_" + strDateTime + ".tar.gz"
	
	objTarFile = tarfile.open(strArchiveFilename, 'w:gz')
	objTarFile.add(strItemToArchive)
	objTarFile.close()

	return strArchiveFilename



def TransferFile(strFileToTransfer):
	# This function will transfer the archive file to the FTP server

	strFTPhost="ftpserver.local"
	strFTPuser="__________"
	strFTPpass="__________"
	strFTPdir="/Folder"

	objFTP = FTP(strFTPhost)
	objFTP.login(strFTPuser,strFTPpass)
	objFTP.cwd(strFTPdir)
	objFTP.storbinary("STOR " + strFileToTransfer, open(strFileToTransfer, "rb"), 1024)

	objFTP.close()



def DeleteArchive(strFileToDelete):
	# This function will delete the archive from the local server

	os.remove(strFileToDelete)
	

	

# Execute the functions

strArchiveFilename = CreateArchive()
TransferFile(strArchiveFilename)
DeleteArchive(strArchiveFilename)