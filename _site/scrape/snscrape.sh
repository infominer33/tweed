searchTerms=("Hyperledger+Aries" "DIDComm" "Key+Event+Receipt+Infrastructure" "w3c+Credentials" "atprotocol" "tbd+dwn")
hashTags=("verifiablecredentials" "selfsovereignidentity" "TrustoverIP" "internetidentityworkshop")
lastWeek=$(date  --date="7 days ago" +"%Y-%m-%d")
today=$(date --date="today" +"%Y-%m-%d")

for t in ${searchTerms[@]}; do
  echo $t
  snscrape --max-results 20 --jsonl --since $lastWeek twitter-search $t >> $today"_twitter.json"
done

for h in ${hashTags[@]}; do
  echo $h
  snscrape --max-results 20 --jsonl twitter-hashtag $h >> $today"_twitter.json"
done
