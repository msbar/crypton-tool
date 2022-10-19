* Documentação de como usar o objeto Crypton nos seus projetos.

### Impotando a Classe.
```Python linenums="1"
from crypton_tool.crypton import Crypton
```

### Gerando uma Chave.
* generate_key é um método de classe que gera a chave token para criptografar os conteúdos.


```Python linenums="1"
Crypton.generate_key()

```

* Se um path for passado como parâmetro to_file o método vai gerar a chave em no arquivo token.crypton no caminho informado.

```Python linenums="1"
Crypton.generate_key(to_file='seu/caminho')

```

### Lendo uma chave do arquivo token.crypton.
```Python linenums="1"
Crypton.read_token_file("seu/caminho/token.crypton")
```

### Instanciando a classe Crypton.
```Python linenums="1"
from crypton_tool.crypton import Crypton

token = Crypton.read_token_file("seu/caminho/token.crypton")
crypton = Crypton(token)
```

### Criptando um arquivo ou arquivos em uma pasta.
```Python linenums="1"
crypt.encrypt_file('caminho/para/arquivo_ou_pasta')
```

### Decriptando um arquivo ou arquivos em uma pasta.
```Python linenums="1"
crypt.decrypt_file('caminho/para/arquivo_ou_pasta')
```
