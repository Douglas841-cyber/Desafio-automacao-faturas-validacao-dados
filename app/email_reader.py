from imap_tools import MailBox, AND
import os
from dotenv import load_dotenv

load_dotenv()

def buscar_emails_com_fatura(simulado=False):
    if simulado:
        print("⚠️  Modo simulado: retornando PDFs de exemplo.")
        return ["fatura1.pdf"]

    email = os.getenv("EMAIL_USER")
    senha = os.getenv("EMAIL_PASS")
    servidor = os.getenv("EMAIL_SERVER", "imap.gmail.com")

    print(f"🔐 Conectando ao e-mail {email} via {servidor}...")

    os.makedirs("anexos", exist_ok=True)
    anexos_pdf = []

    with MailBox(servidor).login(email, senha, initial_folder="INBOX") as mailbox:
        print("📥 Buscando e-mails não lidos com anexos...")

        # Busca e-mails não lidos, do mais novo para o mais antigo
        for msg in mailbox.fetch(AND(seen=False), reverse=True, limit=10):
            print(f"📧 E-mail encontrado: {msg.subject}")
            for anexo in msg.attachments:
                print(f"📎 Anexo encontrado: {anexo.filename}")
                if anexo.filename and anexo.filename.lower().endswith(".pdf"):
                    caminho = f"anexos/{anexo.filename}"
                    with open(caminho, "wb") as f:
                        f.write(anexo.payload)
                    print(f"✅ PDF salvo: {caminho}")
                    anexos_pdf.append(caminho)

    print(f"📊 Total de PDFs encontrados: {len(anexos_pdf)}")
    return anexos_pdf