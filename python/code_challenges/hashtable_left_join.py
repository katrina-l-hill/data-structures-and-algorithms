def left_join(hashmap_1, hashmap_2):
    output = (
        []
    )  # empty list (new data structure) for the results of the joined hashmaps
    for (
        key
    ) in (
        hashmap_1
    ):  # start with the first hashmap since all it's values will be returned.
        left_side_first = [
            key,
            hashmap_1.get(key),
            hashmap_2.get(key),
        ]  # the keys are retrieved and assigned to this variable
        output.append(
            left_side_first
        )  # values on the right side (hashmap_2) will be appended to the left side (hashmap_1)
    return output
