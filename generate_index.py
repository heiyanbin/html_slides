import os
import subprocess
import time

def get_git_mtime(path, filename):
    """Return the last commit timestamp of the given file."""
    try:
        ts = subprocess.check_output(
            ["git", "log", "-1", "--format=%ct", "--", os.path.join(path, filename)],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        return int(ts)
    except subprocess.CalledProcessError:
        return 0  # fallback if not found

def generate_index(path="."):
    files = [
        f for f in os.listdir(path)
        if (
            not os.path.isdir(os.path.join(path, f)) and
            not f.startswith('.') and
            f.endswith(".html") and
            f != "index.html"
        )
    ]

    # ✅ 按 Git 提交时间倒序排列
    files.sort(key=lambda f: get_git_mtime(path, f), reverse=True)

    with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Slides Index</title>
<style>
body {font-family: sans-serif; max-width: 800px; margin: 2rem auto;}
table {width:100%; border-collapse:collapse;}
th, td {padding:0.5rem; border-bottom:1px solid #ddd;}
th {background:#f8f8f8;}
a {text-decoration:none; color:#007bff;}
a:hover {text-decoration:underline;}
</style>
</head>
<body>
<h1>Slides Index</h1>
<table>
<thead><tr><th>File</th><th>Last Commit</th></tr></thead>
<tbody>
''')

        for filename in files:
            ts = get_git_mtime(path, filename)
            mod_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
            link_text = os.path.splitext(filename)[0]
            f.write(f"<tr><td><a href='{filename}'>{link_text}</a></td><td>{mod_time}</td></tr>\n")

        f.write("</tbody></table></body></html>")

if __name__ == "__main__":
    generate_index(".")
