# Michael Soltys
# Feb 10, 2017
#
# Example password cracker

JOHN='/home/ubuntu/Crackers/JohnTheRipper/'

# Create the MD5 hash of <arg> in "exm.sh <arg>"
# and set variab HASH to it
read -p "Create hash corresponding to the password:"
HASH="$(echo -n $1 | md5sum | awk '{print $1;}')"

# put the hash in file "hash.txt"
echo -n $HASH > hash.txt

echo "Password = " $1
echo "MD5 hash = " $HASH

# Use john to attempt to crack the hash in "hash.txt"
read -p "Run john on the hash:"
${JOHN}run/john --format=Raw-MD5 hash.txt

# Just in case the password was already cracked before
# (so john will not bother to run)
# display all passwords cracked already
read -p "A list of passwords already cracked:"
more ${JOHN}run/john.pot
