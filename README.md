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
- Faça o download e extração do repositório;
- Na raiz do diretório extraído, execute o arquivo `simulador.py`;
- Importe um catálogo e, se necessário, configurações adicionais;
- Faça uma simulaçao;
- Exporte os relatórios.
---
#### Catálogos (.xml):

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
- `<cat_info>`: Agrupa informações referentes ao catálogo;
- `<course_id>`: Identificador único do curso à ser simulado (int);
- `<year>`: Ano do catálogo (int);
- `<max_years>`: Tempo máximo que os alunos tem para concluir o curso (int);
- `<subjects>`:  Agrupa todas as disciplinas;
- `<subject>`: Agrupa informações referentes à uma disciplina;
- `<id>`: Identificador único da disciplina a ser simulada (int);
- `<subject_name>`: Nome da disciplina (string);
- `<credits>`: Quantidade de créditos referentes à disciplina (int);
- `<sem_offer>`: Semestre em que a disciplina é ofertada aos alunos (int);
- `<classes_no>`: Quantidade de turmas em paralelo na oferta (int);
- `<tipo_nivel_atividade_mae>`: Natureza da disciplina, pode ser 'G' para se referir à graduação, 'P' para pós-graduação ou qualquer outro valor desejado (chr);
- `<pre_reqs>`: Identificador único da disciplina que seja pré-requisito da disciplina em questão. Mesmo que não haja algum pré-requisito, é necessário ao menos uma instância dessa tag por disciplina (string ou vazio caso não haja). Para disciplinas com mais de um pré-requisito, repetir em ordem correta esta tag e as tags abaixo;
- `<ano_inicio>`: Ano em que se iniciou a vigência do pré-requisito em questão. Mesmo que não haja algum pré-requisito, é necessário ao menos uma instância dessa tag por disciplina (int ou vazio caso não haja);
- `<ano_fim>`: Ano em que se encerrou a vigência do pré-requisito em questão ('0' caso vigência do pré-requisito ainda não tenha encerrado). Mesmo que não haja algum pré-requisito, é necessário ao menos uma instância dessa tag por disciplina (int ou vazio caso não haja);
- `<no_cadeia_pre_requisito>`: Identificador único da cadeia de requisitos à qual este pré-requisito pertence (int);
- `<tipo_pre_requisito>`: O tipo de pré-requisito definirá se para cursar a disciplina, o aluno deve ter passado no pré-requisito ou ao menos cursado ('FORTE' para disciplinas que exigem aprovação no pré-requisito, 'FRACO' para disciplinas que exigem somente matrícula anterior na disciplina);
- `<tipo_nivel_atividade_exigida>`: Natureza do pré-requisito, pode ser 'G' para se referir à graduação, 'P' para pós-graduação ou qualquer outro valor desejado (chr).

#### Configurações adicionais (.xml):

É possível adicionar configurações adicionais para adaptar o comportamento do simulador. Segue estrutura de um arquivo de configurações adicionais:

```
<all_configs>
  <generic_info>
    <ano_ingresso>ANO_DE_INGRESSO</ano_ingresso>
  </generic_info>
  <parameters>
    <parameter>
      <parameter_name>NOME_PARAMETRO</parameter_name>
      <min_grade>NOTA_MINIMA</min_grade>
      <max_grade>NOTA_MAXIMA</max_grade>
      <qtde>QTDE_ALUNOS</qtde>
    </parameter>
  </parameters>
  <factors>
    <easy_pass_factor>FATOR_FACILITADOR</easy_pass_factor>
    <hard_pass_factor>FATOR_DESFAVORÁVEL</hard_pass_factor>
  </factors>
  <subj_dificulty>
    <hard_pass>
      <sub_id>ID_DISCIPLINA</sub_id>
    </hard_pass>
    <easy_pass>
      <sub_id>ID_DISCIPLINA</sub_id>
    </easy_pass>
  </subj_dificulty>
</all_configs>
```
- `<all_configs>`:
- `<generic_info>`:
- `<ano_ingresso>`:
- `<parameters>`:
- `<parameter>`:
- `<parameter_name>`:
- `<min_grade>`:
- `<max_grade>`:
- `<qtde>`:
- `<factors>`:
- `<easy_pass_factor>`:
- `<hard_pass_factor>`:
- `<subj_dificulty>`:
- `<hard_pass>`:
- `<easy_pass>`:
- `<sub_id>`:
