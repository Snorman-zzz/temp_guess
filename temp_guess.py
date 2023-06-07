"""
An application that provides recommendations on where to live based on temp ranges. 
"""


def main():
    """
    Asks the client for two temperatures. Based on the values, it provides cities
    that meets the conditions. 

    | City | High | Low |
    | Beijing | 33 | -8 |
    | Boston | 28 | -7 |
    | Honolulu | 32 | 13 |
    | San Francisco | 27 | 6 |
    | Vancouver BC | 24  | 2 |

    Values can be in any order.

    Examples:
        >>> main()                                       # doctest: +NORMALIZE_WHITESPACE
        Enter a temperature: 28
        Enter a second temperature: -10
        Boston
        San Francisco
        Vancouver
        >>> main()                                       # doctest: +NORMALIZE_WHITESPACE
        Enter a temperature: 0
        Enter a second temperature: 20
        Unknown
    


    """
    
    firstTemp = input("Enter a temperature: ")
    secondTemp = input("Enter a second temperature: ")


    if 13 <= int(firstTemp) <= 24 and 13 <= int(secondTemp) <= 24:
        cityName = "Beijing\nBoston\nHonolulu\nSan Francisco\nVancouver BC"
    elif 6 <= int(firstTemp) < 13 or 6 <= int(secondTemp) < 13:
        cityName = "Beijing\nBoston\nSan Francisco\nVancouver BC"
    elif 2 <= int(firstTemp) < 6 or 2 <= int(secondTemp) < 6:
        cityName = "Beijing\nBoston\nVancouver BC"
    elif -7 <= int(firstTemp) < 2 or -7 <= int(secondTemp) < 2:
        cityName = "Beijing\nBoston"
    elif -8 <= int(firstTemp) < -7 or -8 <= int(secondTemp) < -7:
        cityName = "Beijing"
    elif 24 < int(firstTemp) <= 27 or 24 < int(secondTemp) <= 27:
        cityName = "Beijing\nBoston\nHonolulu\nSan Francisco"
    elif 27 < int(firstTemp) <= 28 or 27 < int(secondTemp) <= 28:
        cityName = "Beijing\nBoston\nHonolulu"
    elif 28 < int(firstTemp) <= 32 or 28 < int(secondTemp) <= 32:
        cityName = "Beijing\nHonolulu"
    elif 32 < int(firstTemp) <= 33 or 32 < int(secondTemp) <= 33:
        cityName = "Beijing"
    else:
        cityName = "None"

    output = cityName

    print(output)

if __name__ == "__main__":
    main()
