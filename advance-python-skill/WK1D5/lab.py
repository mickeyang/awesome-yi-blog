class CumulativeSumStream:
    def __init__(self, data_stream):
        self.data_stream = iter(data_stream) # turn an object into an iterator so that I do not need to use len() function to determine boundary, also no need to know current_position (index)
        self.running_total = 0
        # self.length = len(data_stream)
        # self.current_position = 0

    def __iter__(self):
        return self

    def __next__(self):
        next_value = next(self.data_stream)
        self.running_total += next_value
        
        # if self.current_position >= self.length:
        #     raise StopIteration  # the next() function automatically raise StopIteration

        # self.running_total += self.data_stream[self.current_position]
        # self.current_position += 1

        return self.running_total

mock_payloads = [10, 20, 5, 15]

sum_stream = CumulativeSumStream(mock_payloads)

for m in sum_stream:
    print(m)