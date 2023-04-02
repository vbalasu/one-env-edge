# CURL GET
# curl "$(chalice url)produce/vijay_balasubramaniam_oetrta_kafka_test/hello_from_lambda"

# HTTP POST string
# http post "$(chalice url)produce" topic=vijay_balasubramaniam_oetrta_kafka_test message=hello_lambda_post

# HTTP POST json object
# echo '{"topic": "vijay_balasubramaniam_oetrta_kafka_test", "message": {"hello": "world"}}' | http post "$(chalice url)produce"

# OR USE CURL to POST a json object
# echo '{"topic": "vijay_balasubramaniam_oetrta_kafka_test", "message": {"hello": "world"}}' | curl -H "Content-Type: application/json" -X POST --data-binary @- $(chalice url)produce

