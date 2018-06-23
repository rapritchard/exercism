def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        if len(strand_a) == 0 and len(strand_b) == 0:
            return 0
        else:
            count = 0
            for a, b in zip(strand_a, strand_b):
                if a != b:
                    count += 1
        return count
    else:
        raise ValueError("Stands must be the same length")
