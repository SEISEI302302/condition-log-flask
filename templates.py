# templates.py
HTML = """
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>コンディションログ</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; max-width: 800px; margin: 24px auto; padding: 0 16px; }
    h1 { margin-bottom: 8px; }
    .hint { color: #666; margin-top: 0; }
    form { display: grid; gap: 10px; padding: 12px; border: 1px solid #ddd; border-radius: 10px; }
    label { display: inline-block; min-width: 100px; }
    input[type="number"], input[type="text"] { width: 100%; padding: 8px; }
    .row { display: grid; grid-template-columns: 120px 1fr; gap: 10px; align-items: center; }
    button { padding: 10px 12px; border: none; border-radius: 8px; cursor: pointer; }
    ul { padding-left: 18px; }
    li { margin: 8px 0; }
    .meta { color: #555; }
  </style>
</head>
<body>
  <h1>コンディションログ</h1>
  <p class="hint">体力・心・メモを記録できます（再起動しても残ります）。</p>

  <form method="post" action="/add">
    <div class="row">
      <label>体力 (1〜10)</label>
      <input name="energy" type="number" min="1" max="10" required>
    </div>
    <div class="row">
      <label>心 (1〜10)</label>
      <input name="mind" type="number" min="1" max="10" required>
    </div>
    <div class="row">
      <label>メモ</label>
      <input name="note" type="text" maxlength="200" placeholder="例：パルクール行けた、睡眠浅い など">
    </div>
    <button type="submit">記録する</button>
  </form>

  <hr>

  <h2>記録一覧（新しい順）</h2>
  {% if logs %}
    <ul>
      {% for item in logs %}
        <li>
          <span class="meta">{{ item["time"] }}</span>
          / 体力: {{ item["energy"] }}
          / 心: {{ item["mind"] }}
          {% if item["note"] %} / メモ: {{ item["note"] }}{% endif %}
        </li>
        <form method="post" action="/delete/{{ item['id'] }}" style="display:inline;">
  <button type="submit">🗑 削除</button>
</form>
<a href="/edit/{{ item['id'] }}">✏️ 編集</a>
      {% endfor %}
    </ul>
  {% else %}
    <p>まだ記録がありません。</p>
  {% endif %}
</body>
</html>
"""
EDIT_HTML = """
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>記録の編集</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <h1>記録の編集</h1>

  <form method="post" action="/update/{{ log['id'] }}">
    <label>体力 (1〜10)</label><br>
    <input type="number" name="energy" min="1" max="10" value="{{ log['energy'] }}" required><br><br>

    <label>心 (1〜10)</label><br>
    <input type="number" name="mind" min="1" max="10" value="{{ log['mind'] }}" required><br><br>

    <label>メモ</label><br>
    <input type="text" name="note" value="{{ log['note'] or '' }}"><br><br>

    <button type="submit">保存</button>
  </form>

  <p><a href="/">← 一覧に戻る</a></p>
</body>
</html>
"""
