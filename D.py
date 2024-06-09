def build_prefix_table(pattern):
    m = len(pattern)
    prefix_table = [0] * m
    j = 0
    
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_table[i] = j
    
    return prefix_table

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix_table = build_prefix_table(pattern)
    j = 0
    occurrences = []
    
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i - m + 1)
            j = prefix_table[j - 1]
    
    return occurrences

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    s1 = data[0]
    s2 = data[1]
    
    occurrences = kmp_search(s2, s1)
    
    print(len(occurrences))
    for pos in occurrences:
        print(pos)

if __name__ == "__main__":
    main()
