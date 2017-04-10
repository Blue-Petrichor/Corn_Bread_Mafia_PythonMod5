# Corn_Bread_Mafia_PythonMod5


#############################################

TODO LIST

1. Finish compileData.py: Use the given function to get all data within the date range. It'll return all valid records as a list. Parse the list and create a fixed length representation of all the data. Be sure to combine all entries that have the same trans\_id. The guide for the fixed length string is at the bottom of the assignment pdf. 

2. Output all fixed length strings into one file named 'company\_trans\_BegDate\_EndDate.dat' where BegDate and EndDate are what were initially entered in the command line.

3. Create ftp python script. The ftp python script will upload a file to an ftp server. The uploaded file needs to be placed in '/srv/ftp/MockData'.

4. Use the sendemail.py script to send an email to the specified email address. We need to create template text files for storing our email body text in. 

5. Make sure all python scripts and the README.md are adequately documented. 

#############################################


Wrapper.sh:
  Using getopts to take the following input parameters:

  a. A required (-f <BegDate>). Begin Date with the following format: YYYYMMDD
  (needed for your date query)
  b. A required (-t <EndDate>). End Date with the following format: YYYYMMDD
  (needed for your date query)
  c. A required (-e <email>). For final notification. The customer’s email needed to let
  the user know the file has been transfer or for any problems associated with the
  module.
  d. A required –u <user> should be parsed if available. FTP Account/UserName in
  the “customer server”, which is hosted in your VM
  e. A required –p <passwd> should be parsed if available. FTP Account password
