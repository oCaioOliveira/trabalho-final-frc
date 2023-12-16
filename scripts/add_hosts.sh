#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Este script precisa ser executado como superusuário (root)." 
  exit 1
fi

endereco_ip="127.0.0.1"

nome_do_dominio="trabalho-final-redes-cgmv.com"

if grep -q "$nome_do_dominio" /etc/hosts; then
  echo "O domínio já está mapeado no arquivo hosts."
  exit 0
fi

echo "$endereco_ip $nome_do_dominio" >> /etc/hosts
echo "Mapeamento adicionado para $nome_do_dominio"

