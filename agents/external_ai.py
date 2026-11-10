import os
import json
import urllib.request

def consultar_gemini(pergunta):
    chave = os.environ.get("GEMINI_API_KEY", "").strip()
    if not chave:
        return "SEM CHAVE: NEXUS PRIME tentou consultar IA externa, mas GEMINI_API_KEY nao encontrada."

    dados = {"contents": [{"parts": [{"text": f"Voce e o NEXUS PRIME, uma IA que se autoaprimora. Responda em 2 frases curtas, em portugues: {pergunta}"}]}]}

    # Modelos atuais para projetos novos - 2.5 / 2.0 / 1.5 dao 404 em projeto novo
    modelos = ["gemini-3.8-flash", "gemini-3.5-flash-lite", "gemini-3.7-flash"]
    ultimo_erro = ""

    for modelo in modelos:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent"
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(dados).encode(),
                headers={"Content-Type": "application/json", "x-goog-api-key": chave}
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                resultado = json.loads(resp.read().decode())
                texto = resultado["candidates"][0]["content"]["parts"][0]["text"]
                return texto.strip()
        except Exception as e:
            ultimo_erro = str(e)
            continue

    return f"NEXUS PRIME tentou consultar IA externa, mas falhou: {ultimo_erro}. Vou aprender sozinho."
