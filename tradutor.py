from langdetect import detect


def detectar_idioma(texto):
    try:
        return detect(texto)
    except:
        return "pt"


def precisa_traduzir_para_portugues(texto):
    idioma = detectar_idioma(texto)
    return idioma == "en"