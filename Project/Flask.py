from flask import Flask
from flask import render_template
from flask import request
products = {
    "1":("portokalada",4.5),
    "2":("frapedouba",3.5),
    "3":("espresara",4)
}

app = Flask(__name__)


@app.route('/marousiCafe')
def showSite():
    return render_template('marousiCafe.html')

@app.route('/data', methods=['GET', 'POST'])
def sendData():

    order = request.form.getlist("item")
    itemLst = list()
    for code in order:
        itemLst.append(products[code])
    totalPrice = 0
    yourOrder = "Your order is "
    for _ in itemLst:
        totalPrice += _[1]
        yourOrder += _[0] + ","

    return "ORDER DONE!!! \n" + yourOrder + "\nTotal price :" + str(totalPrice)


app.run(host="192.168.223.116",port=5010)