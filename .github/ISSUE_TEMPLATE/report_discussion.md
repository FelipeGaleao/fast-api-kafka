---
name: Criar uma nova sugestão
about: Crie um reporte de sugestão para nos ajudar a melhorar
title: '[DISCUSSÃO]: '
labels: ["discussao", "triagem"]
body:
    - type:
        name: 'Descrição da sugestão'
        description: 'Descreva a sugestão de forma clara e concisa'
        required: true
        options:
            - type: textarea
              name: 'Descrição'
              description: 'Descreva a sugestão de forma clara e concisa'
              required: true
    - type:
        name: 'Screenshots'
        description: 'Se aplicável, adicione screenshots para ajudar a explicar o problema'
        required: false
        options:
            - type: textarea
              name: 'Screenshots'
              description: 'Se aplicável, adicione screenshots para ajudar a explicar o problema'
              required: false
    - type:
        name: 'Informações Adicionais'
        description: 'Adicione qualquer outra informação sobre o problema aqui'
        required: false
        options:
            - type: textarea
              name: 'Informações Adicionais'
              description: 'Adicione qualquer outra informação sobre o problema aqui'
              required: false

    - type:
        name: 'Eu concordo que não há nenhuma sugestão aberta com o mesmo problema'
        description: 'Marque essa caixa para confirmar que não há nenhuma sugestão aberta com o mesmo problema'
        required: true
        options:
            - type: checkbox
              name: 'Eu concordo que não há nenhuma sugestão aberta com o mesmo problema'
              description: 'Marque essa caixa para confirmar que não há nenhuma sugestão aberta com o mesmo problema'
              required: true
---