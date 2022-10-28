from pylab import *  #Biblioteca de Importação Python em função

p_min=10**5        #Pressão Mínima
p_max=20*10**5     #Pressão Máxima
v_max=0.3          #Volume Máximo
r=2                #Taxa De Compressão do Motor (relação entre V_max(V1)/V_min(V2))

γ=1.4              #Valor Gama

# Processo 1-2
p1=p_min           #P1 é igual a Pressão Mínima
v1=v_max           #V1 é igual a Volume Máximo
c1=p1*v1**γ        #Cálculo referente ao Processo de Compressão Adiabática
v2=v1/r            #V2 referente ao cálculo de Volume Mínimo
p2=c1/v2**γ        #Cálculo entre constante 1 x volume 2 elevado ao valor referente de gama


# Processo 2-3
p3=p_max          #Pressão 3 igual a Pressão máxima
v3=v2             #Volume 3 igual a Volume 2

############ Processo Adiabático: são processos termodinâmicos nos quais não ocorrem transferências de calor 
#entre um sistema e suas vizinhanças

# Processo 3-4
c2=p3*v3**γ       #Cálculo refetente Processo de Expansão Adiabática
v4=v1             #Volume 4 igual a Volume 1
p4=c2/v4**γ       #Cálculo entre constante 2 x volume 4 elevado ao valor referente de gama

########### Processo Adiabático: são processos termodinâmicos nos quais não ocorrem transferências de calor 
#entre um sistema e suas vizinhanças

# Processo 1-2
v=linspace(v2,v1,50)       #Volume referente ao vetores de Volume 2, Volume 1 com 50 pontos
p=c1/v**γ                  #Processo da compressão da pressão adiabática
plot(v,p,'r-')             #plotar variáveis

############ Processo Isovolumétrico: também chamados de isométricos ou isocóricos, 
#ocorrem quando há mudanças de pressão e de temperatura no interior de recipientes rígidos, ou seja,
#recipientes de volume invariável.

# Processo 2-3      
v=zeros(50)+v2           #Volume igual ao retorno equivalente mais o volume 2
p=linspace(p2,p3)        #pressão referente ao vetores de pressão 2, pressão 3
plot(v,p,'b-')           #plotar variáveis

############ Processo Adiabático: são processos termodinâmicos nos quais não ocorrem transferências de calor 
#entre um sistema e suas vizinhanças

#Processo 3-4
v=linspace(v3,v4,50)    #Volume referente ao vetores de Volume 3, Volume 4 com 50 pontos
p=c2/v**γ               #Processo da expansão da pressão adiabática
plot(v,p,'g-')          #plotar variáveis

########### Processo Isovolumétrico: também chamados de isométricos ou isocóricos, 
#ocorrem quando há mudanças de pressão e de temperatura no interior de recipientes rígidos, ou seja,
#recipientes de volume invariável.

#processo 4-1
v=zeros(50)+v1         #Volume igual ao retorno equivalente mais o volume 1
p=linspace(p1,p4)      #pressão referente ao vetores de pressão 1, pressão 4
plot(v,p,'m-')         #plotar variáveis

text(v1,p1-1000,'1',fontsize=12)
text(v2-0.006,p2,'2',fontsize=12)
text(v3-0.006,p3,'3',fontsize=12)
text(v4,p4+1000,'4',fontsize=12)

xlabel('Volume (m³)')      #Referente ao eixo X Volume
ylabel('pressão (atm)')    #Referente ao Eixo Y Pressão
show()                     #Plotar gráfico com as variáveis correspondentes
