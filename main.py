n = int(input())
arrivals = []
departures = []
for i in range(n):
    x = list(map(int, input().split()))
    arrivals.append(x[0])
    departures.append(x[1])

i = 0
j = 0
platform_needed = 0
max_platform_needed = 0
while i < len(arrivals) and j < len(departures):
    if arrivals[i] < departures[j]:
        i+=1
        platform_needed += 1
    else:
        j+=1
        platform_needed -= 1
    max_platform_needed = max(max_platform_needed, platform_needed)


print(max_platform_needed)