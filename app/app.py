from flask import Flask, render_template
from src.data.load_data import load_data, get_summary

app = Flask(__name__)


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    return render_template("home.html")


# ============================================================
# DATASET PAGE
# ============================================================

@app.route("/dataset")
def dataset():
    df = load_data()
    summary = get_summary(df)

    return render_template(
        "load_dataset.html",
        summary=summary,
        first_rows=df.head().to_html(index=False)
    )


# ============================================================
# PREPROCESSING PAGE
# ============================================================

@app.route("/preprocessing")
def preprocessing():
    return render_template("preprocessing.html")


# ============================================================
# EDA PAGE
# ============================================================

@app.route("/eda")
def eda():
    return render_template("eda.html")


# ============================================================
# MACHINE LEARNING MODELS PAGE
# ============================================================

@app.route("/models")
def models():
    return render_template("models.html")


# ============================================================
# PREDICTION PAGE
# ============================================================

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")


# ============================================================
# EVALUATION PAGE
# ============================================================

@app.route("/evaluation")
def evaluation():
    return render_template("evalution.html")


# Keep your old URL also working
@app.route("/evalution")
def evalution():
    return render_template("evalution.html")


# ============================================================
# MODEL COMPARISON PAGE
# ============================================================

@app.route("/comparison")
def comparison():
    return render_template("comparison.html")


# ============================================================
# PROFILE PAGE
# ============================================================

@app.route("/profile")
def profile():
    return render_template("profile.html")


# ============================================================
# RUN FLASK APPLICATION
# ============================================================

if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )