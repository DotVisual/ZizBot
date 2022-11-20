echo "© Ziz Coding DE 2022" && echo "Starting Ziz-Nmap 7.40 ( ZizNmap )"
curl https://hackertarget.com/nmap-online-port-scanner/ --data "theinput="$1"&thetest=nmap&name_of_nonce_field=945655f3c3&_wp_http_referer=%2Fnmap-online-port-scanner%2F" 2>&1 | grep -Pzo "Host is up.(.|\n)*\nNmap done"
