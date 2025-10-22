import os
import time

def generate_index(path="."):
    """
    Generates an index.html file for the current directory.
    Lists all non-hidden HTML files (except index.html) in a table
    sorted by last modified time (newest first).
    """
    files = [
        f for f in os.listdir(path)
        if (
            not os.path.isdir(os.path.join(path, f)) and
            not f.startswith('.') and
            f.endswith(".html") and
            f != "index.html"
        )
    ]

    # 按修改时间倒序排列
    files.sort(key=lambda f: os.path.getmtime(os.path.join(path, f)), reverse=True)

    with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
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
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            text-align: left;
            padding: 0.5rem;
            border-bottom: 1px solid #ddd;
        }
        th {
            background: #f8f8f8;
        }
        a {
            text-decoration: none;
            color: #007bff;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Slides Index</h1>
    <table>
        <thead>
            <tr><th>Slides</th><th>Last Modified</th></tr>
        </thead>
        <tbody>
''')

        for filename in files:
            fullpath = os.path.join(path, filename)
            mod_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(fullpath)))
            link_text = os.path.splitext(filename)[0]
            f.write(f"            <tr><td><a href='{filename}'>{link_text}</a></td><td>{mod_time}</td></tr>\n")

        f.write('''        </tbody>
    </table>
</body>
</html>''')

if __name__ == "__main__":
    generate_index(".")
