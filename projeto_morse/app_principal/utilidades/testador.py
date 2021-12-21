from projeto_morse.app_principal.utilidades.tradutor import Tradutor as t


def main():
    exemplo_texto = 'CESAR E DANILO'
    print(t.encriptar(exemplo_texto))

    exemplo_morse = '-.-. . ... .- .-. / . / -.. .- -. .. .-.. ---'
    print(t.decriptar(exemplo_morse))

if __name__ == '__main__':
    main()