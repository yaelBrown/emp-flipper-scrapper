aa = '$4,078,906'


def convertToInt(n):
    return int(n.replace("$", "").replace(",", ""))
    
    
# print(convertToInt(aa))
    
    
    
    
bb = "{'listingId': '#52900', 'niche': 'Art', 'monthlyNet': '$47,488', 'price': '$2,231,940'}"


def convertToDict(s):
    return dict(bb)
    
print(bb[16:21])