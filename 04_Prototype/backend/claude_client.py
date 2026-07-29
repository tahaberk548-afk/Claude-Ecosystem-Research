def analyze_cve(cve_id):

    prompt = f"""
    Aşağıdaki CVE kaydını analiz et:

    {cve_id}

    Risk seviyesini,
    açıklamasını
    ve çözüm önerisini belirt.
    """

    return {
        "prompt_used": prompt,
        "result": "Claude analiz sonucu burada gösterilecek."
    }