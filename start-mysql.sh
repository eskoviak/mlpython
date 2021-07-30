docker run \
  --name mysql \
  --user 1000:1000 \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=terces \
  -v ~/data/mysql:/var/lib/mysql \
  -d mysql:latest \
  --local-infile=1 
