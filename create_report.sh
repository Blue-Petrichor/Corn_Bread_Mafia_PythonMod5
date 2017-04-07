#!/bin/bash - 
#===============================================================================
#
#          FILE: create_report.sh
# 
#         USAGE: ./create_report.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Corn_Bread_Mafia
#  ORGANIZATION: 
#       CREATED: 04/07/2017 14:32
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error



begin=$1
end=$2


if [[ ! -d temp ]]
then 
	mkdir temp
fi

present=$PWD

cd temp

echo $begin
echo $end

$begin=
#if [[ $fileIn == 2015 || $fileIn == 2016 ]]
#then
#	for i in `seq $fileIn -1 2015`
#	do 
#	wget http://icarus.cs.weber.edu/~hvalle/cs3030/MOCK_DATA_$1.tar.gz
#									done
#										cd $present
#
##									else
#											echo "No such file exists."
#												exit 1
#											fi




exit 0

