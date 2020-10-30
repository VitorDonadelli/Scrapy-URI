# Scrapy-URI

A ideia desse repositório é criar um web scrapy que varre uma categoria (ou todas) de exercicios do [URI](https://www.urionlinejudge.com.br/judge/pt/categories) utilizando [Scrapy](https://scrapy.org/) para gerar um arquivo JSON com o número do exercício seguido da dificuldade do mesmo.

Também nesse repositório existe scripts em python para filtrar e ordenar os exercícios.

## Etapas:

Percorrer uma página coletando informações: *Done*

Percorrer uma categoria coletando informações: *Done*

Seletor de categorias: *Done*

### Organização de informações

Conseguir Listar: *Done*

Fazer filtros: *Done* 


## Tecnologias empregadas:

* Scrapy
* Python
* Precisa de um pouco de conhecimento de HTML + CSS

# Como utilizar:

Instalação do scrapy: [Scrapy Download](https://scrapy.org/download/)

        pip install scrapy


Para utilizar o crawl em apenas uma categoria:

        cd scrapy_uri/spiders
        scrapy crawl exercicios -o ../../nome.json

#### Para utilizar o script de organização, substituir "nome.json" pelo número da categoria que está acontecendo o scrapy, por exemplo, se há interesse em crawlar o Iniciante o arquivo deve ser nomeado como "1.json", lembrando que é necessário o ../../ para armazená-los na raiz do projeto.

Para pegar todas as categorias de uma vez e deixa-los na forma ideal para o script de organização, rode o shell script:

        chmod +x crawl.sh
        ./crawl.sh

Isso irá criar arquivos ".json" na base do projeto, numerados de 1 a 9. Para organizá-los há outros 2 scripts: `organizar.py` e `sem_menus.py`

organizar.py: Alguns menus interativos para selecionar categoria, forma de ordenação, etc.

        python3 organizar.py

sem_menus.py: Requer alterações no código para utilizar redirecionamento de saída.

        python3 sem_menus.py > saida.txt


