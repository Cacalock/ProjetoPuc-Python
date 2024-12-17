# Projeto de Raciocínio Computacional

Este projeto é uma aplicação em Python que utiliza conceitos de organização, manipulação de dados e gerenciamento de listas. Ele permite realizar operações como inclusão, listagem, exclusão, restauração de itens excluídos, e edição de dados relacionados a estudantes, professores, disciplinas, turmas e matrículas.

---

## Estrutura do Projeto

### Classes Principais

1. **Operacoes**
   - Gerencia as listas principais de dados e o armazenamento em arquivo JSON.
   - Funções principais:
     - `carregar_lista()`: Carrega dados do arquivo JSON.
     - `salvar_lista()`: Salva os dados em arquivo JSON.
     - `incluir()`: Adiciona novos registros.
     - `excluir()`: Remove itens das listas e os transfere para um "lixo".
     - `listar()`: Exibe os registros armazenados.
     - `editar()`: Modifica registros existentes.
     - `Lixo()`: Exibe itens excluídos.

2. **Menus**
   - Gerencia a interação com o usuário e os menus principais e secundários.
   - Navega entre as opções de operações para cada categoria de dados.

---

## Funcionalidades

1. **Incluir**:
   - Adiciona novos registros (estudantes, professores, disciplinas, turmas ou matrículas).
   - Realiza validação de entrada para garantir consistência dos dados.

2. **Listar**:
   - Exibe todos os registros cadastrados na categoria selecionada.

3. **Excluir**:
   - Remove registros de forma segura, armazenando-os temporariamente em um "lixo".

4. **Lixo**:
   - Visualiza os itens excluídos para possível recuperação futura.

5. **Editar**:
   - Permite alterações em registros existentes.

6. **Menu Principal**:
   - Organiza as operações em categorias:
     - Estudantes
     - Professores
     - Disciplinas
     - Turmas
     - Matrículas

---

## Requisitos do Sistema

- Python 3.8 ou superior
- Biblioteca padrão (os, time, json, copy)

---

## Como Executar o Projeto

1. Clone o repositório ou copie os arquivos para o seu ambiente local.
2. Certifique-se de que o Python esteja instalado no seu sistema.
3. Execute o script principal:
   ```bash
   python nome_do_arquivo.py
   ```
4. Navegue pelos menus conforme as instruções exibidas no terminal.

---

## Estrutura do Arquivo JSON

Os dados são armazenados em um arquivo chamado `semana8.json`. A estrutura é organizada por categorias:

```json
{
    "1": [{"codigo": 1, "nome": "Estudante A", "cpf": 123456789}],
    "2": [{"codigo": 1, "nome": "Professor B", "cpf": 987654321}],
    "3": [{"codigo": 1, "nome": "Disciplina C"}],
    "4": [{"codigo": 1, "disciplina": "1", "professor": "1"}],
    "5": [{"codigo": 1, "turma": "1", "estudante": "1"}]
}
```

---

## Personalização

- **Editor de Texto**: O editor padrão utilizado é o sistema de terminal.
- **Mensagens e Layout**: Todas as mensagens e menus são customizáveis no código.

---

## Licença

Este projeto é distribuído sob a licença MIT. 

