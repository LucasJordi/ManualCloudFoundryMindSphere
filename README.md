<h1> Manual utilização da plataforma Mindsphere</h1>


O intuito desse projeto é aprender a operar e entender como funciona o OCPP. Por enquanto o único público alvo desse trabalho é o próprio autor.

## Sumário


<ol>

<li> 

<a href="#breve">Primeiros passos</a>
<ul>
<li><a href=""> Conectando com o cloud foundry</a></li>

</ul>

</li>

<li> 

<a href="#ambiente">Configurando conta e/ou ambiente</a> </li>

<li> 

<a href="#deploy">Deploy de aplicação</a>

<ul>
<li><a href="">Configuração manifest.ylm</a></li>

<li><a href="">Publicando no Cloud Foundry</a></li>

</ul>

</li>

<li> 

<a href="#services">Serviços</a>

<ul>
<li><a href="">Criando um serviço</a></li>
<li><a href="">Criando as chaves do serviço</a></li>
<li><a href="">Acessando serviços utilizando SSH</a></li>


</ul>

</li>

<li><a href="#ref">Referências</a></li>

</ol>


<a id="breve"></a>
## Primeiros passos

### Conectando com o cloud foundry
No terminal utilize o comando ```` cf login -a https://api.cf.eu1.mindsphere.io --sso ````

![Screenshot](./img/mind1.PNG)

Se estiver tudo certo vai ser gerado um link para geração de token de autenticação. Esse link deve ser colado no navegador.

![Screenshot](./img/mind2.PNG)


Após inserir o código é gerado um token que deve ser adicionado a requisição no terminal.

![Screenshot](./img/mind5.PNG)

Tudo certo! Se o código for validado com sucesso você já está autorizado para acessar a plataforma.

Se tudo der certo o retorno será equivalente:

````
API endpoint:   https://api.cf.eu1.mindsphere.io
API version:    3.107.0
user:           SEU USUÁRIO
org:            ORG DA SUA EMPRESA
space:          SPACE DA SUA EMPRESA
````





<a id="ambiente"></a>
## Configurando conta e/ou ambiente

### Caso sua org e/ou space não estejam disponíveis ou não estiver autorizado para fazer o push de uma aplicação

Para poder dar o deploy e gerenciar suas aplicações é preciso que a conta esteja atrelada a um org e space (para mais informações acesse a sessão de referências).
Para criar uma Org e Space use os seguintes comandos (Para executar esse comando é preciso ter perfil administrador).

````
cf create-org ORG

cf create-space SPACE [-o ORG] [-q SPACE_QUOTA]

````

Onde "ORG" e "SPACE" é o nome que deseja dar a Org e o Space respectivamente.

Para poder dar o push de uma aplicação é preciso ter a autorização SpaceDeveloper. Para isso use os seguintes comandos:


````
cf set-org-role USERNAME ORG OrgManager
cf set-space-role USERNAME ORG SPACE SpaceDeveloper

````

Onde "USERNAME" é o usuário que deseja atribuir a autorização.

Pronto! Agora o usuário está apto para dar o deploy de uma aplicação.

<a id="deploy"></a>
## Deploy de aplicação

Antes de continuar assegure-se de ter uma conta com perfil SpaceDeveloper. Utilize o comando ```` cf space-users ORG SPACE ```` .

A aplicação utilizada para deploy foi desenvolvida em Spring Boot.

### Configuração manifest.ylm

Essa aplicação utiliza o serviço do Postgresql para mais informações visite a sessão <a href="#services">Serviços</a>

A configuração básica do manifest.ylm para o projeto é:

````



````


###  Publicando no Cloud Foundry

Finalizando as configurações basta apenas utilizar o comando ```` cf push ````.








<a id="services"></a>
## Serviços

O serviço utilizado será o do Postgresql

### Criando um serviço 

Para criar um serviço primeiramente é preciso saber os serviços disponíveis para uso, utilize o seguinte comando:

````
cf marketplace
````
![Screenshot](./img/mind6.PNG)

Para o projeto será utilizado o serviço postgresql94 com o plano postgresql-m. Para criar um serviço no seu Space utilize:

````
cf create-service SERVIÇO PLANO NOMESERVIÇO
````
Para o projeto ficaria o seguinte: ```` cf create-service postgresql94 postgresql-m postgresql-carsharing ````


Antes de utilizar o serviço aguarde alguns minutos até que o status seja atualizado para "create succeeded" para verificar utilize o comando ```` cf services ```` e localize o serviço criado.

![Screenshot](./img/mind10.PNG)


### Criando as chaves do serviço

Para o caso do projeto é preciso criar chaves para acesso ao banco do Postgres:

````
cf create-service-key NOMEDOSERVIÇOCRIADO NOMEDAKEY


Exemplo :

cf create-service-key postgresql-carsharing cimatec
````

Se a key foi criada com sucesso basta executar o comando:

````
cf service-key NOMEDOSERVIÇO NOMEDAKEY

````

A resposta deve ser algo como:

![Screenshot](./img/mind11.PNG)

Agora é só adicionar o serviço no manifest.yml e as keys na sua aplicação para poder utilizar o serviço.
### Acessando serviços utilizando SSH

````
cf ssh -L PORTA:HOSTNAME:PORTADOSERVIÇO NOMEDOAPPQUEUTILIZAOSERVIÇO

````    

Digamos que tenha sido criado um serviço chamado serviço1 que é utilizado pela aplicação 1 cadastrada no sistema como app1 cujas keys são:

````
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

````

Então o comando seria ```` cf ssh -L 63306:ueueue-psql-master-alias.node.dc1.sjusu:5432 app1````

![Screenshot](./img/mind12.PNG)
Imagem mostra o resultado da conexão estabelecida.

Agora se quisermos acessar o banco utilizamos o serviço do Postgresql instalado na máquina. Para esse caso foi utilizado o PhpAdmin.


![Screenshot](./img/mind13.PNG)

Lembrar de colocar a porta escolhida no SSH e não a que está na key. Nesse caso é a 63306.



![Screenshot](./img/mind14.PNG)

É possível ver que as tabelas batem com as do projeto.



<a id="ref"></a>
## Referências

[Serviços e Keys](https://docs.cloudfoundry.org/devguide/services/service-keys.html#create)

[Conectando serviços com SSH](https://docs.cloudfoundry.org/devguide/deploy-apps/ssh-services.html)

[Perfis de autorização](https://docs.cloudfoundry.org/concepts/roles.html#orgs)

[Deploy Spring Apps](https://docs.cloudfoundry.org/buildpacks/java/getting-started-deploying-apps/gsg-spring.html)



[Publicando apps](https://docs.cloudfoundry.org/devguide/deploy-apps/deploy-app.html)














