l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 'hackerrank'

def hackerrankInString(s):
    needle = 'hackerrank'
    idx_in_needle = 0
    for c in s:
        if c == needle[idx_in_needle]:
            idx_in_needle += 1
        if idx_in_needle == len(needle):
            break
             
    if idx_in_needle == len(needle):
        return "YES"
    else: 
        return "NO"

total = hackerrankInString(a)
print(total)
