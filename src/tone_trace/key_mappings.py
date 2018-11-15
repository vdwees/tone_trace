# Numbers mapping to (note, note-length) pairs
# TODO: Make timing correspond to line execution duration?
default_key_mapping = {
    1: ("c", 1),
    2: ("c#", 1),
    3: ("d", 1),
    4: ("d#", 1),
    5: ("e", 1),
    6: ("f", 1),
    7: ("f#", 1),
    8: ("g", 1),
    9: ("g#", 1),
    10: ("a", 1),
    11: ("a#", 1),
    12: ("b", 1),
    13: ("c", 2),
    14: ("c#", 2),
    15: ("d", 2),
    16: ("d#", 2),
    17: ("e", 2),
    18: ("f", 2),
    19: ("f#", 2),
    20: ("g", 2),
    21: ("g#", 2),
    22: ("a", 2),
    23: ("a#", 2),
    24: ("b", 2),
    25: ("c", 3),
    26: ("c#", 3),
    27: ("d", 3),
    28: ("d#", 3),
    29: ("e", 3),
    30: ("f", 3),
    31: ("f#", 3),
    32: ("g", 3),
    33: ("g#", 3),
    34: ("a", 3),
    35: ("a#", 3),
    36: ("b", 3),
    37: ("c", 4),
    38: ("c#", 4),
    39: ("d", 4),
    40: ("d#", 4),
    41: ("e", 4),
    42: ("f", 4),
    43: ("f#", 4),
    44: ("g", 4),
    45: ("g#", 4),
    46: ("a", 4),
    47: ("a#", 4),
    48: ("b", 4),
    49: ("c", 5),
    50: ("c#", 5),
    51: ("d", 5),
    52: ("d#", 5),
    53: ("e", 5),
    54: ("f", 5),
    55: ("f#", 5),
    56: ("g", 5),
    57: ("g#", 5),
    58: ("a", 5),
    59: ("a#", 5),
    60: ("b", 5),
    61: ("c", 6),
    62: ("c#", 6),
    63: ("d", 6),
    64: ("d#", 6),
    65: ("e", 6),
    66: ("f", 6),
    67: ("f#", 6),
    68: ("g", 6),
    69: ("g#", 6),
    70: ("a", 6),
    71: ("a#", 6),
    72: ("b", 6),
    73: ("c", 7),
    74: ("c#", 7),
    75: ("d", 7),
    76: ("d#", 7),
    77: ("e", 7),
    78: ("f", 7),
    79: ("f#", 7),
    80: ("g", 7),
    81: ("g#", 7),
    82: ("a", 7),
    83: ("a#", 7),
    84: ("b", 7),
    85: ("c", 8),
}


def translate_to_note(line_num):
    """Put arbitrary int into the key mapping range"""
    notes_len = 84  # starts at 1, goes to 85
    normalized = abs(line_num % (notes_len * 2) - notes_len) + 1
    return default_key_mapping[normalized]