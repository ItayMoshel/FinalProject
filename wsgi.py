from webapp import create_app

app = create_app()
app.app_context().push()

if __name__ == "__main__":
    from webapp import scraper
    scraper.init_scraper()
    app.run(debug=True, port=1111)




