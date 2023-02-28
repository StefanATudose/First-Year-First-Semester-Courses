siruri = "abudabi", "himalaya", "dumnezeu", "dumnzeu", "haos"
def primul_generator(*siruri, n):
    for i in siruri:
        if len(i) == n:
            yield i
n = 7

for i in primul_generator(*siruri, n = 7):
    print(i);