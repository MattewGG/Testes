package com.mateusweb;

import com.mateusweb.services.FileDowload;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {


        FileDowload.downloadFiles("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos", "downloads");

    }
}