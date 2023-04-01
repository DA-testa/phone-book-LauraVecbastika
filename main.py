# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = input()
    n=int(n)
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))
class QueryProcessor:
    def init(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]
        self._prime = 1000000007
        self._multiplier = 263
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

def add(self, string):
    hashed = self._hash_func(string)
    bucket = self.buckets[hashed]
    if string not in bucket:
        self.buckets[hashed] = [string] + bucket

def delete(self, string):
    hashed = self._hash_func(string)
    bucket = self.buckets[hashed]
    for i in range(len(bucket)):
        if bucket[i] == string:
            bucket.pop(i)
            break

def find(self, string):
    hashed = self._hash_func(string)
    if string in self.buckets[hashed]:
        return "yes"
    return "no"

def process_queries(self, queries):
    result = []
    for query in queries:
        if query.type == 'add':
            self.add(query.string)
        elif query.type == 'del':
            self.delete(query.string)
        else:
            response = self.find(query.string)
            result.append(response)
    return result

if __name__ == '__main__':
    bucket_count = int(input())
    queries = read_queries()
    processor = QueryProcessor(bucket_count)
    result = processor.process_queries(queries)
    write_responses(result)
