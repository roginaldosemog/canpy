# Canpy: Interpretador Canva em Python

Canva é uma linguagem de programação inspirada no Canva, ferramenta de criação de imagens.
Canpy é o interpretador em Python da linguagem Canva.

## Instalação

Para rodar o projeto, é necessário que você tenha Python 3 e pip instalados em sua máquina.

Após a instalação do Python 3 e do pip, rode os seguintes comandos:

```bash
git clone https://github.com/roginaldosemog/canpy.git
cd canpy
python3 -m pip install -r requirements.txt --user
```

## Utilização

Para criar sua própria arte, substitua as imagens na pasta ```img/``` conforme os exemplos, já inseridos na pasta.

### Exemplo 1

Para criar uma imagem para feed, siga os seguintes passos:

1. Coloque a imagem de preferência, na pasta ```ìmg/``` com o nome ```background```. Ficando ```img/background.jpg``` ou ```img/background.png```

2. Altere o código do arquivo ```canva.cnv```, para o que for mais conveniente. Ex:  
```
feed:
    name: 'nome_do_post'
    background: 'img/background.jpg'
```