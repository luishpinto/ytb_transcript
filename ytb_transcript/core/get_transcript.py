from youtube_transcript_api import YouTubeTranscriptApi


def deep_clean(text: str) -> str:
    """
    Normalizza il testo dei segmenti transcript.

    Pulisce caratteri indesiderati e spaziatura.

    Args:
        text:
            Testo grezzo del transcript.

    Returns:
        Testo normalizzato.
    """

    return (
        text.replace("\xa0", " ")   # non-breaking spaces
            .replace("\\", "'")     # fix apostrofi/escape anomali
            .strip()                # rimuove spazi esterni
    )


def get_ytb_transcript(
    video_id: str,
    languages: list[str] | None = None
) -> str | None:
    """
    Recupera il transcript completo di un video YouTube.

    Prova le lingue in ordine di priorità.

    Args:
        video_id:
            ID del video YouTube.

        languages:
            Lingue preferite per il transcript.
            Default: italiano, inglese, spagnolo.

    Returns:
        Transcript completo come stringa,
        oppure None in caso di errore.
    """

    # Evita mutable default arguments
    if languages is None:
        languages = ["it", "en", "es"]

    try:
        print(
            f"[CESARE] Recupero transcript YouTube "
            f"per video: {video_id}"
        )

        # Istanzia client transcript API
        ytt_api = YouTubeTranscriptApi()

        # Recupera transcript disponibile
        transcript = ytt_api.fetch(
            video_id,
            languages=languages,
            preserve_formatting=False
        )

        full_text = []

        # Ricostruisce transcript completo
        # pulendo ogni snippet
        for snippet in transcript:
            clean_text = deep_clean(
                snippet.text
            )
            full_text.append(
                clean_text
            )

        return " ".join(full_text)

    except Exception as e:
        print(
            f"[CESARE] Errore recuperando "
            f"transcript per {video_id}: {e}"
        )
        return None
