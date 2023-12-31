# Trabalho Final

Trabalho final da disciplina de Fundamentos de Redes de Computadores.

## Participantes

Nome Completo | Matrícula |
------------- | --------- |
Caio César Oliveira | 190085291 |
Guilherme Nishimura | 200030264 |
Matheus Costa Gomes | 190093331 |
Vitor Eduardo Kühl Rodrigues | 190118288 |

## Exemplo de Usabilidade

https://github.com/oCaioOliveira/trabalho-final-frc/assets/54439337/bad066f2-bd6e-4347-ab13-cb023a4fa0a5

## Intruções para rodar a aplicação

### Instalação do servidor 

Pré requisitos: 

    Python 

Instalar a biblioteca WebSockets: 

    pip install websockets 

Executar o Servidor (estando na pasta do servidor): 

    python3 server.py 

### Execução do Cliente (WEB) 

Basta executar o arquivo index.html (dois cliques no arquivo para abrir). 

## Instruções para utilizar a configuração do DNS para acesso via URL

A configuração DNS utilizada foi uma solução apenas para execuções da aplicação de forma local, para acessar essa URL globalmente é necessário utilizar um provedor de serviços DNS como GoDaddy, Cloudflare, Google Domains, entre outros. 

- **Manualmente** no ambiente Linux:
  - Ir a pasta raiz da sua máquina e acessar o arquivo etc/hosts, comando:
    - `vim etc/hosts`
  - Colocar uma linha com o endereço e a URL desejados, exemplo:
    - `127.0.0.1       trabalho-final-redes-cgmv.com`

- **Automaticamente** por meio de um script:
  - Acessar a pasta `scripts` nesse repositório e dar permissão ao script `add_hosts.sh`, comando:
    - `chmod +x ./add_hosts.sh`
  - Após isso executar esse script como **sudo**, comando:
      - `sudo ./add_hosts.sh` 
## Instruções para receber conexões HTTP e HTTPS

Para preparar o servidor Apache para receber conexões HTTP e HTTPS no Ubuntu, você pode seguir os seguintes passos:
- **Manualmente** no ambiente Linux:
  
  - Instale o Apache:
    
    - `sudo apt update`
    
    - `sudo apt install apache2`
    
  - Habilite o módulo SSL do Apache:
    
    - `sudo a2enmod ssl`
   
- Configure o Firewall para permitir conexões HTTP e HTTPS:

     - `sudo ufw allow http`
    
    - `sudo ufw allow https`
 - Reinicie o serviço Apache
- `sudo service apache2 restart`

- Crie um diretório para o certificado
- `sudo mkdir /etc/apache2/ssl`
     
 - Crie um Certificado SSL autoassinado: Para conexões HTTPS, é necessário certificado SSL:

     - `sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt`

 
 - Configure o Apache para usar SSL
 - `sudo nano /etc/apache2/sites-available/default-ssl.conf `
 -  No arquivo de configuração, certifique-se de que as linhas abaixo apontam para o certificado e a chave que você acabou de gerar:
   
 SSLCertificateFile      /etc/apache2/ssl/apache.crt

 SSLCertificateKeyFile /etc/apache2/ssl/apache.key

 - Ative o site SSL
- `sudo a2ensite default-ssl.conf`

- Reinicie o Apache
- `sudo service apache2 restart`




