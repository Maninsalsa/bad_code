def over_nine_thousand(lst):
    sum = 0
      while (sum < 9000):
        for i in lst:
          sum += i
      if sum > 9000:
        return sum
        break
    return sum