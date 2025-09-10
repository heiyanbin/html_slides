import os

def generate_index(path="."):
    """
    Generates an index.html file for the current directory.
    It lists all non-hidden HTML files, skipping directories and the index files themselves.
    """
    files = os.listdir(path)
    files.sort()

    with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
        # HTML header and styles
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Slides Index</title>
    <style>
        body {
            font-family: sans-serif;
            max-width: 800px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        h1 {
            text-align: center;
            border-bottom: 1px solid #eee;
            padding-bottom: 0.5rem;
            margin-bottom: 2rem;
            font-weight: normal;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        a {
            text-decoration: none;
            color: #007bff;
            display: block;
            padding: 0.2rem 0;
            font-size: 1.1rem;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Slides Index</h1>
    <ul>
''')

        for filename in files:
            # Skip directories, hidden files, and non-HTML files
            if (os.path.isdir(os.path.join(path, filename)) or
                    filename.startswith('.') or
                    not filename.endswith(".html") or
                    filename == "index.html"):
                continue
            
            # Use the filename without extension as the link text
            link_text = os.path.splitext(filename)[0]
            f.write(f"        <li><a href='{filename}'>{link_text}</a></li>\n")

        f.write("    </ul>\n</body>\n</html>")

if __name__ == "__main__":
    generate_index(".")