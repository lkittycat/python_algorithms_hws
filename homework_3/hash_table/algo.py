class HashTable:
    def __init__(self, capacity=8):
        if capacity < 1:
            raise ValueError("capacity must be positive")

        self.capacity = capacity
        self.size = 0
        self.buckets = []
        for i in range(capacity):
            self.buckets.append([])

    def insert(self, key, value):
        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        if (self.size + 1) * 4 > self.capacity * 3:
            self.resize()
            index = hash(key) % self.capacity
            bucket = self.buckets[index]

        bucket.append([key, value])
        self.size += 1

    def search(self, key):
        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        raise KeyError(key)

    def delete(self, key):
        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                self.size -= 1
                return

        raise KeyError(key)

    def resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = []

        for i in range(self.capacity):
            self.buckets.append([])

        for bucket in old_buckets:
            for pair in bucket:
                index = hash(pair[0]) % self.capacity
                self.buckets[index].append(pair)
