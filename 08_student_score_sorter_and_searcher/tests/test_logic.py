import unittest
from src.logic.sorting import bubble_sort_by_score, tambahkan_peringkat
from src.logic.searching import linear_search_by_name, linear_search_by_score


class TestM8Logic(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"nama": "Rangga", "nilai": 78},
            {"nama": "Sinta", "nilai": 92},
            {"nama": "Budi", "nilai": 65},
            {"nama": "Dewi", "nilai": 88},
        ]

    def test_bubble_sort_descending(self):
        hasil = bubble_sort_by_score(self.data, descending=True)
        nilai_urut = [mhs["nilai"] for mhs in hasil]
        self.assertEqual(nilai_urut, [92, 88, 78, 65])

    def test_bubble_sort_ascending(self):
        hasil = bubble_sort_by_score(self.data, descending=False)
        nilai_urut = [mhs["nilai"] for mhs in hasil]
        self.assertEqual(nilai_urut, [65, 78, 88, 92])

    def test_bubble_sort_tidak_mengubah_data_asli(self):
        bubble_sort_by_score(self.data, descending=True)
        self.assertEqual(self.data[0]["nama"], "Rangga")

    def test_tambahkan_peringkat(self):
        hasil_sort = bubble_sort_by_score(self.data, descending=True)
        hasil_rank = tambahkan_peringkat(hasil_sort)
        self.assertEqual(hasil_rank[0]["peringkat"], 1)
        self.assertEqual(hasil_rank[-1]["peringkat"], len(self.data))

    def test_linear_search_by_name_ditemukan(self):
        hasil = linear_search_by_name(self.data, "sinta")
        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0]["nama"], "Sinta")

    def test_linear_search_by_name_tidak_ditemukan(self):
        hasil = linear_search_by_name(self.data, "zzz")
        self.assertEqual(hasil, [])

    def test_linear_search_by_score(self):
        hasil = linear_search_by_score(self.data, 88)
        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0]["nama"], "Dewi")


if __name__ == "__main__":
    unittest.main()
