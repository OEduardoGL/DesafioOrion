# DesafioOrion

Nossa solução propõe um Data Lake lógico estruturado em três camadas:

### Camada `Raw`
Aqui são inseridos os dados brutos, podendo conter diversas pastas com arquivos em formatos distintos.

### Camada `Staging`
Após a execução do script `monitor.sh`, todos os arquivos armazenados em `Raw` são transferidos para esta camada. Nela, cada arquivo é alocado em seu respectivo diretório de formato (csv, html, xml ou json).

### Camada `Clean`
Depois de executados os scripts de transformação (PySpark), todos os arquivos em `Staging` são transformados para o modelo JSON. Os arquivos resultantes são então armazenados nesta camada, alcançando o objetivo final do processamento.

![orion](https://github.com/user-attachments/assets/f21e5f47-ea11-439a-9960-eaed664a610d)

## Tecnologias Utilizadas

Optamos por utilizar HDFS (Hadoop) e Spark para garantir o processamento de maneira distribuída e escalável, permitindo o trabalho com grande volume de dados de forma eficiente.

## Considerações Finais

Nosso foco foi desenvolver uma solução robusta para o problema proposto, com espaço para futuras melhorias, como a automatização dos scripts.

Para um guia detalhado de execução da nossa solução, consulte o arquivo `tutorial`.

## Equipe

- Eduardo Gomes
- Vítor Magno
- Eliane Laís
