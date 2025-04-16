# Guia de Nomenclatura de Branches e Boas Práticas

## Por que um Guia?

Manter um padrão consistente na nomenclatura de branches é crucial quando trabalhamos em projetos, especialmente em equipe (mesmo que a equipe seja só você no futuro!). Isso torna o histórico do Git mais legível, facilita a automação e ajuda a entender rapidamente o propósito de cada branch. Este guia adota uma convenção comum, alinhada com práticas como o Git Flow.

Além disso, vamos reforçar a importância de escrever código, comentários e nomes de branches/commits em **Inglês**.

## A Convenção de Nomenclatura: `tipo/descricao-curta`

Vamos adotar o seguinte padrão para nomear todas as novas branches (exceto as principais como `main` ou `develop`):

"tipo/descricao_curta"

**De modo que:**

1.  **`tipo`**: Indica a **natureza** ou o **propósito** do trabalho sendo realizado na branch. Deve ser uma das seguintes categorias (em minúsculas):
    *   **`feat`**: Para o desenvolvimento de uma **nova funcionalidade** (feature) para o usuário final.
        *   *Exemplo:* `feat/add-player-inventory`
    *   **`fix`**: Para a **correção de um bug** em produção ou em uma funcionalidade existente.
        *   *Exemplo:* `fix/prevent-item-duplication-on-drop`
    *   **`chore`**: Para tarefas de **manutenção** que não alteram o código de produção diretamente (ex: atualização de dependências, configuração de build, ajustes de ferramentas).
        *   *Exemplo:* `chore/update-python-dependencies`
    *   **`refactor`**: Para **refatoração de código** que não corrige um bug nem adiciona uma funcionalidade (melhora a estrutura, performance, legibilidade).
        *   *Exemplo:* `refactor/simplify-command-parser-logic`
    *   **`docs`**: Para adicionar ou atualizar a **documentação** do projeto.
        *   *Exemplo:* `docs/explain-world-json-format`
    *   **`test`**: Para adicionar ou refatorar **testes** automatizados.
        *   *Exemplo:* `test/add-tests-for-item-interaction`
    *   **`style`**: Para aplicar **ajustes de formatação** de código (espaços, ponto e vírgula, etc., geralmente via linters).
        *   *Exemplo:* `style/apply-black-formatter`

2.  **`/`**: Um separador literal entre o tipo e a descrição.

3.  **`descricao-curta-em-ingles`**: Uma descrição breve e significativa do que está sendo feito na branch. Siga estas regras:
    *   **Use Inglês:** Pela razão explicada abaixo.
    *   **Tudo em minúsculas:** `add-player-inventory` (bom) vs `Add-Player-Inventory` (ruim).
    *   **Use hífens (`-`)** para separar palavras: `add-player-inventory` (bom) vs `add_player_inventory` ou `add player inventory` (ruim).
    *   **Seja conciso, mas claro:** Outra pessoa (ou você no futuro) deve entender o propósito da branch lendo seu nome.
    *   **Evite caracteres especiais:** Além do hífen.

## A Importância de Usar Inglês no Código e Nomes

Mesmo que estejamos aprendendo em português, adotar o inglês para nomes de variáveis, funções, classes, comentários, mensagens de commit e nomes de branches é uma **prática profissional essencial** por várias razões:

1.  **Internacionalização e Colaboração:** O inglês é a língua franca da programação. Seu código poderá ser lido, entendido e mantido por desenvolvedores de qualquer lugar do mundo. Se você for trabalhar em projetos open-source ou em empresas com equipes globais, isso é indispensável.
2.  **Consistência com Ferramentas e Bibliotecas:** A vasta maioria das linguagens de programação, bibliotecas, frameworks e documentações técnicas está em inglês. Manter seu próprio código em inglês cria um ambiente mais coeso e evita a mistura de idiomas, que pode ser confusa.
3.  **Facilidade de Pesquisa:** É muito mais fácil encontrar soluções para problemas, exemplos de código e discussões em fóruns (como Stack Overflow) pesquisando termos técnicos em inglês.
4.  **Profissionalismo:** Demonstra que você está alinhado com as convenções e práticas da indústria de desenvolvimento de software.

**Exemplo Prático:**

*   **Ruim (Português):** `feat/adicionar-inventario-jogador`, `variavel_contador = 0`, `// Verifica se o item é pegável`
*   **Bom (Inglês):** `feat/add-player-inventory`, `item_counter = 0`, `// Check if the item is portable`

## Resumo

*   Nomeie suas branches usando `tipo/descricao-curta-em-ingles`.
*   Escolha o `tipo` correto (`feat`, `fix`, `chore`, `refactor`, `docs`, `test`, `style`).
*   Escreva descrições curtas, claras, em minúsculas e separadas por hífen.
*   **Priorize o Inglês** em todo o código, comentários, commits e nomes de branches.

Adotar essas práticas desde cedo facilitará muito sua jornada como desenvolvedor e sua capacidade de trabalhar em projetos mais complexos e colaborativos.