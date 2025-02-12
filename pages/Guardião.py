import streamlit as st

#título
("""
# Guardião 

  Uma segurança complementar que identifica se a conexão com a internet é num ambiente seguro ou não.
No processo de aceite da funcionalidade o cliente cadastra uma rede wi-fi que ele considera segura, dessa forma ao sair desse ambiente suas transações previamente estabelecidas serão reduzidas de forma automática
 
 """)

("""
           
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

embed_code = """ <iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="600" height="450" src="https://embed.figma.com/proto/GdWmLrOSmBw64bXGVbczPD/Faq-Emps?node-id=142-25&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=142%3A25&show-proto-sidebar=1&embed-host=share" allowfullscreen></iframe>"""
st.components.v1.html(embed_code,height=400)

st.caption("Desenvolvido por Joenice Almeida")
st.caption("Em 13/01/2025")
