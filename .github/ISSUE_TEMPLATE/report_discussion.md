---
name: Criar uma nova discussão
description: Crie uma issue para iniciar uma discussão
title: '[DISCUSSÃO]: '
labels: ["discussao", "triagem"]
body:
    - type: textarea
    id: descricao
    attributes:
        label: Descrição da discussão
        description: Descreva a discussão de forma clara e concisa
        placeholder: Descreva a discussão de forma clara e concisa
        required: true
    - type: textarea
    id: informacoes_adicionais
    attributes:
        label: Informações Adicionais
        description: Adicione qualquer outra informação sobre a discussão aqui
        placeholder: Adicione qualquer outra informação sobre a discussão aqui
        required: false
    - type: checkbox
    id: concordo
    attributes:
        label: Eu concordo que não há nenhuma issue aberta com o mesmo problema
        description: Marque essa caixa para confirmar que não há nenhuma issue aberta com o mesmo problema
        required: true
---

 