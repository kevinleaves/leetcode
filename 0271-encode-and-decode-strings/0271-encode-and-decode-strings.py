class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.

        ['Hello', 'world'] -> "5#Hello5#World"

        [''] -> '0#'

        init result string
        loop through input strings
            append length of curr string to res
            append delimiter of our choice to res
            append current string to res

        return res
        """
        res = ''
        for string in strs:
            res += f'{len(string)}#{string}'
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
                
         0123456789              
        "5#Hello5#World" ->

         01
        '0#'
        if encounter '0', append '' to res array, continue loop

        before we slice, we check if valid range using length. if possible, we split

        res = []
        while i < len(s)
            pull number from current pointer
            set j initial value to i + 2
            init empty string '' curr
            while len curr < number:
                curr += s[j]
                j += 1
            res append curr
            i += number + 2

        return res
        """

        res = []
        i = 0
        while i < len(s):
            # THIS DOESN'T HANDLE >9 NUMBERS
            # loop i until it hits the limiter, then convert it to a number
            number = ''
            while s[i] != '#':
                number += s[i]
                i += 1
            number = int(number)

            j = i + 1
            curr = ''
            while len(curr) < number:
                curr += s[j]
                j += 1
            res.append(curr)
            i += (number + 1)

        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))