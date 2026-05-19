
from flask import render_template, request, redirect, url_for
from app.models import RentalReport


def register_routes(app):

    @app.route("/")
    def home():
        reports = RentalReport.get_all()

        return render_template(
            "index.html",
            reports=reports
        )

    @app.route("/submit", methods=["GET", "POST"])
    def submit_report():

        if request.method == "POST":
            apartment_name = request.form["apartment_name"]
            city = request.form["city"]
            state = request.form["state"]
            rent_price = request.form["rent_price"]
            rating = request.form["rating"]
            review = request.form["review"]

            RentalReport.create(
                apartment_name,
                city,
                state,
                rent_price,
                rating,
                review
            )

            return redirect(url_for("home"))

        return render_template("submit.html")

    @app.route("/search")
    def search():

        city = request.args.get("city")
        apartment_name = request.args.get("apartment_name")

        reports = RentalReport.search(
            city=city,
            apartment_name=apartment_name
        )

        return render_template(
            "search.html",
            reports=reports,
            city=city,
            apartment_name=apartment_name
        )
