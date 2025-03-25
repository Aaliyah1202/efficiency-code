def find_pair (arr,target=9):
    seen=set()
    for num in arr: 
        complement = target-num
        if complement in seen: 
            return num, complement 
        seen.add(num)
        return None #if no pair is found 