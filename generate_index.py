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
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 2rem auto;
            padding: 0 1rem;
            background-color: #fdfdfd;
        }
        h1 {
            text-align: center;
            color: #2c3e50;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 0.5rem;
            margin-bottom: 2rem;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            margin-bottom: 0.8rem;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.08);
            transition: all 0.2s ease-in-out;
        }
        li:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 12px rgba(0,0,0,0.12);
        }
        a {
            text-decoration: none;
            color: #3498db;
            display: block;
            padding: 1rem 1.5rem;
            font-size: 1.1rem;
            font-weight: 500;
        }
        a:hover {
            color: #2980b9;
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