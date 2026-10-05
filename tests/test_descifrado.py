import unittest
from descifrar import calcular_frecuencias, crear_mapa_sustitucion, descifrar_texto


class TestCriptoanalisis(unittest.TestCase):
    def test_calcular_frecuencias(self):
        texto = "aaaa bbb cc d"
        freqs = calcular_frecuencias(texto)
        self.assertAlmostEqual(freqs['a'], 40.0, places=1)
        self.assertAlmostEqual(freqs['b'], 30.0, places=1)
        self.assertAlmostEqual(freqs['c'], 20.0, places=1)
        self.assertAlmostEqual(freqs['d'], 10.0, places=1)

    def test_descifrar_texto_simple(self):
        mapa = {'x': 'h', 'y': 'o', 'z': 'l', 'w': 'a'}
        texto_cifrado = "Xyzw!"
        resultado = descifrar_texto(texto_cifrado, mapa, preservar_mayusculas=True)
        self.assertEqual(resultado, "Hola!")

    def test_crear_mapa_con_manuales(self):
        texto = "zzzzz yyyy xxxx"
        manuales = {'z': 'a'}  # Forzamos que 'z' sea 'a' a pesar de que 'e' sea la más frecuente
        mapa = crear_mapa_sustitucion(texto, manuales=manuales)
        self.assertEqual(mapa['z'], 'a')
        # La siguiente letra más frecuente ('y') debería mapear a 'e' (máxima freq no usada)
        self.assertEqual(mapa['y'], 'e')


if __name__ == '__main__':
    unittest.main()
