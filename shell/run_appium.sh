RESTART="appium"
 

 

PGREP="/usr/bin/pgrep"
 

APPIUM="appium"
 
# find httpd pid
$PGREP ${APPIUM}
 
if [ $? -ne 0 ] 
then
 # restart appium
 $RESTART
fi