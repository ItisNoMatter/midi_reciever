# 環境構築
python3.9-32 windows

```
py -3.9-32 -m venv .venv  
.\.venv\Scripts\activate
pip install -r .\requirements.txt
```
# 動作確認
metronome.pyとmidi_input.pyは直接実行すると標準出力を使ったテストが走ります。
midi_input.pyは、PCがMIDI INPUTデバイスを認識している状態にしておく必要があります