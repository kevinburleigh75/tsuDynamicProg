

def make_array(nrows,ncols):
    arr = []
    for _ in range(nrows):
        arr.append([None]*ncols)
    return arr

def get_splits(idx_lo, idx_hi, best_idxs):
    print('{},{}'.format(idx_lo,idx_hi))
    if idx_lo >= idx_hi:
        return [idx_lo]
    else:
        split_idx = best_idxs[idx_lo][idx_hi]
        return ['('] + get_splits(idx_lo, split_idx, best_idxs) + [')' + '('] + get_splits(split_idx+1, idx_hi, best_idxs) + [')']

def solve(dims):
    num_matrices = len(dims) - 1
    print('num_matrices = {}'.format(num_matrices))

    best_costs = make_array(num_matrices, num_matrices)
    best_idxs  = make_array(num_matrices, num_matrices)

    (split, cost) = find_best(
        idx_lo      = 0,
        idx_hi      = num_matrices-1,
        dims        = dims,
        best_costs  = best_costs,
        best_idxs   = best_idxs,
    )

    splits = get_splits(0, num_matrices-1, best_idxs)

    return (cost, splits)

def find_best(idx_lo, idx_hi, dims, best_costs, best_idxs):
    # print('lo={} hi={}'.format(idx_lo, idx_hi))
    if best_idxs[idx_lo][idx_hi] is None:
        print('lo={} hi={}'.format(idx_lo, idx_hi))

        if idx_lo == idx_hi:
            best_idxs[idx_lo][idx_hi]  = -1
            best_costs[idx_lo][idx_hi] =  0
        else:
            best_idx  = None
            best_cost = None
            for split_idx in range(idx_lo, idx_hi):
                (_, cost_1) = find_best(idx_lo,      split_idx, dims, best_costs, best_idxs)
                (_, cost_2) = find_best(split_idx+1, idx_hi,    dims, best_costs, best_idxs)
                total_cost = cost_1 + cost_2 + dims[idx_lo]*dims[split_idx+1]*dims[idx_hi+1]
                if (best_cost is None) or (total_cost < best_cost):
                    best_idx  = split_idx
                    best_cost = total_cost
            best_idxs[idx_lo][idx_hi]  = best_idx
            best_costs[idx_lo][idx_hi] = best_cost

    return (best_idxs[idx_lo][idx_hi], best_costs[idx_lo][idx_hi])

def main():
    # dims = [10,100,5,50]
    dims = [2,3,5,1,2,5]
    (split, cost) = solve(dims)
    print('{} {}'.format(split, cost))

if __name__ == '__main__':
    main()
