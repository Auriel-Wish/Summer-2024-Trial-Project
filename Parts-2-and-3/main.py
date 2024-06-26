# Auriel Wish
# Trial Project: Summer 2024 Internship
#
# backend.py
# ----------------------------------------------------------------
from flask import Flask, request, jsonify, render_template
from funcs import eval_argument_premade, eval_argument_IBM, breakdown_argument, summarize, get_feedback, compare

app = Flask(__name__)

# model1 = load_model_classification("chkla/roberta-argument")
# model2 = load_model_classification("aurielwish/trial-project")
# model3 = load_model_classification("raruidol/ArgumentMining-EN-ARI-AIF-RoBERTa_L")
# model4 = load_model_summarization("Falconsai/text_summarization")
# model5 = load_model_generation("TinyLlama/TinyLlama-1.1B-Chat-v1.0")

# Initial webpage
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize_arg", methods=["POST"])
def summarize_arg():
    user_argument = request.form["user_argument"]
    ret = summarize(user_argument)
    return jsonify(ret)

# Get the argument and return its evaluation (model 1)
@app.route("/get_analysis_premade", methods=["POST"])
def get_analysis_premade():
    user_argument = request.form["user_argument"]
    eval = eval_argument_premade(user_argument)
    breakdown = breakdown_argument(user_argument)
    ret = [eval, breakdown]
    return jsonify(ret)

# Get the argument and return its evaluation (model 2)
@app.route("/get_analysis_IBM", methods=["POST"])
def get_analysis_IBM():
    user_argument = request.form["user_argument"]
    eval = eval_argument_IBM(user_argument)
    breakdown = breakdown_argument(user_argument)
    ret = [eval, breakdown]
    return jsonify(ret)

# Get more in dpeth analysis of argument from chatbot
@app.route("/in_depth", methods=["POST"])
def in_depth():
    user_argument = request.form["user_argument"]
    arg_score = float(request.form["arg_qual"])
    feedback = get_feedback(user_argument, arg_score)
    return jsonify(feedback)

@app.route("/get_comparison", methods=["POST"])
def get_comparison():
    user_argument2 = request.form["user_argument2"]
    user_argument3 = request.form["user_argument3"]
    comparison = compare(user_argument2, user_argument3)
    return jsonify(comparison)

# Run application
if __name__ == "__main__":
    app.run()