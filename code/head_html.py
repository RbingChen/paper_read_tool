# 生成垂直列布局的 head.html
with open('head.html', 'w') as f:
    f.write("""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>页面索引</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 300px;
            margin: 20px auto;
            padding: 20px;
        }
        .page-list {
            list-style-type: none;
            padding: 0;
        }
        .page-item {
            margin: 10px 0;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }
        .page-link {
            display: block;
            padding: 10px;
            text-decoration: none;
            color: #333;
            transition: all 0.3s;
            border-left: 3px solid transparent;
        }
        .page-link:hover {
            background-color: #f9f9f9;
            border-left: 3px solid #4CAF50;
            padding-left: 15px;
        }
        .header {
            text-align: center;
            color: #444;
            margin-bottom: 25px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h2>页面索引</h2>
        <p>点击跳转到对应页面</p>
    </div>
    
    <ul class="page-list">
""")

    # 生成 0-10 的垂直列表链接
    for i in range(100):
        f.write(f"""        <li class="page-item">
            <a class="page-link" href="{i}.html">→ 页面 {i}</a>
        </li>\n""")

    f.write("""    </ul>
</body>
</html>""")

print("head.html 文件生成成功！")