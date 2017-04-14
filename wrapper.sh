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

##################### Getopts and  error handling  ###############################################

while getopts ":f:t:e:u:p:" opt
    do
        case $opt in
            f)
                begDate=$OPTARG
                ;;
            t)
                endDate=$OPTARG
                ;;
            e)
                email=$OPTARG
                ;;
            u)
                user=$OPTARG
                ;;
            p)
                password=$OPTARG
                ;;
            *) #send to usage function for how to enter
                usage
                ;;
        esac
    done

# If empty arguments are given call help prompt
if [[ -z "$begDate" || -z "$endDate" || -z "$email" || -z "$user" || -z "$password" ]]
then 
	echo ""
	echo "Missing Argument(s) parameter(s)."
	help_prompt
fi


#####################  Main shell execution  ##################################################
# Run create file only if optargs are equal to zero and FTPpassword has been entered.
    echo "entering python..."
	python3 create_report.py $begDate $endDate $email $user $password
    #capture exit code before we accidently change it
    code=$?

if [[ $code -eq 0 ]]
then
    echo "exit 0"
    exit 0
fi

if [[ $code -eq 1 ]]
then
    echo "exit 1"
    exit 1
fi

if [[ $code -eq 2 ]]
then
    echo "exit 2"
    exit 2
fi
