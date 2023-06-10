name: Reporte de Bug
about: Crie um reporte de bug para nos ajudar a melhorar
title: '[BUG]: '
labels: ["bug", "triagem"]
body:
    - type:
        name: 'Descrição do Bug'
        description: 'Descreva o bug de forma clara e concisa'
        required: true
        options:
            - type: textarea
              name: 'Descrição'
              description: 'Descreva o bug de forma clara e concisa'
              required: true
    - type:
        name: 'Reprodução do Bug'
        description: 'Passos para reproduzir o bug'
        required: true
        options:
            - type: textarea
              name: 'Passos'
              description: 'Passos para reproduzir o bug'
              required: true
    - type:
        name: 'Comportamento Esperado'
        description: 'Descreva o comportamento esperado'
        required: true
        options:
            - type: textarea
              name: 'Comportamento Esperado'
              description: 'Descreva o comportamento esperado'
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
        name: 'Eu concordo que não há nenhuma issue aberta com o mesmo problema'
        description: 'Marque essa caixa para confirmar que não há nenhuma issue aberta com o mesmo problema'
        required: true
        options:
            - type: checkbox
              name: 'Eu concordo que não há nenhuma issue aberta com o mesmo problema'
              description: 'Marque essa caixa para confirmar que não há nenhuma issue aberta com o mesmo problema'
              required: true