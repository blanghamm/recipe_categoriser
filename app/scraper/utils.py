def num(s):
    trim = s.strip()
    if not trim.isdigit():
        return trim
    try:
        return int(trim)
    except ValueError:
        return float(trim)
