from flask import Flask, render_template
import requests
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd8c0e8f1c1d09e9ecf54795c17e11fb3'
app.config['STATIC_FOLDER'] = 'static'
app.debug = True


def api_data(category):
    url = f'https://newsapi.org/v2/{category}&apiKey=d6b3a63000d04b91b2b2c1391dcfdd97'
    response = requests.get(url)
    data = response.json()
    return data


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", tech=api_data("top-headlines?sources=techcrunch"),
                            business=api_data("top-headlines?country=us&category=business"),
                              wallstreet=api_data("everything?domains=wsj.com"),
                              popular = api_data("everything?q=apple&from=2023-03-23&to=2023-03-23&sortBy=popularity"),
                              tesla = api_data("everything?q=tesla&from=2023-02-24&sortBy=publishedAt"))
@app.route('/trending')
def trending():
    return render_template("trending.html", tesla = api_data("everything?q=tesla&from=2023-02-24&sortBy=publishedAt" ),
                           wallstreet = api_data("everything?domains=wsj.com"))
@app.route('/business')
def business():
    return render_template("business.html", business = api_data("top-headlines?country=us&category=business" ),
                           apple = api_data("everything?q=apple&from=2023-03-23&to=2023-03-23&sortBy=popularity"))

if __name__ == '__main__':
    app.run()
