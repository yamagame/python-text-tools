## ソースコードについて

  XML形式の特許文書データを分析するためのサンプルコードです。

## 使用する文書

  下記URLからダウンロードした特許文書を使用します。

  https://www.publication.jpo.go.jp/index.action

## ダウンロードしたファイルの例（一部抜粋）

  ```
          :
    <technical-field>
    <p num="0001">
      本発明は、移動無線の基地局または端末、衛星通信および放送システムに用いられる....。<br/>
          :
    </technical-field>
          :
  ```

## 主に使うツール

  分析に使用するツールを紹介します。

### コマンド

  - python3

  - chmod
  
  - cat
  
  - find
  
  - grep
  
  - cut

  - sed

  - awk

  - ls

  - pwd

  - cd

#### UNIXコマンド使用例
  
  JPH_2018042 ディレクトリに含まれている、拡張子が pdf のファイルのファイルサイズの合計を計算する例です。

  ```bash
    $ find JPH_2018042 -name '*.pdf' -exec ls -l {} \; | cut -d' ' -f 7 | awk '{sum+=$1}END{print sum}'
  ```

### Pythonプログラム

  - readdir.py

    ディレクトリの中にあるある拡張子のファイルのリストを作成。
    拡張子は引数で指定可。

    find . -name '*.xml' と同意。

    ```
      $ ./readdir.py xml ./[ディレクトリ]
    ```

    実行例

    ```
      $ ./readdir.py xml ./JPH_2018042/
      ./JPH_2018042/DOCUMENT/B9/0006409001/0006409201/0006409211/0006409217.xml
      ./JPH_2018042/DOCUMENT/B9/0006409001/0006409901/0006409981/0006409984.xml
          :
    ```

  - xml2json.py

    xmlファイルをjson形式に変換

    ```
      $ ./readdir.py xml ./[ディレクトリ] | ./xml2json.py
    ```

    変換結果は、入力ファイルと同じ場所に、拡張子 .json で保存される。

    XMLファイルから以下のタグを抜き出す。

    - tech-problem
    - background-art
    - technical-field
    - tech-solution
    - description-of-drawings
    - description-of-embodiments
    - reference-signs-list
    - claim-text

    実行例

    ```
      $ ./readdir.py xml ./JPH_2018042/ | ./xml2json.py
      ./JPH_2018042/DOCUMENT/B9/0006409001/0006409201/0006409211/0006409217.json
      ./JPH_2018042/DOCUMENT/B9/0006409001/0006409901/0006409981/0006409984.json
          :
    ```

    出力ファイル例

    ```
      {
        "tech-problem": "上記のように、.....",
        "background-art": "本発明は、...",
        "technical-field": "本発明は、...",
        "description-of-drawings": "図１は、...",
        "description-of-embodiments": "本発明に関わる...",
        "reference-signs-list": "...",
        "claim-text": "ベースバンド変調信号の..."
      }
    ```

  - mecab.py

    json形式になったデータに含まれる文字列を形態素解析する。

    実行には mecab コマンドが必要。

    ```
      $ ./readdir.py json ./[ディレクトリ] | ./mecab.py
    ```

    変換結果は、入力ファイルと同じ場所に、拡張子 .mecab で保存される。

    実行例

    ```
      $ ./readdir.py json ./JPH_2018042/ | ./mecab.py
      ./JPH_2018042/DOCUMENT/B9/0006409001/0006409201/0006409211/0006409217.mecab
      ./JPH_2018042/DOCUMENT/B9/0006409001/0006409901/0006409981/0006409984.mecab
          :
    ```

    出力ファイル例

    ```
      上記	名詞,一般,*,*,*,*,上記,ジョウキ,ジョーキ
      の	助詞,連体化,*,*,*,*,の,ノ,ノ
      よう	名詞,非自立,助動詞語幹,*,*,*,よう,ヨウ,ヨー
      に	助詞,副詞化,*,*,*,*,に,ニ,ニ
          :
    ```

  - frequency.py

    文書に含まれている単語の頻度リストを作成する。

    ```
      $ ./readdir.py mecab ./[ディレクトリ] | ./frequency.py
    ```

    変換結果は、入力ファイルと同じ場所に、拡張子 .freq で保存される。

    実行例

    ```
      $ ./readdir.py mecab ./JPH_2018042/ | ./frequency.py
      ./JPH_2018042/DOCUMENT/B9/0006409001/0006409201/0006409211/0006409217.freq
      ./JPH_2018042/DOCUMENT/B9/0006409001/0006409901/0006409981/0006409984.freq
          :
    ```

    出力ファイル例

    ```
      、	1195	0.06728603603603604	記号
      の	880	0.04954954954954955	助詞
      信号	783	0.04408783783783784	名詞
      １	633	0.03564189189189189	名詞
      ２	575	0.03237612612612613	名詞
      と	558	0.03141891891891892	助詞
          :
    ```

    単語、回数、tf値、品詞のタブ区切りの文字列

    ※ tf値 = その単語のそのドキュメントでの出現回数 / そのドキュメントで出現したすべての単語の総数

  - ngram.py

    文書に含まれている単語のnグラムリストを作成する。N値のデフォルトは2。

    ```
      $ ./readdir.py mecab ./[ディレクトリ] | ./ngram.py
    ```

    変換結果は、入力ファイルと同じ場所に、拡張子 .2gram で保存される。

    N値は引数で変更できる。

    ```
      $ ./readdir.py mecab ./[ディレクトリ] | ./ngram.py 3
    ```

    上記の場合、変換結果は、入力ファイルと同じ場所に、拡張子 .3gram で保存される。

    実行例

    ```
      $ ./readdir.py mecab ./JPH_2018042/ | ./ngram.py 3
      ./JPH_2018042/DOCUMENT/B9/0006409001/0006409201/0006409211/0006409217.3gram
      ./JPH_2018042/DOCUMENT/B9/0006409001/0006409901/0006409981/0006409984.3gram
          :
    ```

    出力ファイル例

    ```
      複合	送信	機	150
      支援	信号	の	97
      主	信号	の	78
          :
    ```

## ToDo

  - ビジュアライズ
  - UNIXコマンド マニュアル

