package com.mateusweb.services;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class FileZip {

    public static void zipfile(String outputfile, String[] inputfiles) throws IOException {
        try (
                FileOutputStream destino = new FileOutputStream(new File(outputfile));
                ZipOutputStream out = new ZipOutputStream(destino)
        ) {
            for (String inputfile : inputfiles) {
                File file = new File(inputfile);
                if (!file.exists()) {
                    System.err.println("file not found: " + inputfile);
                    continue;
                }

                try (FileInputStream streamDeEntrada = new FileInputStream(file)) {
                    ZipEntry entry = new ZipEntry(file.getName());
                    out.putNextEntry(entry);

                    byte[] buffer = new byte[8192];
                    int bytesRead;
                    while ((bytesRead = streamDeEntrada.read(buffer)) != -1) {
                        out.write(buffer, 0, bytesRead);
                    }

                    out.closeEntry();
                }
            }
        }
    }
}