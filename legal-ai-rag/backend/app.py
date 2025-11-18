from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from utils.loader import load_pdf, load_docx
from utils.embed import build_vector_store
from utils.rag import get_rag_response

app = Flask(__name__)
CORS(app)

UPLOAD_DIR = "backend/storage/uploaded_files"


@app.route("/ping", methods=["GET"])
def ping():
    return {"status": "ok"}, 200


@app.post("/upload")
def upload_docs():
    files = request.files.getlist("files")

    if len(files) > 5:
        return jsonify({"error": "Max 5 files allowed"}), 400

    docs_text = []

    for file in files:
        filepath = os.path.join(UPLOAD_DIR, file.filename)
        file.save(filepath)

        if file.filename.endswith(".pdf"):
            docs_text.append(load_pdf(filepath))
        elif file.filename.endswith(".docx"):
            docs_text.append(load_docx(filepath))
        else:
            return jsonify({"error": "Only .pdf and .docx allowed"}), 400

    build_vector_store(docs_text)
    return jsonify({"message": "Documents processed successfully"})


@app.post("/ask")
def ask():
    data = request.json
    question = data.get("question")
    answer = get_rag_response(question)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
