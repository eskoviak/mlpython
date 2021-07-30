docker run \
  --name mysql \
  --user 501:20 \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=terces \
  -v /Users/edmundlskoviak/data/mysql:/var/lib/mysql \
  -d mysql:latest \
  --local-infile=1 
