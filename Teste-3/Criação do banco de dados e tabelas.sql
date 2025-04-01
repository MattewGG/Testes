

create database TesteTres;
CREATE DATABASE TesteTres CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE TesteTres;


CREATE TABLE operadoras (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(50) NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(9),
    ddd VARCHAR(2),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_comercializacao VARCHAR(50),
    data_registro DATE,
    UNIQUE KEY (registro_ans),
    FULLTEXT INDEX idx_fulltext_search (razao_social, nome_fantasia, cidade)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    registro_ans VARCHAR(50) NOT NULL,        
    cd_conta_contabil VARCHAR(50) NOT NULL,
    descricao VARCHAR(500) NOT NULL,          
    vl_saldo_inicial NUMERIC(15,2),
    vl_saldo_final NUMERIC(15,2),
    data_importacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_registro_ans (registro_ans),
    INDEX idx_data (data)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
