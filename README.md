# Trabalho Final

Trabalho final da disciplina de Fundamentos de Redes de Computadores.

## Participantes

Nome Completo | Matrícula |
------------- | --------- |
Caio César Oliveira | 190085291 |
Guilherme Nishimura | 200030264 |
Matheus Costa Gomes | 190093331 |
Vitor Eduardo Kühl Rodrigues | 190 |

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

