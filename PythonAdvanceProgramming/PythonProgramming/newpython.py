def make_it_equal(A, B):
    if '%' not in A:
        if A == B:
            return ""
        else:
            return "-1"
    if A.count('%') > 1:
        return "-1"
    prefix, suffix = A.split('%')
    if len(B) < len(prefix) + len(suffix):
        return "-1"
    if not B.startswith(prefix):
        return "-1"
    if not B.endswith(suffix):
        return "-1"
    return B[len(prefix):len(B) - len(suffix)]

# non editable starts here
if __name__ == "__main__":
    A = input().strip()
    B = input().strip()
    print(make_it_equal(A, B))
# non editable ends here
