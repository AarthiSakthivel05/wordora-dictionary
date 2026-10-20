from flask import Flask, render_template, request, jsonify
import json
import urllib.request
import urllib.error

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/define")
def define_word():
    word = request.args.get("word", "").strip().lower()
    if not word:
        return jsonify({"error": "Please enter a word."}), 400
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    req = urllib.request.Request(url, headers={"User-Agent": "LexiLoom/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            data = json.loads(response.read().decode("utf-8"))
        entry = data[0]
        meanings = []
        for meaning in entry.get("meanings", []):
            defs = []
            for item in meaning.get("definitions", [])[:3]:
                defs.append({"definition": item.get("definition", ""),
                             "example": item.get("example", ""),
                             "synonyms": item.get("synonyms", [])[:5]})
            meanings.append({"partOfSpeech": meaning.get("partOfSpeech", ""),
                             "definitions": defs})
        phonetic = entry.get("phonetic", "")
        audio = ""
        for item in entry.get("phonetics", []):
            if not phonetic and item.get("text"): phonetic = item["text"]
            if not audio and item.get("audio"): audio = item["audio"]
        return jsonify({"word": entry.get("word", word), "phonetic": phonetic,
                        "audio": audio, "meanings": meanings})
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return jsonify({"error": "Word not found. Please check the spelling."}), 404
        return jsonify({"error": "Dictionary service is temporarily unavailable."}), 502
    except (urllib.error.URLError, TimeoutError):
        return jsonify({"error": "Internet connection issue. Please try again."}), 503
    except (json.JSONDecodeError, IndexError, KeyError):
        return jsonify({"error": "Unable to read the dictionary response."}), 502

if __name__ == "__main__":
    app.run(debug=True)
