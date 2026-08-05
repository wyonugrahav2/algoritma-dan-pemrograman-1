import unittest
from src.logic.geometry_2d import (
    luas_persegi,
    keliling_persegi,
    luas_persegi_panjang,
    luas_segitiga,
    luas_lingkaran,
    keliling_lingkaran,
)
from src.logic.geometry_3d import (
    volume_kubus,
    volume_balok,
    volume_tabung,
    volume_bola,
)
from src.utils.stats_utils import rata_rata, nilai_tertinggi, ringkasan_hasil


class TestM10Logic(unittest.TestCase):

    def test_geometri_2d(self):
        self.assertEqual(luas_persegi(4), 16)
        self.assertEqual(keliling_persegi(4), 16)
        self.assertEqual(luas_persegi_panjang(5, 3), 15)
        self.assertEqual(luas_segitiga(6, 4), 12.0)
        self.assertAlmostEqual(luas_lingkaran(2), 3.14 * 4)
        self.assertAlmostEqual(keliling_lingkaran(2), 2 * 3.14 * 2)

    def test_geometri_2d_default_phi_bisa_diganti(self):
        # Menguji bahwa default parameter phi tetap bisa dioverride
        self.assertAlmostEqual(luas_lingkaran(2, phi=3.14159), 3.14159 * 4)

    def test_geometri_3d(self):
        self.assertEqual(volume_kubus(3), 27)
        self.assertEqual(volume_balok(2, 3, 4), 24)
        self.assertAlmostEqual(volume_tabung(2, 5), 3.14 * 4 * 5)
        self.assertAlmostEqual(volume_bola(3), (4 / 3) * 3.14 * 27)

    def test_rata_rata_args(self):
        self.assertEqual(rata_rata(10, 20, 30), 20)
        self.assertEqual(rata_rata(), 0)

    def test_nilai_tertinggi_args(self):
        self.assertEqual(nilai_tertinggi(10, 50, 30), 50)

    def test_ringkasan_hasil_kwargs(self):
        ringkasan = ringkasan_hasil(luas_persegi=16, volume_kubus=27, luas_segitiga=12)
        self.assertEqual(ringkasan["jumlah_data"], 3)
        self.assertEqual(ringkasan["label_tertinggi"], "volume_kubus")
        self.assertAlmostEqual(ringkasan["rata_rata"], (16 + 27 + 12) / 3)

    def test_ringkasan_hasil_kosong(self):
        ringkasan = ringkasan_hasil()
        self.assertEqual(ringkasan["jumlah_data"], 0)


if __name__ == "__main__":
    unittest.main()
