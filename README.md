# Corn_Bread_Mafia_PythonMod5


Wrapper.sh:
  Using getopts to take the following input parameters and pass inputs to 
    the necessary files for query and process:

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

  Provide help promt if any conditions are not meet for entering parameters to
    run the file.


    ############################
compileData.py:
    Quiries the database with a given date range for information retrieval and
        compiles all recored into a fixed length format.


    ###########################
DBAccess.py:
    Database acess script. Contains functions for opening a connection
        to a database and reading information from it.
        USAGE: python3 DBAcess.py <dbname>


    ###########################
ftpaccess.py:
    Using the ftp library, and passing in two arguments from the wrapper file.
    If a user enters a password and username the ftp or without the File
    Transfer creates and uploads the created queryed file to the specified 
    ip address.


    ###########################
create_report.py:
    Taking in three arguments recs, begData, endDate as a list and quieries the
    selected search date (from / to) after converting the string date to a 
    usable format to quiery the database.


    ###########################
DIR:email_templates:
    BadParam.txt:
        calls a bad parameter for email verification using input postion
            (from/to).

    NoTrans.txt:
        called when the search range in not a within a valid search range
            (from/to).

    Success.txt:
        Displays a success message when transaction is successful showing
            (from/to).


    ###########################
hw8SQLite.db:
    File used for the database query.


    ###########################
Sendemail.py:
    Using the smtplib for sending mail and mail module mime.text.
    Sends email using plain text as the email body and takes as args:
        dest  = destination
        textfile = see email_templates above.
        sustr = message substring
        begDate = is added by template and shown the date entered
        endDate = is added by template ans shown the end date entered


##################### end of READFILE ########################### #########
