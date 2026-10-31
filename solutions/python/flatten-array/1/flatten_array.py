def flatten(iterable):
    return list(helper(iterable))
                
def helper(iterable):
    for item in iterable:
        if isinstance(item, list):
            yield from helper(item)
        else:
            if item != None:
                yield item