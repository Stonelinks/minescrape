#!/bin/sh
curl 'https://arlweb.msha.gov/drs/ASP/BasicMineInfostatecounty.asp' -H 'Pragma: no-cache' -H 'Origin: https://arlweb.msha.gov' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.8,ja;q=0.6' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: no-cache' -H 'Referer: https://arlweb.msha.gov/drs/asp/extendedsearch/statebycommodityoutput2.asp' -H 'Connection: keep-alive' --data 'MineId='"$1"'' --compressed
