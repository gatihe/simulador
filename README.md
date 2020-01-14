# Gerador de notas para disciplinas

Este projeto é um Trabalho de Conclusão de Curso para o curso de Sistemas de Informação da Faculdade de Tecnologia da Unicamp. Consiste na criação de um simulador de notas e projeção de cumprimento do currículo escolar de estudantes, baseado nos cursos existentes na Unicamp em 2020.

---
### Instalação
#### Requisitos:
- [Python 3.x](https://www.python.org/download/releases/3.0/)
- [Pandas](https://pandas.pydata.org/)
#### Instruções:
- Faça o download e extração do repositório
- Na raiz do diretório extraído, rode o arquivo `simulador.py`
#### Observações:
- Todas as funcionalidades estão ativas e funcionando corretamente, **apenas cuidado pois o tratamento de erros para inputs manuais ainda não está totalmente implementado**.
- Para importar as configurações de forma mais eficiente o arquivo `config.xml` pode servir de auxílio.
- A simulação gera dois arquivos (html e csv). **Somente com a finalidade de evidenciar o funcionamento do sistema**, os campos preenchidos com 'Fez em outra turma' e 'Faltam prereqs' servem para apontar que as funções de aplicação de pré-requisitos e de disperção de alunos em turmas estão se comportando da forma esperada.
---
### Mais informações
#### Backlog:
 - Configurar prevenção de erro de usuários
 - Encontrar e alterar melhor termo para disciplinas não cursadas por falta de requisitos
 - Encontrar e alterar melhor termo para turmas não cursadas
 - Refatorar o código :grimacing:
 - [Feature] Listagem de quantidade de turmas junto à listagem de disciplinas.
#### Em progresso:
- Configurar prevenção de erro de usuários (previsto 27/01)
- Encontrar e alterar melhor termo para disciplinas não cursadas por falta de requisitos (previsto 27/01)
- Encontrar e alterar melhor termo para turmas não cursadas (previsto 27/01)
- Refatorar o código (previsto 27/01)
#### Feito:
- Importação de configurações em XML.
- Gerar tabela html com distribuição de notas de alunos por disciplina.
- Gerar CSV para exportação da tabela de distribuição de notas.
- Implementar download de arquivo CSV gerado.
- Alunos e funcionalidades.
- Parâmetros e funcionalidades.
- Pré-requisitos e funcionalidades.
---
### Entregas
##### 14/01/2020 - Primeira entrega:

O entregável deste sprint foi um sistema, de interface em linha de comando, baseado nos requisitos acordados na última reunião. Visando basicamente as seguintes questões:
- Quantos alunos serão simulados?
- Quais são as faixas de rendimento dos alunos?
- Quantas disciplinas haverão?
- Quantas turmas haverão nas disciplinas?
- Quais são os pré-requisitos dessas disciplinas?
