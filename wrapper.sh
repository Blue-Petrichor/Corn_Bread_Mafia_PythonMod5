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
#        AUTHOR: Corn Bread Mafia
#  ORGANIZATION: 
#       CREATED: 04/07/2017 20:21
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error


#####################  Help functions   ##################

# prompt for help
help_prompt()
{
	echo ""
	echo "<Filename.sh> takes five parameters:"
	echo "For help on how to enter parameters type:"
	echo "bash <filename.sh> --help"
	echo
}

# Function if exit process is not correct or = 0
usage()
{
	echo "Try:"
	echo "(-f <begDate>) (-t <endDate>) (-e <email>)  (-u <user name>)  (-p <password>)"
	echo "     required       required       required      required          required  "
	echo " " 
	exit 1
}
# Function if email is not valid
email_usage()
{
	echo "ex: john_doe@something.com .org .edu etc...."
	echo " "
	exit 1
}
# Function if begin date is not valid
begDateUsage()
{
	echo "Invalid length or format for begin search date."
	echo "Usage For Begin Date: YYYYMMDD "
	echo " "
	exit 1
}
# Function if end date is not valid
endDateUsage()
{
	echo "Invalid length or format for end search date."
	echo "Usage For End Date: YYYYMMDD "
	echo " "
	exit 1
}
################ END HELP FUNCTIONS ##############################################################

#check for the --help option for first param was entered
if [[ $1 == "--help" ]]
then
	usage
fi

##################### Getopts and  error handling  ###############################################

if [[ $1 != --help && ! -z "$2" && ! -z "$4" && ! -z "$6" && ! -z "$8" && ! -z "$10" ]]
then
	while getopts ":f:t:e:u:p:" opt
	do
		case $opt in
			f) 
				begDate=$OPTARG
				# Check if is empty and is lengh of 8, is an integer value, and non-negative
				if [[  ! -z $1 && ${#2} == 8 && $2 == ?(-)+([0-9]) ]]
				then 
					echo ""
					echo "Begin search date has been verified: "
				else
					begDateUsage
				fi
				;;
			t) 
				endDate=$OPTARG
				# Check if is empty and is lengh of 8, is an integer value, and non-negative
				if [[ ! -z $3 && ${#4} == 8 && $4 == ?(-)+([0-9]) ]]
				then
					echo "Ending search date has been verified: "
				else
					endDateUsage
				fi
				;;
			e)  
				email=$OPTARG
				if [[ ! -z $5 && $6 =~ @ && $3 =~ . ]]
				then
					# make varible to store email for use
					echo "$6 is an accepted email address:"
					else
						echo " "
						echo "$6 is partial or missing requirements, see help below:"
						email_usage
				fi
				;;
			u) 
				FTPuser=$OPTARG
				# verify if the first Argument is not empty and print welcome messeage if correct.
				user=$OPTARG
				if [[ ! -z $7  ]]
				then 
					echo "Welcome $8!"
				else
					usage
				fi
				;;
			p)  
				FTPpassword=$OPTARG
				# Verify if the second Argument is not empyt and print if successfully set.
				if [[ ! -z $9 ]]
				then 
					echo "Password is now set: ********"
				else
					usage
				fi
				;;

			*) #send to usage function for how to enter
				usage
				;;
		esac
	done
fi

# If empty arguments are given call help prompt
if [[ -z "$begDate" || -z "$endDate" || -z "$email" || -z "$FTPuser" || -z "$FTPpassword" ]]
then 
	echo ""
	echo "Missing Argument(s) parameter(s)."
	help_prompt
fi


#####################  Main shell execution  ##################################################
python3 create_report.py $begDate $endDate

if [[ $? -eq 0 ]]
then
	echo ""
	echo "Need to change this in the main but for now the Date args have been passed ..."
	echo "This is line 154 - 160"
fi

exit 0

