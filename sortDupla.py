
import random

# Out:   "Amanda L", "Amanda M", "Yuri"

alunosS = ["Iara", "Lorenzo"]
alunos = ["Julia", "Nathan", "Thais", "Carlos", "Donderi", "Cabelin", "Allan", "Carioca", "Guilherme", "Roberto", "Paulo"]

random.shuffle(alunos)

if len(alunos) % 2 == 1:
	a, *alunos = alunos
	print(a, end=', ')

while alunos:
	a, b, *alunos = alunos
	print(f'{a}, {b}')