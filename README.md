# Corn_Bread_Mafia_PythonMod5


#############################################

TODO LIST

1. Output all fixed length strings into one file named 'company\_trans\_BegDate\_EndDate.dat' where BegDate and EndDate are what were initially entered in the command line.

2. Use the sendemail.py script to send an email to the specified email address. We need to create template text files for storing our email body text in. 

3. Make sure all python scripts and the README.md are adequately documented. 

4. The wrapper.sh file should not have any coding in it. All the coding should be done in 'create\_report.py'. Wrapper.sh should only take command line inputs then it should defer all args to 'create\_report.py'.

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
