# organiza_pastas
## Organizador de Pastas para Professores

Este programa foi desenvolvido para ajudar professores a organizar suas pastas e subpastas de forma padronizada e eficiente. Ele cria uma estrutura de diretórios com base em informações fornecidas como:
    nome da escola, 
    ano de vigência, 
    ciclo, 
    disciplina, 
    turma
    número de aulas. 

Ideal para quem busca praticidade na gestão de materiais didáticos digitais.

Funcionalidades
Automatização: Cria automaticamente pastas e subpastas com base em padrões definidos pelo usuário.
Personalização: Permite configurar parâmetros como:
Nome da escola
Ano letivo
Ciclo
Disciplina
Letra da classe (turma)
Quantidade de aulas (usado para subpastas específicas)
Interface Simples: Utiliza comandos no terminal para facilitar o uso em diferentes sistemas operacionais.
Requisitos
Python 3.x instalado
Compatível com Windows, macOS e Linux
Como Usar
Clone o repositório para sua máquina local.
Execute o programa no terminal com o comando:
bash
Copiar código
python organizador_pastas.py
Siga as instruções fornecidas pelo programa para inserir as informações necessárias.
Exemplo de Estrutura Gerada
Para os parâmetros:

Escola: Colégio Exemplo
Ano de Vigência: 2024
Ciclo: Ensino Fundamental II
Disciplina: Matemática
Turma: 7A
Número de Aulas: 5
O programa criará a seguinte estrutura:

Copiar código

Colégio Exemplo/
├── 2024/
    ├── Ensino Fundamental II/
        ├── Matemática/
            ├── 7A/
                ├── Aula 1/
                ├── Aula 2/
                ├── Aula 3/
                ├── Aula 4/
                ├── Aula 5/
Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto está licenciado sob a MIT License.