from flask import Flask, render_template, request

aplikasi = Flask(__name__)

@aplikasi.route("/")
def app():
    return render_template("persegi.html")

@aplikasi.route("/send", methods=["POST"])
def send(sum=sum):
    if request.method == "POST":
        persegi = request.form["persegi"]
        sum = float(persegi)
        sum2 = float(persegi)
        sum3 = sum * sum
        sum4 = sum * 4
        return render_template("persegi.html", sum=sum3, sum2=sum4)
    else:
        return render_template("persegi.html")

if __name__ == '__main__':
    aplikasi.run(debug=True)
