from app import create_app
from app import oliStuff

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    fetcher = oliStuff.Fetcher()
    #print(fetcher.getCompanyEm("ExxonMobil"))
    #print(fetcher.getRandomCompany())

    exit()