class Tradutor:
    TEXTO_PARA_MORSE = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.', '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', ' ': '/', 'Á': '.--.-', 'É':'..-..', ':': '---...', ';': '-.-.-', "'": '.----.'}

    MORSE_PARA_TEXTO = {v: k for k, v in TEXTO_PARA_MORSE.items()}

    @classmethod
    def encriptar(cls, texto):
        '''
        Recebe uma string de texto e retorna a string traduzida para código morse
        '''
        return ''.join(cls.TEXTO_PARA_MORSE[caractere.upper()] + ' ' for caractere in texto)

    @classmethod
    def decriptar(cls, morse):
        '''
        Recebe uma string de código morse e retorna a string traduzida para texto
        '''
        return ''.join(cls.MORSE_PARA_TEXTO[caractere.upper()] for caractere in morse.split(' '))
        