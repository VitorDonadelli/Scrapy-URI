import scrapy

class WebScrapy(scrapy.Spider):
    name = 'exercicios' #Usado em: $ scrapy crawl name -o saida.json
    i = int(input(
            "Qual categoria quer fazer o crawl?\n[1] - Iniciante\n[2] - AD-HOC\n[3] - Strings\n[4] - Estruturas e Bibliotecas\n[5] - Matemática\n[6] - Paradigmas\n[7] - Grafos\n[8] - Geometria Computacional\n[9] - SQL\n"))

    url_inicial = 'https://www.urionlinejudge.com.br/judge/pt/problems/index/'
    
    start_urls = [
        url_inicial + str(i)
    ]

    def parse(self, response):
        exercicios = response.css('#element .id a::text').getall() 
        dificuldade = response.css('.small+ .tiny::text').getall() 

        result = []
        for i in range(0,len(exercicios)):
            result.append(exercicios[i])
            result.append(dificuldade[i])
        

        yield {
            'Exercicios': result
        }
        
        next_page = response.css('.next a::attr(href)').get()
    
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)