# def build_index(documents):
#     index = []

#     for i, doc in enumerate(documents):
#         word_count = {}


#         words = doc.split()
#         for word in words:
#             if word not in word_count:
#                 word_count[word] = 0
#             word_count[word] += 1

#         index.append(word_count)

#     return index

# def process_query(index, query):
#     words = query.split()

#     relevance = {}

#     for doc_id, word_counts in enumerate(index):
#         total_relevance = sum(word_counts.get(word, 0) for word in words)

#         if total_relevance > 0:
#             relevance[doc_id + 1] = total_relevance

#     sorted_docs = sorted(relevance.items(), key=lambda x: (-x[1], x[0]))

#     result = [doc_id for doc_id, _ in sorted_docs[:5]]

#     return result

# n = int(input())
# documents = [input().strip() for _ in range(n)]
# m = int(input())
# queries = [input().strip() for _ in range(m)]

# index = build_index(documents)

# for query in queries:
#     print(" ".join(map(str, process_query(index, query))))



def build_index(documents):
    index = []

    for i, doc in enumerate(documents):
        word_count = {}


        words = doc.split()
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

        index.append(word_count)

    return index

def process_query(index, query):
    words = query.split()

    relevance = {}

    for doc_id, word_counts in enumerate(index):
        total_relevance = sum(word_counts.get(word, 0) for word in words)

        if total_relevance > 0:
            relevance[(total_relevance, -(doc_id + 1))] = doc_id + 1

    sorted_docs = sorted(relevance.keys())

    result = [relevance[key] for key in sorted_docs]

    return result[:5]

n = int(input())
documents = [input().strip() for _ in range(n)]
m = int(input())
queries = [input().strip() for _ in range(m)]

index = build_index(documents)

for query in queries:
    print(" ".join(map(str, process_query(index, query))))