ktutil << EOF
rkt /etc/security/keytabs/impala.service.keytab
rkt /etc/security/keytabs/impala-http.service.keytab
wkt /etc/security/keytabs/impala-http.keytab
quit
EOF
chmod 400 /etc/security/keytabs/impala-http.keytab
chown impala:impala /etc/security/keytabs/impala-http.keytab
