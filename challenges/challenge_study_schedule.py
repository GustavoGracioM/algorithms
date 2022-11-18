def study_schedule(permanence_period, target_time=None):
    if isinstance(target_time, int):
        count = 0
        for pp in permanence_period:
            if not isinstance(pp[0], int) or not isinstance(pp[1], int):
                return None
            if target_time >= pp[0] and target_time <= pp[1]:
                count += 1
        return count
    else:
        return None


permanence_period = [(None, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

print(study_schedule(permanence_period, 1))
