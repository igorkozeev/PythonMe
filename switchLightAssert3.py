market_2nd = {'ns':'green', 'ew':'red'}

def switchLight(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'

    #Sanity check. In plain english, it's saying: "I assert that this condition
    #always holds True and if not, there is a clearly a bug there.
    assert 'res' in intersection.values(), 'Neither light is red!' 


print(market_2nd)
switchLight(market_2nd)
print(market_2nd)
