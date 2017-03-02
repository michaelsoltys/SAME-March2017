#!/bin/sh
# Michael Soltys, March 2, 2017
# usage: retrieve-cert.sh <remote.host.naem> [port]
#
REMHOST=$1
REMPORT=${2:-443}

echo |\
openssl s_client -connect ${REMHOST}:${REMPORT} 2>&1 |\
sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p'
