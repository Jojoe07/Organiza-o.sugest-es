import streamlit as st

#título
("""
# Guardião 

  Uma segurança complementar que identifica se a conexão com a internet é num ambiente seguro ou não.
No processo de aceite da funcionalidade o cliente cadastra uma rede wi-fi que ele considera segura, dessa forma ao sair desse ambiente suas transações previamente estabelecidas serão reduzidas de forma automática
 
 """)

tab1 , tab2 = st.tabs(["Como funciona", "Jornada"])
tab1.write("""
           
 Vale ressaltar os ganhos com a implantação do Guardião. 
         
**Para o cliente:**

- Mais segurança na rua
 
- Redução de perda financeira / atrito 
 
- Controle das transações 
 
**Na central**
- Redução de atrito

- Algo a mais para argumentar em caso de questionamento sobre a impossibilidade de uso do bankline, reforcando os benefícios de manter o Guardião ativo.

 **Para o time de desenvolvedores**
 
- Criação da jornada
 
- Criação do roteiro esclarecendo como funciona e os benefícios 
 
- Será necessário criar uma forma de visualização na central e no app quando o guardião estiver ativado
 
 """) #markdown

tab2.video("pages/Guardião_att.mp4")

st.caption("Desenvolvido por Joenice Almeida")
st.caption("Em 13/01/2025")