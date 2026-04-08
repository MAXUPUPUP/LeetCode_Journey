def build_prefix_sum(nums):
    pre = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        pre[i + 1] = pre[i] + x
    return pre


def range_sum(pre, left, right):
    return pre[right + 1] - pre[left]
