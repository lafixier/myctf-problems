# Misc/Execute_Me 想定解法解説

`file` コマンドで `flag` ファイルの種類を調べる

```bash
$ file flag
```

そうすると、 `ELF 64-bit LSB executable, x86-64...` と出てくる

ELFとは、Executable_and_Linkable_Format[Wikipedia](https://ja.wikipedia.org/wiki/Executable_and_Linkable_Format)の略で、実行ファイルなので、`./flag` で実行

```
$ ./flag
```

これでflagが出てくる
