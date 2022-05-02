from flaskr import app
from flask import render_template

@app.route('/')
def index():
    blog = {
        'title': '技術ブログ',
        'category': 'プログラミング',
        'content': '関数',
        'code': 'def index():'
    }
    return render_template(
        'index.html',
        blog=blog
    )




# コードを挿入というボタンを作成し、
# そこを押すとコード入力フォームが本文中に表示されて、
# そこでコードを記載またはペーストできるようにする。
# コード入力は必須項目ではないので全く記載しない場合は、
# フォームは表示されないようにする。
# 5/2 flaskでpreを使ってWebブラウザ側に出力することに成功した。
# リストにしてfor文で回すことを考えると、
# codeはDjangoでいうmodelに登録しない仕様が良い。
# あくまで本文中の記載内容として処理するようにしたい。
# 本文中はテキストになっているため、
# 本文テキスト内の文字列をpre対応にできるようにできれば、
# この問題は簡単に解決する