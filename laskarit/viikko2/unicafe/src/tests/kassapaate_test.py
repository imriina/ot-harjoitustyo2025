import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(10000)

    def test_onko_oikee_raha(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

#edullisen jutut

    def test_lisaako_kassaan_edu(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100240)
    
    def test_ei_lisaa_kassaan_edu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)

    def test_edullinen_kateisosto(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kateisella(500)), 260)

    def test_edu_kateis_ei_saldoa(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kateisella(100)), 100)

    def test_edullinen_kateisosto_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual((self.kassapaate.edulliset), 1)

    def test_edu_kateis_maara_jos_ei_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual((self.kassapaate.edulliset), 0)
    
    #kortti jutut

    def test_veloitetaan_edu_kortilta_on_saldo(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kortilla(self.kortti)), True)

    def test_ei_veloiteta_edu_ei_saldo(self):
        self.kortti = Maksukortti(100)
        self.assertEqual((self.kassapaate.syo_edullisesti_kortilla(self.kortti)), False)

    def test_lahteeko_raha_edu_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual((self.kortti.saldo), 9760)

    def test_ei_lahde_edu_kortilta_ei_saldo(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual((self.kortti.saldo), 100)
    
    def test_lisaantuuko_mau_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual((self.kassapaate.edulliset), 1)

    def test_edu_ei_lisaanny_kun_kortti_ei_saldo(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual((self.kassapaate.edulliset), 0)

        

#maukkaan jutut

    def test_lisaako_kassaan_mau(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100400)

    def test_ei_lisaa_kassaan_mau(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)

    def test_maukas_kateisosto(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kateisella(500)), 100)

    def test_mau_kateis_ei_saldoa(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kateisella(100)), 100)

    def test_maukas_kateisosto_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual((self.kassapaate.maukkaat), 1)

    def test_mau_kateis_maara_jos_ei_saldoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual((self.kassapaate.maukkaat), 0)

    #kortti osa 

    def test_veloitetaan_mau_kortilta_on_saldo(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kortilla(self.kortti)), True)

    def test_ei_veloiteta_mau_ei_saldo(self):
        self.kortti = Maksukortti(100)
        self.assertEqual((self.kassapaate.syo_maukkaasti_kortilla(self.kortti)), False)

    def test_lahteeko_raha_mau_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual((self.kortti.saldo), 9600)

    def test_ei_lahde_mau_kortilta_ei_saldo(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual((self.kortti.saldo), 100)
    
    def test_lisaantuuko_mau_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual((self.kassapaate.maukkaat), 1)

    def test_mau_ei_lisaanny_kun_kortti_ei_saldo(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual((self.kassapaate.maukkaat), 0)

#    def test_veloitetaan_mau_kortilta_ei_saldo1(self):
#       self.assertNotEqual((self.kassapaate.syo_maukkaasti_kortilla(self.kortti)), False)

    def test_lataa_rahaa_kortilta(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 10000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 110000)
        self.assertEqual((self.kortti.saldo), 20000)

    def test_ladataan_neg_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)
        self.assertEqual((self.kortti.saldo), 10000)