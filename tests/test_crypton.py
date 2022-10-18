import base64
from pathlib import Path

from crypton_tool.crypton import Crypton

BASE_DIR_TEST = Path(__file__).resolve().parent
DECRYPTED_FILE_TEST = BASE_DIR_TEST / "decrypted_file_test"
ENCRYPTED_FILE_TEST = BASE_DIR_TEST / "encrypted_file_test"
TOKEN_CRYPTON = BASE_DIR_TEST / "token.crypton"
KEY = b"CJSgfXb23iXqTJLzwmWwTf-Wu6VWBFNMWXZObWdXaTE="
CRYPT = Crypton(KEY)


def test_generate_key_is_not_none():
    """Testa se função generate key retorna diferente de None."""
    key = Crypton.generate_key()
    assert key is not None


def test_generate_key_size():
    """Testa se tamanho da chave é igual a 32 bytes."""
    key = base64.urlsafe_b64decode(Crypton.generate_key())
    assert len(key) == 32


def test_generate_key_to_file():
    """Testa criação de arquivo token.crypton"""
    Crypton.generate_key(BASE_DIR_TEST)
    assert Path(TOKEN_CRYPTON).exists()


def test_read_token_file():
    """Testa a leitura do arquivo token.crypton"""
    key = base64.urlsafe_b64decode(Crypton.read_token_file(TOKEN_CRYPTON))
    assert len(key) == 32


def test_path_handler_string():
    """Testa handler file passando o path como string"""
    assert isinstance(CRYPT.path_handler("."), list)


def test_path_handler_path():
    """Testa handler file passando o path como instância do Path"""
    assert isinstance(CRYPT.path_handler(BASE_DIR_TEST)[0], Path)


def test_encrypt_file():
    """Testa a encryptação do arquivo decrypted_file_test"""
    CRYPT.encrypt_file(DECRYPTED_FILE_TEST)
    file_content = DECRYPTED_FILE_TEST.read_text()
    assert file_content != "teste crypton"
    CRYPT.decrypt_file(DECRYPTED_FILE_TEST)


def test_decrypt_file():
    """Testa a decryptação do arquivo encrypted_file_test"""
    CRYPT.decrypt_file(ENCRYPTED_FILE_TEST)
    file_content = ENCRYPTED_FILE_TEST.read_text()
    assert file_content == "teste crypton"
    CRYPT.encrypt_file(ENCRYPTED_FILE_TEST)


def test_encrypt_content():
    """Testa a encryptação do arquivo decrypted_file_test"""
    content = "Texto em string"
    content_encrypted = CRYPT.encrypt_content(content)
    assert content != content_encrypted


def test_decrypt_content():
    """Testa a encryptação do arquivo decrypted_file_test"""
    content = "Texto em string"
    content_encrypted = "gAAAAABjTr8RM4tXSFThDT1a2TcSUiJz7Z4Q5jI98QF4D3LpbEl85bSsGD8TbmdVhYFhV6cohDYO5OsfJEdC7q5N9LXWprJX9Q=="
    content_decrypted = CRYPT.decrypt_content(content_encrypted)
    assert content == content_decrypted
