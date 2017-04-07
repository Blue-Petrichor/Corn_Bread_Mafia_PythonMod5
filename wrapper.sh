
#!/bin/bash - 
#===============================================================================
#
#          FILE: wrapper.sh
# 
#         USAGE: ./wrapper.sh 
# 
#   DESCRIPTION: Wrapper to run all scripts
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Electron Group
#  ORGANIZATION: 
#       CREATED: 02/14/2017 20:21
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error


#####################  Help functions   ##################

# prompt for help
echo "For help on how to enter parameters type:"
echo "bash <filename.sh> --help"
echo


# Optional function if entered wrong
optional_function()
{
	echo 
	echo "If optional params are not entered use this example below."
	echo "[-y year] [-e email]"
	echo " required   required"
	exit 1
}
# Function if exit process is not correct or = 0
usage()
{
	echo "Try:"
	echo "[-y year] [-e email] [-u user] [-p passwd]"
	echo " required   required  optional  optional"
	optional_function
	echo " " 
	exit 1
}
# Function if email is not valid
email_usage()
{
	echo "ex: john_doe@something.com"
	echo " "
	exit 1
}

#check for the --help option for first param was entered
if [[ $1 == "--help" ]]
then
	usage
fi


##################### Getopts and  error handling  ##################
if [[ $1 != --help ]]
then
	while getopts ":y:e:u:p:" opt
	do
		case $opt in
			y) 
				year=$OPTARG
				#verify the file is correct and not empty in $2, $4
				# $2 must have 2015 or 2016 and $4 must have an email entered
				# verify these conditions are true and print messeage if correct.
				if [[ ! -z "$2" && ! -z "$4" ]]
				then
					if [[ $2 =~ 2015 || $2 =~ 2016 ]]
					then
						if [[ $? -eq 0 ]]
						then
							# Add the file to run here
							echo "$2 is an accepted year for process:"
						else
							usage
						fi
					fi
				fi
				;;
			e)  
				email=$OPTARG
				if [[ $4 =~ @ && $4 =~ .com ]]
				then
					# make varible to store email for use
					echo "$4 is an accepted email address:"
					else
						echo " "
						echo "$4 is partial or missing see help below:"
						email_usage
				fi
				;;
			u)  
				user=$OPTARG
				if [[ ! -z $6  ]]
				then 
					echo "Welcome $6!"
					echo ""
				else
					usage
				fi
				;;
			p) 
				pass=$OPTARG
				if [[ -z $8 ]]
				then 
					usage
				else
					#add default password
					echo "Passwordi will be set to default"
					echo ""
				fi
				;;
			*) #send to usage function for how to enter
				usage
				;;
		esac
	done
fi


#####################  Main shell execution  ##################
bash wget.sh $year

if [[ $? -eq 0 ]]
then
	echo "Expanding..."
	bash expand.sh $year
fi

if [[ $? -eq 0 ]]
then 
	echo ""
	echo "Filtering data..."
	bash filterData.sh temp
fi

if [[ $? -eq 0 ]]
then
	echo "Compressing filtered data..."
	bash compress.sh temp
fi

if [[ $? -eq 0 && -z $user && -z $pass ]]
then 
	echo ""
	echo "Uploading to ftp server..."
	echo "Succesfully transfered file to FTP 137.190.19.90 server"
	echo "No email was entered, no email confirmation sent"
	bash ftpAccess.sh MOCK_DATA_FILTER_*.zip $user $pass
fi

if [[ $? -eq 0 && ! -z $user && ! -z $pass ]]
then 
	user="anonymous"
	pass="password"
	echo ""
	echo "Uploading to ftp server..."
	echo "Succesfully transfered file to FTP 137.190.19.90 server"
	mail -s "Subject: Successful FTP email confirmatin"  $email < email_subject.txt
	echo "Sending verifications email to $email"
	bash ftpAccess.sh MOCK_DATA_FILTER_*.zip $user $pass
fi

if [[ $? -eq 0 ]]
then
	echo ""
	echo "Cleaning up..."
	bash cleanup.sh
fi

exit 0

