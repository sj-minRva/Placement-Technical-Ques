
strings = ['ab', 'ab', 'bc', 'bc', 'bc', 'abc']
queries = ['ab', 'abc', 'bc']


def matchingStrings(strings, queries):
    count = 0
    results = []
    for i in queries:
        for j in strings:
            if i == j:
                count += 1
        results.append(count)
        count = 0
    return results

    
ans = matchingStrings(strings, queries)
print(ans)
