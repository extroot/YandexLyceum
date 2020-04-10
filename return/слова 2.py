d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
     9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
     15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
     40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
     80: 'eighty', 90: 'ninety'}


def number_in_english(n):
    result = ''
    if n // 100 and n % 100:
        result = f'{d[n // 100]} hundred and '
    elif n // 100:
        result = f'{d[n // 100]} hundred'
        return result
    if n % 100 <= 19 or n % 10 == 0:
        result += d[n % 100]
    else:
        result += d[(n % 100 // 10) * 10] + ' ' + d[n % 10]
    return result
