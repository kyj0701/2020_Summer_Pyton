# h : hour
# m : minute

# h => 30h + 0.5m
# m => 6m

# h. > m. => 30h - 5.5m
# h. < m. => 5.5m - 30h
hour = 1
minutes = 57

h = 30 * hour + 0.5 * minutes
m = 6 * minutes

if h >= 360:
    h = h - 360
if m >= 360:
    m = m - 360

print(h)
print(m)

if h > m:
    if h - m >= 180:
        return 360 - (h - m)
    else:
        return h - m
else:
    if m - h >= 180:
        return 360 - (m - h)
    else:
        return m - h