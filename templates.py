# templates.py 
HTML = """
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>コンディションログ</title>
  <link rel="stylesheet" href="/static/style.css?v=999">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <main>
    <h1>コンディションログ</h1>
    <p class="hint">体力・心・メモを記録できます（再起動しても残ります）。</p>

    <div class="card">
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
    </div>

    <h2 style="margin-top:16px;">記録一覧（新しい順）</h2>

    {% if logs %}
      <div class="list">
        {% for item in logs %}
          <div class="item">
            <div class="item-head">
              <span class="meta">{{ item["time"] }}</span>
              <span class="meta">体力 {{ item["energy"] }} / 心 {{ item["mind"] }}</span>
            </div>

            {% if item["note"] %}
              <div class="note">メモ：{{ item["note"] }}</div>
            {% endif %}

            <div class="actions">
              <a class="btn" href="/edit/{{ item['id'] }}">✏️ 編集</a>

              <form method="post" action="/delete/{{ item['id'] }}" style="margin:0;">
                <button class="delete" type="submit">🗑 削除</button>
              </form>
            </div>
          </div>
        {% endfor %}
      </div>
    {% else %}
      <p>まだ記録がありません。</p>
    {% endif %}
  </main>
</body>
</html>
"""
EDIT_HTML = """
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>記録の編集</title>
  <link rel="stylesheet" href="/static/style.css?v=999">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <main>
    <h1>記録の編集</h1>

    <div class="card">
      <form method="post" action="/update/{{ log['id'] }}">
        <div class="row">
          <label>体力 (1〜10)</label>
          <input type="number" name="energy" min="1" max="10" value="{{ log['energy'] }}" required>
        </div>

        <div class="row">
          <label>心 (1〜10)</label>
          <input type="number" name="mind" min="1" max="10" value="{{ log['mind'] }}" required>
        </div>

        <div class="row">
          <label>メモ</label>
          <input type="text" name="note" value="{{ log['note'] or '' }}" maxlength="200">
        </div>

        <div class="actions">
          <button type="submit">保存</button>
          <a class="btn" href="/">← 一覧に戻る</a>
        </div>
      </form>
    </div>
  </main>
</body>
</html>
"""
