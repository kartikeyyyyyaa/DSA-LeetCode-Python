def lcp():
    strs=list(map(str,input().split()))
    if not strs:
        return ""
    strs.sort()
    first = strs[0]
    last = strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        print(strs[i])
        i += 1
    print(first[:i])
    return first[:i]