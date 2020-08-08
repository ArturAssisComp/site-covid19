# Projeto CES-22 - 2º bimestre
Projeto de CES - 22 do 2º bimestre

Integrantes:

  Ana Paula Schuch

  Artur Assis Alves

  Vinícius Brito Bastos Antunes

### OBS: 
1 - Os pacotes que precisam ser instalados na máquina do desenvolvedor se encontram no arquivo requirements-dev.txt. O arquivo requirements.txt será utilizado para fazer deploy no servidor e ele chamará o arquivo requirements-dev.txt para instalar todos pacotes dele além de instalar mais dois, que não precisam ser instalados na máquina do desenvolvedor.

2 - É importante não publicar as variáveis SECRET_KEY e DEBUG. Por isso, utilizar a lib decouple pode ajudar.

### Instalar os seguintes pacotes para iniciar o servidor:

  python               3.7.7

  django               3.0.8

  matplotlib           3.3.0   

  pandas               1.1.0          

  django-widget-tweaks 1.4.8

  mpld3

  reportlab            3.5.46  


#### Para realizar o deploy no Heroku, foi utilizado o tutorial: https://github.com/Gpzim98/django-heroku
