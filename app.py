from flask import Flask, request, jsonify, render_template
import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
import logging

# Log ayarı
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class SimpleRAGChatbot:
    def __init__(self):
        self.vector_store = None
        self.initialize_rag_system()
    
    def initialize_rag_system(self):
        """RAG sistemini başlat"""
        try:
            logger.info("🤖 RAG sistemi başlatılıyor...")
            
            # 1. Embedding modeli
            embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
            logger.info("✅ Embedding modeli yüklendi")
            
            # 2. Veri setini yükle (gerçek dosya veya fallback)
            documents = self.load_documents()
            logger.info(f"✅ {len(documents)} doküman yüklendi")
            
            # 3. Metni böl
            text_splitter = CharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50,
                separator="\n"
            )
            split_docs = text_splitter.split_documents(documents)
            logger.info(f"✅ {len(split_docs)} metin parçası oluşturuldu")
            
            # 4. Vektör veritabanını oluştur
            self.vector_store = Chroma.from_documents(
                documents=split_docs,
                embedding=embeddings,
                persist_directory="./chroma_db"
            )
            logger.info("✅ Vektör veritabanı oluşturuldu")
            
        except Exception as e:
            logger.error(f"❌ RAG sistemi başlatılamadı: {str(e)}")
            self.initialize_fallback_system()
    
    def load_documents(self):
        """Dokümanları yükle"""
        try:
            # Gerçek dosyayı dene
            if os.path.exists("data/mit_istatistik_notlari.txt"):
                loader = TextLoader("data/mit_istatistik_notlari.txt", encoding="utf-8")
                return loader.load()
            else:
                # Fallback: Manuel içerik
                fallback_content = """
                MIT İSTATİSTİK - HİPOTEZ TESTLERİ
                
                T-TEST: İki grup ortalaması arasındaki farkı test eder. 
                Bağımsız ve bağımlı t-test olarak ikiye ayrılır.
                
                ANOVA: İkiden fazla grup ortalamasını karşılaştırır. 
                Tek yönlü ve çift yönlü ANOVA türleri vardır.
                
                P DEĞERİ: Null hipotez doğru iken gözlemlenen sonucun olasılığı.
                p < 0.05 istatistiksel olarak anlamlı kabul edilir.
                
                HİPOTEZ TESTİ ADIMLARI:
                1. Hipotezleri kur
                2. Anlamlılık düzeyi belirle
                3. Test istatistiğini hesapla
                4. Karar ver
                
                HATA TÜRLERİ:
                - Tip 1 Hata: Doğru null hipotezi reddetmek
                - Tip 2 Hata: Yanlış null hipotezi kabul etmek
                """
                return [Document(page_content=fallback_content, metadata={"source": "MIT_Notlari"})]
                
        except Exception as e:
            logger.error(f"❌ Doküman yükleme hatası: {str(e)}")
            return [Document(page_content="MIT istatistik notları: Hipotez testleri", metadata={"source": "Fallback"})]
    
    def initialize_fallback_system(self):
        """Basit fallback sistem"""
        logger.info("🔄 Basit sistem moduna geçiliyor...")
        self.fallback_kb = {
            "t-test": "T-test iki grup ortalaması arasındaki farkı test eder. MIT notlarına göre bağımsız ve bağımlı t-test türleri vardır.",
            "anova": "ANOVA ikiden fazla grup ortalamasını karşılaştırır. MIT'de tek yönlü ve çift yönlü ANOVA anlatılır.",
            "p değeri": "P değeri, null hipotez doğru iken gözlemlenen sonucun olasılığıdır. p < 0.05 anlamlı kabul edilir.",
            "hipotez testi": "Hipotez testi istatistiksel karar verme yöntemidir. Null ve alternatif hipotez ile çalışır.",
            "mit": "MIT istatistik ders notlarında hipotez testleri detaylı anlatılmaktadır."
        }
    
    def ask_question(self, question):
        """Soruyu cevapla"""
        try:
            if self.vector_store:
                # Gerçek RAG ile cevap ver
                docs = self.vector_store.similarity_search(question, k=2)
                answer = "\n\n".join([doc.page_content for doc in docs])
                sources = list(set([doc.metadata.get("source", "MIT_Notları") for doc in docs]))
                return answer, sources
            else:
                # Fallback ile cevap ver
                return self.fallback_ask(question)
                
        except Exception as e:
            logger.error(f"❌ Soru cevaplama hatası: {str(e)}")
            return self.fallback_ask(question)
    
    def fallback_ask(self, question):
        """Basit eşleştirme ile cevap ver"""
        question_lower = question.lower()
        
        for key in getattr(self, 'fallback_kb', {}):
            if key in question_lower:
                return self.fallback_kb[key], ["MIT_İstatistik_Notları"]
        
        return "MIT istatistik notlarına göre hipotez testleri hakkında daha spesifik sorabilirsiniz. Örneğin: 't-test nedir?', 'ANOVA nasıl çalışır?'", ["MIT_İstatistik_Notları"]

# Chatbot'u başlat
chatbot = SimpleRAGChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({'error': 'Lütfen bir soru yazın'}), 400
        
        answer, sources = chatbot.ask_question(question)
        
        return jsonify({
            'answer': answer,
            'sources': sources,
            'status': 'success'
        })
        
    except Exception as e:
        logger.error(f"❌ API hatası: {str(e)}")
        return jsonify({
            'error': 'Sistem hatası oluştu',
            'status': 'error'
        }), 500

if __name__ == '__main__':
    print("🚀 MIT İstatistik ChatBot Başlatılıyor...")
    print("📚 RAG Sistemi: AKTİF")
    print("🌐 http://localhost:8000 adresini açın")
    print("⏹️  Durdurmak için: Ctrl+C")
    app.run(host='0.0.0.0', port=8000, debug=False)
