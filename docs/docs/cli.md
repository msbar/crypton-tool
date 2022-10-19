* O CLI conta com comando que permitem o usuário usar o pacote via comandos de terminal.

### Comandos:

* Cria uma chave e printa no terminal.

```
crypton --genkey
```

* Cria uma chave no arquivo token.crypton no path informado.

```
crypton --genkey --to_file path/to/your/token.crypton
``` 

* Encripta o arquivo passado por argumento.

```
crypton --encrypt_file path/to/your/file
``` 

* Decripta o arquivo passado por argumento.

```
crypton --decrypt_file path/to/your/file
``` 

* Encripta o arquivo passado por argumento.

```
crypton --encrypt_content 'seu conteúdo'
``` 

* Decripta o arquivo passado por argumento.

```
crypton --decrypt_content 'seu conteúdo'
``` 