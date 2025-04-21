import os
import json
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def load_data(file_name):
    with open(os.path.join('data', file_name)) as f:
        return json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message", "").lower()

    jobs = load_data("jobs.json")
    events = load_data("events.json")
    mentorships = load_data("mentorships.json")

    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return jsonify({"response": "Hello! I'm ASHA 🤖, your career buddy. Ask me about <b>jobs</b>, <b>events</b>, or <b>mentorship programs</b>!"})

    elif "job" in user_input:
        selected_jobs = random.sample(jobs, min(5, len(jobs)))
        response = "<br><br>".join([
            f"👩‍💻 <b>{job['job_title']}</b> at <b>{job['company_name']}</b> – {job['location']}<br>"
            f"apply_link: {job['apply_link']}<br>"
            f"Posted: {job['posted']}"
            for job in selected_jobs
        ])
        return jsonify({"response": response})

    elif "event" in user_input:
        response = "<br><br>".join([
            f"📅 <b>{e['name']}</b> on {e['date']} at {e['time']}<br>"
            f"📍 Venue: {e['venue']}"
            for e in events
        ])
        return jsonify({"response": response})

    elif "mentor" in user_input or "mentorship" in user_input:
        response = "<br><br>".join([
            f"👩‍🏫 <b>{m['mentor']}</b> – {m['area']}<br>{m['description']}"
            for m in mentorships
        ])
        return jsonify({"response": response})

    else:
        return jsonify({"response": "I'm not sure about that. Try asking about <b>jobs</b>, <b>events</b>, or <b>mentorship</b>. 💡"})

if __name__ == "__main__":
    app.run(debug=True)
