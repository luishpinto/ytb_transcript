from youtube_transcript_api import YouTubeTranscriptApi

def deep_clean(text: str) -> str:
    return (
        text.replace('\xa0', ' ')
            .replace("\\", "'")
            .strip()
    )

def get_ytb_transcript(video_id, languages=['it', 'en', 'es']):

    try:
        ytt_api = YouTubeTranscriptApi()

        transcript = ytt_api.fetch(
            video_id,
            languages=languages,
            preserve_formatting=False
        )

        full_text = []

        for snippet in transcript:
            clean = deep_clean(snippet.text)
            full_text.append(clean)

        return " ".join(full_text)

    except Exception as e:
        print(f"Error fetching transcript for {video_id}: {e}")
        return None
