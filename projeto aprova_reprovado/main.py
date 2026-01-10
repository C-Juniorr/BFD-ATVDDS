alunos = [
    {"nome": "Ana", "nota": 7.5, "frequencia": 80},
    {"nome": "Bruno", "nota": 6, "frequencia": 70},
    {"nome": "Ana", "nota": 4.5, "frequencia": 90},
]

for aluno in alunos:
    nota = aluno["nota"]
    freq = aluno["frequencia"]
    
    if nota >= 7 and freq >= 75:
        print(f"ALUNO APROVADO: {aluno['nome']}")
    elif nota >= 5:
        print(f"Aluno em recuperacao: {aluno["nome"]}")
    else:
        print(f"Aluno Reprovado: {aluno["nome"]}")