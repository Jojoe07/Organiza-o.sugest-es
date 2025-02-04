import streamlit as st 


#envio de e-mails 
("""
 # Envio de e-mails 
 
 Focado no objetivo de acolhimento ou felicitação por mais um ano de vida.

Como ficará a jornada:

**Parabenizando** 

Será enviado de forma automática no dia do aniversário do representante legal, baseado na base que temos de nossos clientes.

**Acolhimento** 

O Emprs Force recepciona a ligação ou chat e ao ser informado sobre roubo, perda ou sequestro irá enviar os dados para os Empers Specs realizar o envio do e-mail prestando nossa solidariedade nesse momento difícil
 
 """)


#parabenizando
tab1 , tab2 = st.tabs(["E-mail parabenizando" , "E-maill de acolhimento"])
tab1.write("""
**Assunto: Parabéns pelo seu aniversário!**

Olá **[Nome do Cliente]**,

Espero que esta mensagem o encontre bem. Hoje é um dia especial, e não poderíamos deixar de parabenizá-lo pelo seu aniversário! 🎉

Em nome de toda a equipe da Itaú Emps, gostaria de expressar nossos mais sinceros votos de felicidade, saúde e sucesso. Que este novo ano de vida seja repleto de momentos inesquecíveis e realizações.

Agradecemos por ser um cliente tão valioso e por confiar em nossos serviços. Estamos sempre à disposição para atendê-lo da melhor forma possível.

Aproveite seu dia ao máximo!

Com os melhores cumprimentos,

[Seu Nome] [Seu Cargo] [Nome da Empresa] [Telefone] [E-mail]
""") #markdown

st.balloons()


#roubo/sequestro ou perda
tab2.write("""
**Assunto: Lamentamos profundamente o ocorrido**

Olá **[Nome do Cliente]**,

Espero que esta mensagem o encontre em segurança. Recebemos a notícia do recente incidente de sequestro/roubo ou perda e gostaríamos de expressar nossa profunda solidariedade e preocupação.

Em nome de toda a equipe da Itaú Emps, lamentamos profundamente o ocorrido e estamos à disposição para oferecer qualquer tipo de apoio que possa necessitar neste momento difícil. Sabemos que situações como essa são extremamente traumáticas e queremos que saiba que estamos aqui para ajudar no que for possível.

Se houver algo que possamos fazer para apoiar você ou sua família, por favor, não hesite em nos informar. Nossa prioridade é garantir que você se sinta amparado e seguro.

Com os melhores cumprimentos,

[Seu Nome] [Seu Cargo] [Nome da Empresa] [Telefone] [E-mail]
           """) #markdown


st.caption("Desenvolvido por Joenice Almeida")
st.caption("Em 13/01/2025")
