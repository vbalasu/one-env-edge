from chalice import Chalice

app = Chalice(app_name='one-env-edge')


@app.route('/')
def index():
    produce()
    return {'hello': 'world'}

@app.route('/produce/{topic}/{message}', methods=['GET'])
def get_produce(topic, message):
    return produce(topic, message)

@app.route('/produce', methods=['POST'])
def post_produce():
    topic = app.current_request.json_body['topic']
    message = app.current_request.json_body['message']
    return produce(topic, message)


def produce(topic, message):
    from kafka import KafkaProducer
    producer = KafkaProducer(bootstrap_servers='b-2.oetrta-kafka.oz8lgl.c3.kafka.us-west-2.amazonaws.com:9092')
    future = producer.send(topic, bytes(message, 'utf8'))
    result = future.get(timeout=60)
    return result

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
