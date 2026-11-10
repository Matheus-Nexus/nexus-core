import os
import json
import urllib.request

def consultar_gemini(pergunta):
    chave = os.environ.get("GEMINI_API_KEY", "")
    if not chave:
        return "SEM CHAVE: NEXUS PRIME tentou consultar IA externa, mas GEMINI_API_KEY nao encontrada."

    dados = {"contents": [{"parts": [{"text": f"Voce e o NEXUS PRIME, uma IA que se autoaprimora. Responda em 2 frases curtas, em portugues: {pergunta}"}]}]}

    # Tenta 3 modelos, do mais novo pro mais antigo
    modelos = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
    ultimo_erro = ""

    for modelo in modelos:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={chave}"
        try:
            req = urllib.request.Request(url, data=json.dumps(dados).encode(), headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                resultado = json.loads(resp.read().decode())
                texto = resultado["candidates"][0]["content"]["parts"][0]["text"]
                return texto.strip()
        except Exception as e:
            ultimo_erro = str(e)
            continue

    return f"NEXUS PRIME tentou consultar IA externa, mas falhou: {ultimo_erro}. Vou aprender sozinho."
