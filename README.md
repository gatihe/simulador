# Gerador de notas para disciplinas

Este projeto é um Trabalho de Conclusão de Curso para o curso de Sistemas de Informação da Faculdade de Tecnologia da Unicamp. Este projeto objetiva gerar e adaptar conjuntos de dados para dois sistemas de mineração de dados educacionais em elaboração na Faculdade de Tecnologia da UNICAMP. O primeiro sistema é um visualizador de conjuntos de históricos escolares. O foco deste trabalho é desenvolver um gerador de conjuntos de históricos escolares simulados.
Esses conjuntos devem ter características programáveis, como por exemplo padrões específicos que se deseja que sejam possíveis de visualizar, e que serão derivadas de demandas de análise de dados já informadas por coordenadores de curso de graduação.

##### Áreas do conhecimento envolvidas no trabalho:
- Visualização da Informação
- Mineração de dados educacionais
---
#### Requisitos:
- [Python 3.x](https://www.python.org/download/releases/3.0/)
- [Pandas](https://pandas.pydata.org/)
#### Instruções:
- Faça o download e extração do repositório
- Na raiz do diretório extraído, execute o arquivo `simulador.py`
---
#### Catálogos:

Entre as configurações que dão suporte à simulação de dados educacionais estão os catálogos de curso. Este arquivo tem como utilidade especificar as características do curso à ser simulado. Conta com a seguinte estrutura:

```
<all_configs>
	<cat_info>
		<course_id><ID_CURSO></course_id>
		<year><ANO_DO_CATALOGO></year>
		<max_years><TEMPO_MAXIMO_DE_DURACAO></max_years>
	</cat_info>
	<subjects>
		<subject>
			<id><ID_DISCIPLINA></id>
			<subject_name><NOME_DISCIPLINA></subject_name>
			<credits><QTDE_DE_CREDITOS></credits>
			<sem_offer><SEMESTRE_DE_OFERTA></sem_offer>
			<classes_no><NUMERO DE TURMAS></classes_no>
			<tipo_nivel_atividade_mae><NIVEL_ATIVIDADE_DA_DISCIPLINA></tipo_nivel_atividade_mae>
			<pre_reqs><PRE_REQUISITO></pre_reqs>
			<ano_inicio><ANO_DE_INICIO_DE_VIGENCIA_DO_PREREQ></ano_inicio>
			<ano_fim><ANO_DO_FIM_DE_VIGENCIA_DO_PREREQ></ano_fim>
			<no_cadeia_pre_requisito><NUM_CADEIA_DE_PRE_REQUISITOS></no_cadeia_pre_requisito>
			<tipo_pre_requisito><TIPO_PRE_REQUISITO></tipo_pre_requisito>
			<tipo_nivel_atividade_exigida><NIVEL_ATIVIDADE_EXIGIDA></tipo_nivel_atividade_exigida>
		</subject>
<all_configs>
```
