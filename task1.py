__author__ = 'dinesh'

# TASK
# ------------------------------------------------------------------------------------------------------------------
# Write code to find a string of characters that contains only letters from
#
# acdegilmnoprstuw
#
# such that the hash(the_string) is
#
# 930846109532517
#
# if hash is defined by the following pseudo-code:
#
# Int64 hash (String s) {
#     Int64 h = 7
#     String letters = "acdegilmnoprstuw"
#     for(Int32 i = 0; i < s.length; i++) {
#         h = (h * 37 + letters.indexOf(s[i]))
#     }
#     return h
# }
# For example, if we were trying to find the 7 letter string where hash(the_string) was 680131659347, the answer would be "leepadg".



# characters valid for this program
VALID_CHARACTERS = 'acdegilmnoprstuw'

# taking first character as it has least hash value to cross check
FIRST_CHARACTER = VALID_CHARACTERS[0]


# program to get has value for the given character string
def compute_hash(string):
    h = 7
    for char in string:
        h = h * 37 + VALID_CHARACTERS.index(char)
    return h


# program to get string length based on given hash digit
def get_string_length(hash_length):
    string_length = 0
    while True:
        current_string = FIRST_CHARACTER * (string_length + 1)
        current_hash = compute_hash(current_string)
        if len(str(current_hash)) > hash_length:
            break
        string_length += 1
    return string_length


# program to get string from hash digit
def compute_string(hash):
    hash = int(hash)

    hash_length = len(str(hash))
    string_length = get_string_length(hash_length)

    if (string_length == 0):
        return ""

    chars = []
    for i in range(string_length):
        previous_char = None
        for char in VALID_CHARACTERS:
            current_string = ''.join(chars) + char + FIRST_CHARACTER * (string_length - i - 1)
            current_hash = compute_hash(current_string)
            if current_hash == hash:
                return current_string
            elif current_hash > hash:
                chars.append(previous_char or FIRST_CHARACTER)
                break
            else:
                previous_char = char
