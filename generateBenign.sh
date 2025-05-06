# Number of times to repeat each curl request
REPEAT=1000

echo "Generating benign requests"

for i in $(seq 1 $REPEAT); do
  echo "Visit $i"

  # Homepage visit
  curl -s -A "Mozilla/5.0" http://localhost:8080/ > /dev/null

  # Contact form 
  curl -s -X POST http://localhost:8080/contact \
    -d "name=Alice$i&message=Hello+again" > /dev/null

  # Search
  curl -s "http://localhost:8080/search?q=item$i" > /dev/null

  # Fake login
  curl -s -X POST http://localhost:8080/login \
    -d "username=alice$i&password=test123" > /dev/null

  # Visit admin (non-malicious)
  curl -s -A "Mozilla/5.0 (Mac OS X)" http://localhost:8080/admin > /dev/null

  # About page or unknown but realistic path
  curl -s http://localhost:8080/about > /dev/null

  sleep 0.3  # Small delay
done

echo "Finished generating benign traffic!"
