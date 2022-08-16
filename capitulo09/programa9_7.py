with open("página.html", "w", encoding="utf-8") as página:
    página.write("<!DOCTYPE html>\n")
    página.write("<html lang=\"pt-br\">\n")
    página.write("<head>\n")
    página.write("<meta charset=\"utf-8\">\n")
    página.write("<title>Página</title>\n")
    página.write("</head>\n")
    página.write("<body>\n")
    página.write("<h1>Olá!</h1>\n")
    for l in range(1, 10):
        página.write(f"<p>{l}</p>\n")
    página.write("</body>\n")
    página.write("</html>\n")
   