---

# ✅ **README.md – Mistério da Mansão em São José dos Pinhais**

```markdown
# 🕵️‍♂️ Mistério da Mansão em São José dos Pinhais
Projeto acadêmico — Jogo de Detetive com Lógica Proposicional  
Curso: Ciência da Computação – 1º Período  
Disciplina: Lógica  


---

## 🎯 Objetivo do Projeto
O objetivo deste trabalho é desenvolver um **jogo de detetive** utilizando:

- Regras de inferência  
- Pistas verdadeiras, falsas e indeterminadas  
- Deduções lógicas  
- Recursividade  
- Interação simples via terminal  

O jogador deve descobrir:

1. **Quem matou Álvaro Mello**  
2. **Qual foi a arma usada**  
3. **Em qual local ocorreu o crime**

---

## 📜 Contexto Narrativo
A história se passa em uma antiga mansão localizada em São José dos Pinhais.  
Durante uma tempestade, o empresário **Álvaro Mello** é encontrado morto em seu escritório, trancado por dentro.  

O detetive **Rafael Costa** assume o caso e precisa investigar:

- **Dra. Camila Mello** – filha da vítima  
- **Renato Borges** – caseiro  
- **Dona Lúcia** – governanta  
- **Eduardo Lima** – artista hospedado na mansão  

O jogador deve interpretar o detetive, analisando pistas e deduzindo a verdade — lembrando que **nem todas as pistas são confiáveis.**

---

## 🧩 Pistas Utilizadas
Cada pista pode ser:

- ✅ Verdadeira  
- ❌ Falsa  
- ❔ Indeterminada  

| Código | Pista | Tipo |
|-------|-------|------|
| P1 | A porta do escritório estava trancada. | ✅ |
| P2 | Passos foram ouvidos na biblioteca. | ✅ |
| P3 | Renato discutiu com Álvaro pela manhã. | ✅ |
| P4 | A arma foi um castiçal. | ✅ |
| P7 | Renato estava no escritório na hora do crime. | ❌ |
| P8 | Camila estava dormindo durante o crime. | ❌ |
| P10 | Pegadas molhadas no corredor. | ❔ |
| P12 | O castiçal tinha digitais de duas pessoas. | ❔ |

---

## 🧠 Sistema de Deduções
O jogo gera deduções automáticas de acordo com as pistas usadas pelo jogador.

Exemplos implementados:

- P1 + P2 → **Alguém pode ter usado passagem secreta.**  
- P8 + P3 → **Camila mentiu e tinha motivo.**  
- P4 → **A arma foi o castiçal.**

Essas deduções guiam o jogador até a conclusão final.

---

## 🔎 Acertos Parciais
Ao tentar resolver o caso, o sistema mostra:

- Se o culpado está correto  
- Se a arma está correta  
- Se o local está correto  
- Total de acertos: 0/3, 1/3, 2/3 ou 3/3  

O jogador **só vence** quando atinge **3/3**.

Exemplo:

```

✔ Culpado correto!
✘ Arma incorreta.
✔ Local correto.

Acertos totais: 2/3
Continue investigando...

```

---

## 🧬 Recursividade
O jogo **não usa while** nem **loops tradicionais**.

A função `menu()` chama ela mesma ao final, mantendo o jogo ativo até:

- O jogador vencer  
- O jogador digitar **sair**

Isso atende ao requisito da disciplina.

---

## 🕹️ Como Jogar
Comandos disponíveis:

| Comando | Função |
|---------|--------|
| `pistas` | Mostra todas as pistas disponíveis |
| `usar P?` | Usa uma pista (ex: `usar P4`) |
| `revelar P?` | Revela se é verdadeira, falsa ou indeterminada |
| `deduzir` | Mostra deduções baseadas nas pistas usadas |
| `responder` | Tenta resolver o caso |
| `sair` | Encerra o jogo |

### Exemplo de jogo:
```

pistas
usar P1
usar P2
deduzir
responder

```

---

## 🧾 Solução Correta (Gabarito Interno do Jogo)

- **Culpado:** Camila  
- **Arma:** Castiçal  
- **Local:** Escritório  

---

## 💾 Como Executar

### Requisitos
- Python 3 instalado

### Execução
1. Baixe o arquivo `jogo_mansao.py`
2. Abra o terminal na pasta do arquivo
3. Execute:

```

python jogo_mansao.py

```




