# You are given a large sample of integers in the range [0, 255]. Since the sample is so large, it is represented by an array count where count[k] is the number of times that k appears in the sample.

# Calculate the following statistics:

# minimum: The minimum element in the sample.
# maximum: The maximum element in the sample.
# mean: The average of the sample, calculated as the total sum of all elements divided by the total number of elements.
# median:
# If the sample has an odd number of elements, then the median is the middle element once the sample is sorted.
# If the sample has an even number of elements, then the median is the average of the two middle elements once the sample is sorted.
# mode: The number that appears the most in the sample. It is guaranteed to be unique.
# Return the statistics of the sample as an array of floating-point numbers [minimum, maximum, mean, median, mode]. Answers within 10-5 of the actual answer will be accepted.


class Solution:
    def sampleStats(self, count: list) -> list:
        cnt = [(i, n) for i, n in enumerate(count) if n > 0]
        len_c = sum(tpl[1] for tpl in cnt)
        len_half = len_c // 2
        odd = bool(len_c % 2)
        
        mean = float(sum(k * n for k, n in cnt)) / len_c
        
        smallest = cnt[0][0]
        
        largest = cnt[-1][0]
        
        mode = max(cnt, key=lambda tpl: tpl[1])[0]
        
        left = 0
        
        for i, (k, n) in enumerate(cnt):
            left += n
            if left > len_half:
                prev_left = left - n
                if not odd and prev_left == len_half:
                    median = float(k + cnt[i - 1][0]) / 2
                else:
                    median = k
                break
                
        return [smallest, largest, mean, median, mode]