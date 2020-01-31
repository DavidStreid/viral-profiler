import unittest

from parse_variants import parse_variant_file, POS_COL, ALLELES, NUCLEOTIDE, COUNT

class ParseVariants(unittest.TestCase):
    def test_parse_variant_file(self):
        """
        Test that the variant file is parsed correctly
        """
        test_file = './test/test_file.variation'

        parsed_content = parse_variant_file(test_file )
        expected_content = [
            {
                POS_COL: 1591,
                ALLELES: [
                    {NUCLEOTIDE: 'C', COUNT: 1}
                ]
            },
            {
                POS_COL: 1592,
                ALLELES: [
                    {NUCLEOTIDE: 'C', COUNT: 3},
                    {NUCLEOTIDE: 'T', COUNT: 5}
                ]
            },
            {
                POS_COL: 1593,
                ALLELES: [
                    {NUCLEOTIDE: 'T', COUNT: 8},
                    {NUCLEOTIDE: 'G', COUNT: 4}
                ]
            },
            {
                POS_COL: 1594,
                ALLELES: [
                    {NUCLEOTIDE: 'A', COUNT: 1},
                    {NUCLEOTIDE: 'T', COUNT: 1}
                ]
            }
        ]
        self.assertEqual(parsed_content, expected_content)


if __name__ == '__main__':
    unittest.main()
