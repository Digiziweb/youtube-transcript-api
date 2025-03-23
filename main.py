from flask import Flask, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["100 per hour"])

@app.route("/api/transcript/<video_id>")
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([line['text'] for line in transcript])
        return jsonify({
            "status": "success",
            "transcript": text,
            "video_id": video_id
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "video_id": video_id
        }), 400

if __name__ == "__main__":
    app.run(debug=True)
