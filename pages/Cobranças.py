
import streamlit as st

("""
 # Opções de cobrança
 
 Com o avanço da tecnologia é interessante que nossos clientes tenham outras formas de cobrança. Pensando nisso foram criadas algumas opções.
 
 **Ganhos da Emps:**
- Aumenta as movimentações em conta 
- Cliente terá autonomia de qual forma é mais lucrativa para enviar suas cobranças
 """)

#Cobrança via WhatsApp 
tab1 , tab2 = st.tabs(["Cobrança via whatsApp" , "Pagamento por aproximação"])
tab1.write("""
 # Cobrança via whatsApp
 
 **Para vendas online**
 
 Direcionado para lojas virtuais ou físicas com a  utilização da tecnologia a seu favor pode ser utilizado como mais um meio de pagamento.
 
 **Como funciona:**
 
 O dono da empresa gera o boleto e deixa acordado previamente a forma de pagamento com o cliente e ao visualizar o sucesso do pagamento 
 direciona a mercadoria/serviço.
 
 **Clientes beneficiados com essa opção:**
 
- Problemas no chip para realizar a transação no cartão de crédito, cartão perdido ou guardando o recebimento da nova via. Podendo assim realizar a transação gerando um cartão virtual 
- Sem saldo em conta para pagar com o QR Code no Pix, não tem como ir na loja por ser distante
- A laranjinha descarregou

 **Para desenvolvedores:**
- Criar um fluxo para gerar o boleto por esse canal
- Inserir no fluxo de caixa as entradas

 """) #markdown

st.link_button("Clique aqui para mais detalhes" , "https://faq.whatsapp.com/1690350561340616")




tab2.write("""
 # Aproximou pagou
 
 **Como funciona:** 
 
 Pagamento por meio de aproximação transformando assim o smartphone do cliente numa maquininha e o dinheiro cai na hora na conta.
 O dono da empreesa  gera o valor para pagamento e o seu cliente após confirmação do valor e forma de pagamento é só encostar os smartphones 
 
 **Objetivo:**
- Trazer mais um valor ao app Emps
 
 **Regras para a utilização**
- Somente para smartphone que tenha tecnologia NFC (tanto o dono da empresa quanto o seu cliente)
 
 **Para desenvolvedores:**
- Criar uma jornada dentro do app para o pagamento por aproximação atrelado a chave Pix.
- Inserir no fluxo  de caixa as entradas
 """)

st.caption("Desenvolvido por Joenice Almeida")
st.caption("Em 13/01/2025")
