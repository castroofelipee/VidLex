from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pytube import YouTube
import os
import speech_recognition as sr
from moviepy.editor import AudioFileClip
from pydub import AudioSegment

app = FastAPI()

class VideoRequest(BaseModel):
    url: str
    words: list[str]

def transcribe_segment(audio_segment, recognizer):
    with sr.AudioFile(audio_segment) as source:
        audio_data = recognizer.record(source)
    return recognizer.recognize_sphinx(audio_data)

@app.post("/transcribe/")
async def transcribe_video(request: VideoRequest):
    try:
        yt = YouTube(request.url)
        stream = yt.streams.filter(only_audio=True).first()
        audio_file = stream.download(filename="audio.mp4")

        
        clip = AudioFileClip(audio_file)
        audio_path = "audio.wav"
        clip.write_audiofile(audio_path)

        
        recognizer = sr.Recognizer()
        audio = AudioSegment.from_wav(audio_path)
        segment_duration = 30000  
        results = []

        for i in range(0, len(audio), segment_duration):
            segment = audio[i:i + segment_duration]
            segment_path = f"segment_{i//segment_duration}.wav"
            segment.export(segment_path, format="wav")
            try:
                transcript = transcribe_segment(segment_path, recognizer).lower()
                for word in request.words:
                    if word.lower() in transcript:
                        start_time = i / 1000
                        results.append({"word": word, "timestamp": start_time})
            except sr.UnknownValueError:
                pass  
            os.remove(segment_path)


        os.remove(audio_path)
        os.remove("audio.mp4")

        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
