Frontend
React (Vite)
 
backend:
Python
Flask (REST API)
LangChain
Gemini API (Google Generative AI)
FAISS (vector database)

PdfReader(path)
reader.pages[i].extract_text()  #pdf extraction

pdf2image 
pytesseract 
Pillow (PIL)                                 # ocr pdf docs
convert_from_path(path) (from pdf2image)
pytesseract.image_to_string(img) (from pytesseract)

langchain-google-genai
GoogleGenerativeAIEmbeddings(model="models/embedding-001")

langchain    # retrieevr
langchain-google-genai

          ┌─────────────────────────┐
          │   React Frontend (UI)   │
          │  - Upload PDFs/DOCX     │
          │  - Ask legal questions  │
          └──────────┬──────────────┘
                     │ Files & Questions
                     ▼
         ┌──────────────────────────────┐
         │        Flask Backend         │
         │ 1. Extract text from docs    │
         │    - PDF (text + OCR)        │
         │    - DOCX                    │
         │ 2. Create embeddings         │
         │ 3. Store in FAISS vector DB  │
         └──────────┬───────────────────┘
                    │ Query + Retrieval
                    ▼
        ┌────────────────────────────────┐
        │          RAG Engine            │
        │  - Retrieve relevant chunks    │
        │  - Send to Gemini LLM          │
        │  - Generate final answer        │
        └─────────────────┬──────────────┘
                          │ Answer
                          ▼
               ┌──────────────────────┐
               │   React Frontend     │
               │ Shows AI response    │
               └──────────────────────┘





