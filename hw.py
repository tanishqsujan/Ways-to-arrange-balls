def min_platforms(arrival, departure):
    n = len(arrival)
    max_platforms = 1

    for i in range(n):
        platforms = 1  

        for j in range(n):
            if i != j:
                if (arrival[j] >= arrival[i] and arrival[j] < departure[i]) or \
                   (arrival[i] >= arrival[j] and arrival[i] < departure[j]):
                    platforms += 1

        max_platforms = max(max_platforms, platforms)

    return max_platforms


arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

print("Minimum platforms required:", min_platforms(arrival, departure))