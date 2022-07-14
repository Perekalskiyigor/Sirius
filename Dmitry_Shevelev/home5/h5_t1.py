n = int(input("count>"))


def str_list(ent):
    return list(map(int, ent.split()))


nums = str_list(input("nums>"))
dist = []

for ind, house in enumerate(nums):
    neib_l = -1
    neib_r = -1
    if house == 0:
        dist.append(0)
        # print(ind, 0)
    else:
        for counter in range(1, len(nums)):
            if ind+counter < len(nums):
                neib_l = nums[ind+counter]
            if ind-counter >= 0:
                neib_r = nums[ind-counter]
            if neib_l == 0 or neib_r == 0:
                # print(ind, counter)
                dist.append(counter)
                break
print(*dist)