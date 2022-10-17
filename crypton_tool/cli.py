import argparse
from pathlib import Path

from crypton import Crypton
from logger import logger

parser = argparse.ArgumentParser()

parser.add_argument("--encrypt_file", help="Encripta o arquivo passado por argumento.")
parser.add_argument("--decrypt_file", help="Decripta o arquivo passado por argumento.")
parser.add_argument("--encrypt_content", help="Encripta o arquivo passado por argumento.")
parser.add_argument("--decrypt_content", help="Decripta o arquivo passado por argumento.")
parser.add_argument("--genkey", action="store_true", help="Gera chave aleatória")
parser.add_argument("--to_file", action="store_true", help="Gera chave aleatória e salva em arquivo")

args = parser.parse_args()

log = logger().getLogger('manage.py')
CRYPTON_TOKEN = Path('token.crypton').read_bytes()


def crypton():

    crypt = Crypton(CRYPTON_TOKEN)
    if args.encrypt_file:
        crypt.encrypt_file(args.encrypt_file)
    elif args.decrypt_file:
        crypt.decrypt_file(args.decrypt_file)
    elif args.encrypt_content:
        print(crypt.encrypt_content(args.encrypt_content))
    elif args.decrypt_content:
        print(crypt.decrypt_content(args.decrypt_content))
    elif args.genkey:
        if args.to_file:
            Crypton.generate_key(to_file=args.to_file)
            print(Crypton.read_token_file('token.crypton'))
        else:
            print(Crypton.generate_key())
    else:
        log.info(f'Este comando não é um comando do Crypon.')


if __name__ == '__main__':
    crypton()
