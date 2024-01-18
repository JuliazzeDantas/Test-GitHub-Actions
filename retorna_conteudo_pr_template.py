import base64
import sys

def main(name, owner, project, area):
    content = f'''---
name: Modelo Pull Request
about: Describe this issue template's purpose here.
title: Modelo Pull Request
labels: ''
assignees: claricepdantas

---

# Pull Request

## Descrição

Descreva brevemente as alterações implementadas nesta solicitação de pull.

## Problema

Explique o problema ou a necessidade que essa solicitação de pull visa resolver.

## Solução

Descreva a solução implementada e como ela aborda o problema mencionado acima.

## Alterações Propostas

Liste as principais alterações realizadas no código.

- [ ] Alteração 1
- [ ] Alteração 2
- [ ] ...

## Testes Realizados

Descreva os testes que foram realizados para garantir que as alterações não introduziram novos problemas.

- [ ] Teste A
- [ ] Teste B
- [ ] ...

## Capturas de Tela (se aplicável)

Inclua capturas de tela relevantes, se necessário.

## Checklist

- [ ] Minhas alterações passaram nos testes locais.
- [ ] Eu atualizei a documentação conforme necessário.
- [ ] Os testes de unidade foram adicionados ou atualizados conforme necessário.
- [ ] Eu li o guia de contribuição e segui as diretrizes.

## Comentários Adicionais

Forneça qualquer informação adicional que você julgar relevante.

## Issue Relacionada

Indique se há uma issue relacionada a este pull request.

## Pontos de Atenção

Destaque áreas específicas que podem precisar de revisão ou atenção extra.'''
    return base64.b64encode(str(content).encode()).decode()



if __name__ == "__main__":
    print(main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))