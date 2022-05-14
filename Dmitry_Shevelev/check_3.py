def find_athlets(a, b, c, d, e, f, g, h, k):
    know_english = [a, b, c]
    sportsmen = [d, e, f]
    more_than_20_years = [g, h, k]
    print(list(set(know_english) & set(sportsmen) & set(more_than_20_years)))
