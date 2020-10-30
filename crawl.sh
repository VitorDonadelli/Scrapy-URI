#!/bin/bash
cd scrapy_uri/spiders



for counter in {1..9}; do 
    rm ../../$counter.json
    echo $counter | scrapy crawl exercicios -o ../../$counter.json

done