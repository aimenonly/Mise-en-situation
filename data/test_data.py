#################################################
#####             GLOBAL DATA               #####
#################################################


#local machine

LOCAL="192.168.0.27"
LOCAL_PORT=22
LOCAL_USERNAME="aimen"
LOCAL_PASSWORD="aimen"
LOCAL_SSHKEY_PATH=""  #the path of private key if the remote server uses public/private key pairs as authentification method

#remote machine

REMOTE="192.168.0.27"
PORT=22
USERNAME="aimen"
PASSWORD="aimen"
SSHKEY_PATH=""  #the path of private key if the remote server uses public/private key pairs as authentification method

#test environnement setup

REPORTS_PATH="/home/aimen/Documents/MISE-EN-SITUATION/reports" #Directory used to store reports of test runs


#################################################
#####           TEST SPECIFIC DATA          #####
#################################################


### TEST CASE 1

COMMAND_TO_EXECUTE="ls"

### TEST CASE 2

REMOTE_LOGS_PATH="/home/aimen/Documents/DIRECTORY/test_file1.txt"
LOCAL_TMP_PATH="/home/aimen/Documents/MISE-EN-SITUATION/tmp/" #Temporary directory used to store files locally during tests
PROCESS_TO_CHECK="CRON"

### TEST CASE 3

FILES_TO_CHECK = {
    "/home/aimen/Documents/DIRECTORY/test_file1.txt": 89,
    "/home/aimen/Documents/DIRECTORY/test_file2.csv": 39,
    "/home/aimen/Documents/DIRECTORY/test_file3.csv": 60,
    "/home/aimen/Documents/DIRECTORY/test_file4.txt": 80,
    "/home/aimen/Documents/DIRECTORY/test_file5.txt": 5,
}




