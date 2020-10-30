
import random

alunosS = ["Iara", "Thais"]
alunos = ["Carlos", "Donderi", "Carioca", "Cabelin", "Allan", "Amanda M", "Amanda L", "Guilherme", "Paulo", "Roberto", "Yuri"]
random.shuffle(alunos)

if len(alunos) % 2 == 1:
	a, *alunos = alunos
	print(a, end=', ')

while alunos:
	a, b, *alunos = alunos
	print(f'{a}, {b}')