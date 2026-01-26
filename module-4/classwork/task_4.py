def stars(n):
    if n == 0:
        return ""
    return "*" + stars(n - 1)

print(stars(1))