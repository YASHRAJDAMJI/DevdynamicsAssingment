from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)


topics = {
    "Oop": set(),
    "DBMS": set(),
    "OS": set(),
    "Blockchain": set()
}

subscribers = {}

def generate_subscriber_id(name):
    prefix = name[:2].upper()
    suffix = ''.join(random.choices(string.digits, k=4))
    return prefix + suffix

@app.route('/createsubscriberid', methods=['POST'])
def create_subscriber_id():
    data = request.get_json()
    name = data.get('name')

    if not name or len(name) < 2:
        return jsonify({"error": "Invalid subscriber name"}), 400

    subscriber_id = generate_subscriber_id(name)
    subscribers[name] = subscriber_id
    return jsonify({"message": "Subscriber ID created", "subscriberId": subscriber_id}), 201

@app.route('/getsubscriberid', methods=['GET'])
def get_subscriber_id():
    name = request.args.get('name')

    if not name or len(name) < 2:
        return jsonify({"error": "Invalid subscriber name"}), 400

    subscriber_id = subscribers.get(name)
    if not subscriber_id:
        return jsonify({"error": "No subscriber found"}), 404

    return jsonify({"subscriberId": subscriber_id}), 200

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    topic_id = data.get('topicId')
    subscriber_id = data.get('subscriberId')

    if not topic_id or not subscriber_id:
        return jsonify({"error": "Invalid input"}), 400

    if topic_id not in topics:
        return jsonify({"error": "Topic not found"}), 404

    if len(subscriber_id) != 6 or not subscriber_id.isalnum():
        return jsonify({"error": "Subscriber ID should be 6 alphanumeric characters"}), 400

    topics[topic_id].add(subscriber_id)
    return jsonify({"message": f"Subscriber {subscriber_id} subscribed to topic {topic_id}"}), 200

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json()
    topic_id = data.get('topicId')

    if not topic_id:
        return jsonify({"error": "Invalid input"}), 400

    if topic_id not in topics:
        return jsonify({"error": "Invalid topic ID"}), 404

    if not topics[topic_id]:
        return jsonify({"message": "No subscribers to notify"}), 200

    subscribers = list(topics[topic_id])
    return jsonify({"message": f"Notified subscribers of topic {topic_id}", "subscribers": subscribers}), 200

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    data = request.get_json()
    topic_id = data.get('topicId')
    subscriber_id = data.get('subscriberId')

    if not topic_id or not subscriber_id:
        return jsonify({"error": "Invalid input"}), 400

    if topic_id not in topics:
        return jsonify({"error": "Topic not found"}), 404

    if len(subscriber_id) != 6 or not subscriber_id.isalnum():
        return jsonify({"error": "Subscriber ID should be 6 alphanumeric characters"}), 400

    if subscriber_id in topics[topic_id]:
        topics[topic_id].remove(subscriber_id)
        return jsonify({"message": f"Subscriber {subscriber_id} unsubscribed from topic {topic_id}"}), 200
    else:
        return jsonify({"error": "Subscription not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
