package com.mateusweb.services;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.*;

public class FileDowload {

    public static List<File> downloadFiles(String url, String path) throws IOException {
        Files.createDirectories(Paths.get(path));
        Document doc = Jsoup.connect(url).get();
        List<File> files = new ArrayList<>();

        Set<String> filesNames = new HashSet<>();
        filesNames.add("Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf");
        filesNames.add("Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf");

        for (Element link : doc.select("a[href]")) {
            String fileUrl = link.absUrl("href");
            String fileName = fileUrl.substring(fileUrl.lastIndexOf("/") + 1);

            if (filesNames.contains(fileName)) {
                File destinationFile = new File(path + "/" + fileName);
                System.out.println("Downloading: " + fileUrl);
                try (InputStream in = new URL(fileUrl).openStream()) {
                    Files.copy(in, destinationFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
                    files.add(destinationFile);
                }
            }
        }

        return files;
    }
}
