def sum_of_multiples(limit, multiples):
    all_vals = set()

    for m in multiples:
        if m == 0:
            continue
        idx = 1
        while((m*idx) < limit):
            curr_sum = m * idx
            all_vals.add(curr_sum)
            idx+=1

    return sum(all_vals)