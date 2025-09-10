import os

def generate_index(path="."):
    files = os.listdir(path)
    files.sort()

    with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>\n")
        f.write("<title>目录列表</title>\n</head>\n<body>\n")
        f.write("<h1>目录列表</h1>\n<ul>\n")

        for file in files:
            if file == "index.html":
                continue
            f.write(f"<li><a href='{file}'>{file}</a></li>\n")

        f.write("</ul>\n</body>\n</html>")

if __name__ == "__main__":
    generate_index(".")
