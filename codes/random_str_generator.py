import random
import string


# 生成长度为 nums 的随机字符串
def random_str_generator(nums):
    s = string.digits + string.ascii_letters
    samples = random.sample(s, nums)
    return ''.join(samples)


for i in range(20):
    print(str(i) + ":" + random_str_generator(i))
