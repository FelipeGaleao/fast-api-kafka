---
name: Criar uma nova discussão
about: Crie uma issue para iniciar uma discussão
title: '[DISCUSSÃO]: '
labels: ["discussao", "triagem"]
body:
    - type: textarea
        name: 'Descrição da discussão'
        description: 'Descreva a discussão de forma clara e concisa'
        required: true
        placeholder: 'Descreva a discussão de forma clara e concisa'
    - type: textarea
        name: 'Informações Adicionais'
        description: 'Adicione qualquer outra informação sobre a discussão aqui'
        required: false
        placeholder: 'Adicione qualquer outra informação sobre a discussão aqui'
    - type: checkbox
        name: 'Eu concordo que não há nenhuma issue aberta com o mesmo problema'
        description: 'Marque essa caixa para confirmar que não há nenhuma issue aberta com o mesmo problema'
        required: true
        options:
            - type: checkbox
              name: 'Eu concordo que não há nenhuma issue aberta com o mesmo problema'
              description: 'Marque essa caixa para confirmar que não há nenhuma issue aberta com o mesmo problema'
              required: true
---

 