import unittest
from main import funnyString, alternatingCharacters, caesarCipher, alternate, gridChallenge

class TestHackerRank(unittest.TestCase):
    def test_funnyString(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_alternatingCharacters(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        self.assertEqual(alternatingCharacters("BABABA"), 0)
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_caesarCipher(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")
        self.assertEqual(caesarCipher("Always-Look-on-the-Bright-Side-of-Life", 5), "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj")
        self.assertEqual(caesarCipher("1234", 10), "1234")

    def test_alternate(self):
        self.assertEqual(alternate("beabeefeab"), 5)
        self.assertEqual(alternate("a"), 0)
        self.assertEqual(alternate("ab"), 2)
        self.assertEqual(alternate("aba"), 3)
        self.assertEqual(alternate("asdcbsdcagfsdbgdfanfghbsfdab"), 8)
        self.assertEqual(alternate("asvkugfiugsalddlasguifgukvsa"), 0)

    def test_gridChallenge(self):
        self.assertEqual(gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES")
        self.assertEqual(gridChallenge(["mpxz", "abcd", "wlmf"]), "NO")
        self.assertEqual(gridChallenge(["abc", "hjk", "mpq", "rtv"]), "YES")

if __name__ == '__main__':
    unittest.main()