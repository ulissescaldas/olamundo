# Aula Markdown - Curso em Vídeo
## [Link do Curso GIT/GITHUB](https://www.cursoemvideo.com/curso/curso-de-git-e-github/)

Olá, Mundo!

**Olá, Mundo!**

__Olá, Mundo!__

*Olá, Mundo!*

_Olá, Mundo!_

__*Olá, Mundo!*__

~~Olá, Mundo!~~

~~__*Olá, Mundo!*__~~


# Título nível 1

## Título nível 2

### Título nível 3

## Linha 
---

## Lista numerada
---
1. Lista numerada
   1. Lista numerada
   2. Lista numerada
      1. Lista numerada
      2. Lista numerada
   3. Lista numerada     
3. Lista numerada
4. Lista numerada
7. Lista numerada
8. Lista numerada
9. Lista numerada

## Lista demarcada
---
* Lista demarcada
* Lista demarcada
  * Lista demarcada
  * Lista demarcada
    * Lista demarcada
    * Lista demarcada
* Lista demarcada     
 
## Lista tarefa
---
- [ ] Criar tarefa 1
- [x] Criar tarefa 2
- [x] Criar tarefa 3
- [ ] Criar tarefa 4

## Imagem
---
![Imagem de teste aula002](https://github.com/ulissescaldas/Ola-Mundo/assets/140160383/2f2395a5-dd0a-41c8-a3b7-670f590d9590)

## Link
---
[Acesse aqui a aula de Markdown - Curso em Vídeo](https://www.youtube.com/watch?v=LntSB-gl-ZI&t=1389s)

## Tabela
---
coluna 1 | coluna 2 | caluna 3
--- | --- | ---
linha 1 | aula002 | título
linha 2 | aula002 | lista
linha 3 | aula002 | imagem
linha 4 | aula002 | link
linha 5 | aula002 | tabela

## Comando de Programação
---
Comando de Programação `select * from tb_fato_atividade_coordenada`

Comando de Programação 
```
select ac.codigo,
       ac.nome,
       ac.tipo,
       ac.status,
       ac.sigla
  from tb_fato_atividade_coordenada ac
left join tb_dimensao_tipo ti on ac.tipo = ti.tipo
where ac.status = 'concluído' and ti.tipo = 1
order by ac.nome asc
```

## Emoji
---
Olá, Mundo! :earth_americas: `:earth_americas:`

[Perfil com nomes emojis](https://github.com/ikatyang/emoji-cheat-sheet)

## Citações e marcação
---
Obrigado! @ikatyang

> Esta é uma citação externa com algum texto. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
>> Esta é uma citação interna com algum texto.

## Link para o manual Markdown do Curso em Vídeo
---
[click aqui para ver o manula Markdown](https://github.com/ulissescaldas/Ola-Mundo/blob/main/GIT-GITHUB/guia-markdown.pdf)
