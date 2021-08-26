def longestCommonPrefix(strs):
    min_length = 99999999
    result = ''
    for i in strs:
        if min_length > len(i):
            min_length = len(i)

    for i in range(min_length):
        x = strs[0][i]
        # print(strs[:])
        for j in range(len(strs)):
            if strs[j][i] != x:
                if result == '':
                    return ''
                    # print('')

                else:
                    return result

        result = result + x
    return result


def main():
    longestCommonPrefix(["flower", "flow", "flight"])
    longestCommonPrefix(["dog", "racecar", "car"])


main()
