#DYNAMIC PROGRAMMING WAY
map_it={1:1,2:2,3:4}
def countWaysDP(n, map_it):
    if n<=0:
        return 0
    elif n in map_it:
        return map_it[n]
    else:
        map_it[n]= countWaysDP(n-1, map_it)+countWaysDP(n-2, map_it)+countWaysDP(n-3, map_it)
        return map_it[n]