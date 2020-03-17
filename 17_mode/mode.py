def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_count = {}

    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    highest_count = 0

    for num in num_count.keys():
        if num_count[num] > highest_count:
            highest_count = num_count[num]
            highest_num = num
    
    return highest_num