from flask import Flask, render_template
from backend.routes.prediction_routes import predict_bp

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

# Register Blueprint
app.register_blueprint(predict_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
