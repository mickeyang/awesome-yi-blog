from collections import defaultdict, Counter
import itertools as itl

mock_event_stream = [
    ("adv_123", "impression"),
    ("adv_456", "impression"),
    ("adv_123", "click"),
    ("adv_123", "impression"),
    ("adv_456", "click"),
    ("adv_789", "impression")
]

def aggregate_ad_data(event_stream):
    event_types = defaultdict(list)
    global_counts = Counter()

    for adv_id, event_type in event_stream:
        event_types[adv_id].append(event_type)  # this is aggregation
        global_counts[event_type] += 1  # this is counting, when a new event_type comes in, starting it from 0.

    return event_types, global_counts

result = aggregate_ad_data(mock_event_stream)
result[0]["adv_123"]
result[1]["impression"]
result[1]["click"]
