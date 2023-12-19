#!/bin/bash

# Atualize os pacotes existentes
sudo apt-get update

# Ative o módulo SSL do Apache
sudo a2enmod ssl

# Configure o Firewall para permitir conexões HTTP e HTTPS
sudo ufw allow http
sudo ufw allow https


# Reinicie o serviço Apache
sudo service apache2 restart

# Crie um diretório para o certificado
sudo mkdir /etc/apache2/ssl

# Crie um certificado autoassinado
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/apache.key -out /etc/apache2/ssl/apache.crt

# Você será solicitado a inserir detalhes como país, estado, etc. 
# O mais importante é "Common Name", insira o nome de domínio do seu site ou, em caso de certificado local, seu endereço IP

# Configure o Apache para usar SSL
sudo nano /etc/apache2/sites-available/default-ssl.conf

# No arquivo de configuração, certifique-se de que as linhas abaixo apontam para o certificado e a chave que você acabou de gerar:
# SSLCertificateFile      /etc/apache2/ssl/apache.crt
# SSLCertificateKeyFile /etc/apache2/ssl/apache.key

# Ative o site SSL
sudo a2ensite default-ssl.conf

# Reinicie o Apache
sudo service apache2 restart
