package com.mateusweb;

import com.mateusweb.services.FileDowload;
import com.mateusweb.services.FileZip;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {


        FileDowload.downloadFiles("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos", "downloads");
        FileZip.zipfile("downloads//my_files.zip", new String[]{"downloads/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf", "downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"});

    }
}