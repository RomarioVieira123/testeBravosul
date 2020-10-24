<h1>INTRODUÇÃO</h1>

<body>Projeto teste criado para simular uma livraria online. O projeto possui uma listagem de livros emprestados e caso exista multa a sua vizualização.
Possui uma listagem de livros reservados de acordo com o livro e uma listagem de todos os livros cadastrados e seus staus seja disponível ou emprestado. 

<body>
<h2>Índice</h2>
<ul>
    <li><a href="#estruturaprojeto">Estrutura Projeto</a>
        <ul>
            <li><a href="#appbook">App Book</a></li>
            <li><a href="#apploan">App Loan</a></li>
            <li><a href="#apppenalty">App Penalty</a></li>
            <li><a href="#apppricing">App Pricing</a></li>
            <li><a href="#appreservation">App Reservation</a></li>
            <li><a href="#projetocore">Projeto Core</a></li>
        </ul>
    </li>
    <li><a href="#regras">Regras</a></li>
    <li><a href="#instrucoesapi">API</a>
    <li><a href="#instrucoesexecucao">Instruções de execução</a></li>
    <li><a href="#tecnologiasusadas">Tecnologias Usadas para Desenvolvimento</a>
        <ul>
            <li><a href="#sistemaoperacional">Sistema Operacional</a></li>
            <li><a href="#ide">IDE</a></li>
            <li><a href="#frameworks">Frameworks</a></li>
            <li><a href="#testeapi">Teste API</a></li>
        </ul>
    </li>
</ul>
<h2 id="estruturaprojeto">Estrutura do Projeto</h2>
        A estrutura do projeto está organizado em 4 apps, sendo elas broker, message, shareds, telephone_operator e o projeto core.
        A organização do banco de dados obedece o diagrama abaixo:
        <img src="images/Diagrama%20Livraria%20Teste%20Python%20BravoSul.png" alt="">
        <h4 id="appbook">App Book</h4>
            <ol>
                <li>App responsável pelos dados do broker, sendo o idbroker, name e create_at.</li>
                <li>Sua serialização é realizada apenas retornando o idbroker.</li>
                <li>Não possui urls ou views.</li>          
            </ol>         
        <h4 id="apploan">App Loan</h4>
            <ol>
                <li>App responsável pelos dados compartilhados.</li>
                <li>Possui 3 models sendo Country, Stat e City usando apenas Stat.</li>
                <li>Não possui serialização, urls ou views.</li>
                <li>Contém o arquivo BlackList.py responsável pela conexão com a API Black List.</li>
                <li>Nesta classe "toda" a lista é carregada uma única vez para se evitar que a aplicação perca desempenho a cada requisição realizada.</li>
            </ol>  
        <h4 id="apppenalty">App Penalty</h4>
             <ol>
                <li>App responsável pelos dados de mensagens, sendo o idmensagem, operator, stat, message, destination_number, shipping_time e created_at.</li>
                <li>Sua serialização é realizada apenas retornando o idmensagem e operator.</li>
                <li>Posusi a url principal de acesso da API.</li>    
                <li>Sua view possui 2 métodos sendo GET e POST.</li>
                <li>O método GET retorna HTTP 400, enquanto o método POST retorna os dados solicitados de acordo com a regra do teste, sendo somente idmensagem e idbroker.</li>
                <li>Possui a pasta fixtures onde guarda um arquivo shared.json para inicialização e população com dados fictícios no banco de dados.</li>
            </ol>  
        <h4 id="apppricing">App Pricing</h4>
             <ol>
                <li>App responsável pelos dados da operadora sendo idoperator, broker, operator e created_at.</li>
                <li>Sua serialização é realizada apenas retornando o idmensagem e operator.</li>
                <li>Posusi 2 métodos de serialização onde um retorna todos os dados e o outro retorna apenas o idbroker.</li>    
                <li>Não possui urls ou views.</li>
            </ol>
       <h4 id="appreservation">App Reservation</h4>
             <ol>
                <li>App responsável pelos dados de mensagens, sendo o idmensagem, operator, stat, message, destination_number, shipping_time e created_at.</li>
                <li>Sua serialização é realizada apenas retornando o idmensagem e operator.</li>
                <li>Posusi a url principal de acesso da API.</li>    
                <li>Sua view possui 2 métodos sendo GET e POST.</li>
                <li>O método GET retorna HTTP 400, enquanto o método POST retorna os dados solicitados de acordo com a regra do teste, sendo somente idmensagem e idbroker.</li>
                <li>Possui a pasta fixtures onde guarda um arquivo shared.json para inicialização e população com dados fictícios no banco de dados.</li>
            </ol>   
        <h4 id="projetocore">Projeto Core</h4>
            <ol>
                <li>Projeto principal do django.</li>
                <li>Adicionado ao arquivo settings.py todas as variáveis usadas como constantes no projeto. </li>
                <li>Adicionado ao arquivo urls.py, as url principal da aplicação /api/messages</li>
            </ol>  
<h2 id="regras">Regras Implementadas</h2>
    <ul>
        <li>Mensagens que possuam o nº de celular na blacklist e ativos, devem ser bloqueadas.</li>
        <li>Mensagens para SP, devem ser bloqueadas</li>
        <li>Mensagens com agendamento após as 19:59:59 devem ser bloqueadas.</li>
        <li>Mensagens com mais de 140 caracteres devem ser bloqueadas.</li>
        <li>Mensagens com DDD com mais de 2 dígitos ou menos de 2 dígitos ou DDD não for válido devem ser bloqueadas.(Válido se estiver cadastrado no banco de dados.)</li>
        <li>Mensagens com nº de celular com mais ou menos de 9 dígitos, devem ser bloqueadas.</li>
        <li>Mensagens com nº de celular em que o 1º dígito não começe com 9 ou o 2 dígito menor que 6 devem ser bloqueadas.</li>   
    </ul>
<h2 id="instrucoesapi">API</h2>
    <h3 id="instrucoesexecucao">Instruções de execucão</h3>
        <p>
        Ao abrir o projeto pela IDE Pycharm, realizar a instalação do ambiente virtualenv, atráves do seguindo comando:
        <ul>
            <li>python3 -m virtualenv venv</li>
        </ul>
        Após instalação, realizar a ativação do ambiente virtual, através do comando:
        <br>
        <ul>
            <li>. venv/bin/activate</li> 
        </ul>
        Após a ativação do ambiente virtual, realizar as migrações necessárias para ocorrer a criação do modelos e a criação do banco de dados .sqlite.
        Executar os comandos abaixo:
        <br>
        <ul>
            <li>python manage.py makemigrations</li>
            <li>python manage.py migrate</li>
        </ul>
        Após as migrações, realizar as configurações dos dados fictícios para teste da aplicação. Digita o seguinte comando a linha de comando:
        <ul>
            <li>python3 manage.py loaddata shareds.json</li>
        </ul>
    <h3 id="instrucoetesteaplicacao">Instruções de teste aplicação</h3>
        <p>Para realizar o teste da aplicação deve ser usado a ferramenta Postman, ferramenta muito utilizada por desenvolvedores para
           se testar API's, obtida no endereço <a href="https://www.postman.com/">Download Postman</a> de acordo com a versão do Sistema Operacional.
           Com a instalação do Postman realizada e a aplicação rodando, deve adicionar a url ao ferramenta Postman configurando o endereço e porta de
           execução do Django e configurar os parâmentros de acordo com a imagem.
        <img src="images/Teste%20Aplicação.png" alt=""></p>
            No campo de dados adicionar os dados localizados em /comandos/Dados usados para test.text.
            <img src="images/Teste%20Aplicação%203.png" alt="">
            Ao solicitar a requisição o retorno deve ser as mensagens válidas com seu respectivo broker.
        <img src="images/Teste%20Aplicação%202.png" alt="">
    <h3 id="tecnologiasusadas">Tecnologias Usadas para Desenvolvimento</h3>
        <ul>
            <li><h4 id="sistemaoperacional">Sistema Operacional</h4>
            Sistema operacional Kubuntu versão 20.04 64 bits...   
            </li>
            <li><h4 id="ide">IDE</h4>
            Pycharm Profissional 2020.2  
            </li>
            <li><h4 id="frameworks">Frameworks</h4>
            Django versão 3.1.1 - Django Rest Framework versão 3.11.1 - *Ver requirements.txt  
            </li>
            <li><h4 id="testeapi">Teste API</h4>
            Postman for Linux - versão 7.33.1
            </li>     
        </ul>
        
</body>