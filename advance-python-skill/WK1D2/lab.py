batch_1 = ["HEADER: SYSTEM A DATA", "100.2", "101.5", "100.9"]
batch_2 = ["HEADER: SYSTEM B DATA", "99.4", "98.7"]

import itertools as itl

merged_batches = itl.chain(
    itl.islice(batch_1, 1, None),  # Use None to reach the end of a stream
    itl.islice(batch_2, 1, None),  # Use None to reach the end of a stream
    )

for batch in merged_batches:
    print(batch)