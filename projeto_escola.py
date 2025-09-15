import guarda_funcoes
import streamlit as st 

st.title("calculadora de media dos aulunos")

nome = st.text_input("Nome do aluno")
 
nota1 = st.slider(min_value=0.0, max_value=10.0,label="Nota 1",step=0.25)
nota2 = st.slider(min_value=0.0, max_value=10.0,label="Nota 2",step=0.25)
nota3 = st.slider(min_value=0.0, max_value=10.0,label="Nota 3",step=0.25)
nota4 = st.slider(min_value=0.0, max_value=10.0,label="Nota 4",step=0.25)

botao = st.button ("enviar")

if botao:
    media = guarda_funcoes.calcula_media(nota1,nota2,nota3,nota4)
    situacao = guarda_funcoes.situacao_media(media)
    texto = f"O aluno:{nome}, está {situacao}, com media: {media}"
    if situacao == "Aprovado":
        st.success(texto)
    elif situacao == "Recuperação":
        st.warning(texto)
    else:
        st.error(texto)