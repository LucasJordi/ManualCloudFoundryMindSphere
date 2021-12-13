

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">



<h1> Manual utilização Cloud Foundry (MindSphere)</h1>




## Sumário


<ol>

<li> 

<a href="#breve">Primeiros passos</a>
<ul>
<li><a href="#breve.1"> Conectando-se ao cloud foundry</a></li>

</ul>

</li>

<li> 

<a href="#ambiente">Configurando conta e/ou ambiente</a> </li>

<li> 

<a href="#deploy">Deploy de aplicação</a>

<ul>
<li><a href="#deploy.1">Configuração manifest.ylm</a></li>

<li><a href="#deploy.2">Publicando no Cloud Foundry</a></li>

</ul>

</li>

<li> 

<a href="#services">Serviços</a>

<ul>
<li><a href="#services.1">Criando um serviço</a></li>
<li><a href="#services.2">Criando as chaves do serviço</a></li>
<li><a href="#services.3">Acessando serviços utilizando SSH</a></li>


</ul>

</li>

<li><a href="#ref">Referências</a></li>

</ol>


<a id="breve"></a>
## Primeiros passos


<a id="breve.1"></a>
### Conectando com o cloud foundry
No terminal utilize o comando <code> cf login -a https://api.cf.eu1.mindsphere.io --sso </code>


<figure>
  <img src="./img/mind1.PNG" >
 <figcaption>Fig.1 - Terminal do cf.</figcaption>
</figure>

Se estiver tudo certo vai aparecer um link para geração de token de autenticação. Esse link deve ser colado no navegador.

<figure>
   <img src="./img/mind2.PNG">
 <figcaption>Fig.2 - Tela de verificação de identidade.</figcaption>
</figure>

Após inserir o código é gerado um token que deve ser adicionado a requisição no terminal.
<figure>
  <img src="./img/mind5.PNG">
  <figcaption>Fig.3 - Token de autenticação.</figcaption>
</figure>

Tudo certo! Se o código for validado com sucesso você já está autorizado para acessar a plataforma.

Se tudo der certo o retorno será equivalente:

<pre>
<code>
API endpoint:   https://api.cf.eu1.mindsphere.io
API version:    3.107.0
user:           SEU USUÁRIO
org:            ORG DA SUA EMPRESA
space:          SPACE DA SUA EMPRESA
</code>
</pre>





<a id="ambiente"></a>
## Configurando conta e/ou ambiente

### Caso sua org e/ou space não estejam disponíveis ou não estiver autorizado para fazer o push de uma aplicação

Para dar o deploy e gerenciar suas aplicações é preciso que a conta esteja atrelada a um org e space (para mais informações acesse a sessão de referências).
Para criar uma Org e Space use os seguintes comandos (Para executar esse comando é preciso ter perfil administrador).

<pre>
<code>
cf create-org ORG

cf create-space SPACE [-o ORG] [-q SPACE_QUOTA]

</pre>
</code>

Onde "ORG" e "SPACE" é o nome que deseja dar a Org e o Space respectivamente.

Para dar o push de uma aplicação é preciso ter a autorização SpaceDeveloper. Para isso use os seguintes comandos:


<pre>
<code>
cf set-org-role USERNAME ORG OrgManager
cf set-space-role USERNAME ORG SPACE SpaceDeveloper

</pre>
</code>

Onde "USERNAME" é o usuário que deseja atribuir a autorização.

Pronto! Agora o usuário está apto para dar o deploy de uma aplicação.

<a id="deploy"></a>
## Deploy de aplicação

Antes de continuar assegure-se de ter uma conta com perfil SpaceDeveloper. Utilize o comando <code> cf space-users ORG SPACE </code> .

A aplicação utilizada para deploy foi desenvolvida em Spring Boot.


<a id="deploy.0"></a>
### Gerando arquivo .war
Para gerar o arquivo .war, usando o STS, acessar "File->Export-> Selecionar Web -> Clicar em WAR File"

<figure>
  <img src="./img/mind22.PNG">
  <figcaption>Fig.4 - Geração de arquivo .War no STS.</figcaption>
</figure>


<a id="deploy.1"></a>
### Configuração manifest.ylm

Essa aplicação utiliza o serviço do Postgresql para mais informações visite a sessão <a href="#services">Serviços</a>

A configuração básica do manifest.ylm para o projeto é:

<pre>
<code>
applications:
  - name: NOMEAPLICAÇÃO 
    instances: 1
    buildpacks: 
      - java_buildpack
    path: ./APP.war  #Caminho da aplicação
    random-route: true
    memory: 1024MB   #Quantidade de memória ram 
    disk_quota: 500MB #Quantidade de espaço disponível para a aplicação
    services:
      - NOMESERVIÇO  #Nome do serviço criado
    


</pre>
</code>

<a id="deploy.2"></a>
###  Publicando no Cloud Foundry

Finalizando as configurações basta apenas utilizar o comando <code> cf push </code>








<a id="services"></a>
## Serviços

O serviço utilizado será o do Postgresql


<a id="services.1"></a>
### Criando um serviço 

Para criar um serviço primeiramente é preciso saber os serviços disponíveis para uso, utilize o seguinte comando:

<pre>
<code>
cf marketplace
</pre>
</code>

<figure>
  <img src="./img/mind6.PNG">
  <figcaption>Fig.5 - Serviços disponíveis no marketplace do cf.</figcaption>
</figure>

Para o projeto será utilizado o serviço postgresql94 com o plano postgresql-m. Para criar um serviço no seu Space utilize:

<pre>
<code>
cf create-service SERVIÇO PLANO NOMESERVIÇO
</pre>
</code>
Para o projeto ficaria o seguinte: <code> cf create-service postgresql94 postgresql-m postgresql-carsharing</code>.


Antes de utilizar o serviço aguarde alguns minutos até que o status seja atualizado para "create succeeded" para verificar utilize o comando <code> cf services </code> e localize o serviço criado.

<figure>
  <img src="./img/mind10.PNG">
  <figcaption>Fig.6 - Criação de serviço.</figcaption>
</figure>

<a id="services.2"></a>
### Criando as chaves do serviço

Para o caso do projeto é preciso criar chaves para acesso ao banco do Postgres:

<pre>
<code>
cf create-service-key NOMEDOSERVIÇOCRIADO NOMEDAKEY


Exemplo :

cf create-service-key postgresql-carsharing cimatec
</pre>
</code>

Se a key foi criada com sucesso basta executar o comando:

<pre>
<code>
cf service-key NOMEDOSERVIÇO NOMEDAKEY

</pre>
</code>

A resposta deve ser algo como:

<figure>
  <img src="./img/mind11.PNG">
  <figcaption>Fig.7 - Chaves de acesso serviço do postgresql.</figcaption>
</figure>

Agora é só adicionar o serviço no manifest.yml e as keys na sua aplicação para poder utilizar o serviço.


<a id="services.3"></a>
### Acessando serviços utilizando SSH

<pre>
<code>
cf ssh -L PORTA:HOSTNAME:PORTADOSERVIÇO NOMEDOAPPQUEUTILIZAOSERVIÇO

</pre>
</code>    

Digamos que tenha sido criado um serviço chamado serviço1 que é utilizado pela aplicação 1 cadastrada no sistema como app1 cujas keys são:

<pre>
<code>
{
  "credentials": {
    "host": "ueueue-psql-master-alias.node.dc1.sjusu",
    "hosts": [
      "ueueue-psql-master-alias.node.dc1.djndh",
      "ueueue-psql-master-alias.node.dc1.sjiidiusu",
      "ueueue-psql-master-alias.node.dc1.ddudu"
    ],
    "name": "ususuusu",
    "password": "viidjfjidfijfdjifd",
    "port": 5432,
    "uri": "postgres://fijsgdsfiogdiogjdoigd:jidsfojofdjisdojifdjoidf@dfiudi-psql-master-alias.node.dc1.a9ssvc:5432/ususuusu",
    "username": "fdsuufidudfjufsdsdufi"
  }
}

</pre>
</code>

Então o comando seria <code> cf ssh -L 63306:ueueue-psql-master-alias.node.dc1.sjusu:5432 app1</code>

<figure>
  <img src="./img/mind12.PNG">
  <figcaption>Fig.8 - Resultado de conexão com o container usando SSH.</figcaption>
</figure>

Imagem mostra o resultado da conexão estabelecida.

Agora se quisermos acessar o banco utilizamos o serviço do Postgresql instalado na máquina. Para esse caso foi utilizado o PhpAdmin.

<figure>
  <img src="./img/mind13.PNG">
  <figcaption>Fig.9 - Conexão do banco usando o PhpMyAdmin.</figcaption>
</figure>

Lembrar de colocar a porta escolhida no SSH e não a que está na key. Nesse caso é a 63306.


<figure>
  <img style="width:30%" src="./img/mind14.PNG">
  <figcaption>Fig.10 - Tabelas do banco cadastrado no cf.</figcaption>
</figure>


É possível ver que as tabelas batem com as do projeto.



<a id="ref"></a>
## Referências

[Serviços e Keys](https://docs.cloudfoundry.org/devguide/services/service-keys.html#create)

[Conectando serviços com SSH](https://docs.cloudfoundry.org/devguide/deploy-apps/ssh-services.html)

[Perfis de autorização](https://docs.cloudfoundry.org/concepts/roles.html#orgs)

[Deploy Spring Apps](https://docs.cloudfoundry.org/buildpacks/java/getting-started-deploying-apps/gsg-spring.html)

[Publicando apps](https://docs.cloudfoundry.org/devguide/deploy-apps/deploy-app.html)














