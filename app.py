from flask import Flask, request, render_template
import json
import pandas as pd
import beams 
import mpld3
app = Flask(__name__)
beam = beams.Beam(isWeb=True)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        return render_template()
    
    return render_template("index.html")






@app.route('/menu', methods = ['GET', 'POST'])
def menu():
    if request.method == "POST":
        return render_template()
    
    return render_template("menu.html")







@app.route('/simple', methods = ['GET', 'POST'])
def simple():
    if request.method == "POST":
        # Parse JSON from form input
        json_data = request.form.get('json_data')
        data = json.loads(json_data)

        lengtha = data.get('length')
        table1 = data.get('table1', [])
        table2 = data.get('table2', [])

        pF = pd.DataFrame(table1, columns=['distance', 'force', 'moment'])  # concentrated forces
        dF = pd.DataFrame(table2, columns=['idistance', 'fdistance', 'localeqn',  'eqforce', 'eqdistance', 'moment'])  # distributed forces
        # print(pF)
        # print(dF)
        fig1, fig2 = beam.simple(lengtha, pF, dF)
        if fig1 == False:
            return render_template("unstable_error.html") 

        return render_template("output.html", img1=fig1, img2=fig2)

    
    return render_template("simple.html")






@app.route('/canti', methods = ['GET', 'POST'])
def canti():
    if request.method == "POST":
        # Parse JSON from form input
        json_data = request.form.get('json_data')
        data = json.loads(json_data)

        lengthb = data.get('length')
        table1 = data.get('table1', [])
        table2 = data.get('table2', [])

        pF = pd.DataFrame(table1, columns=['distance', 'force', 'moment'])  # concentrated forces
        dF = pd.DataFrame(table2, columns=['idistance', 'fdistance', 'localeqn',  'eqforce', 'eqdistance', 'moment'])  # distributed forces
        print(pF)
        print(dF)
        fig1, fig2 = beam.canti(lengthb, pF,dF)

        

        return render_template("output.html", img1=fig1, img2=fig2)
    
    return render_template("canti.html")






@app.route('/mixed', methods = ['GET', 'POST'])
def mixed():
    if request.method == "POST":
        # Parse JSON from form input
        json_data = request.form.get('json_data')
        data = json.loads(json_data)

        lengtha = data.get('lengtha')
        lengthb = data.get('lengthb')
        lengthc = data.get('lengthc')
        table1 = data.get('table1', [])
        table2 = data.get('table2', [])

        pF = pd.DataFrame(table1, columns=['distance', 'force', 'moment'])  # concentrated forces
        dF = pd.DataFrame(table2, columns=['idistance', 'fdistance', 'localeqn',  'eqforce', 'eqdistance', 'moment'])  # distributed forces
        print(pF)
        print(dF)
        fig1, fig2 = beam.mixed(lengtha,lengthb,lengthc,pF,dF)
        if fig1 == False:
            return render_template("unstable_error.html") 

        return render_template("output.html", img1=fig1, img2=fig2)
    
    return render_template("mixed.html")





@app.route('/output', methods = ['POST'])
def output():
    # Parse JSON from form input
    json_data = request.form.get('json_data')
    data = json.loads(json_data)

    length = data.get('length')
    table1 = data.get('table1', [])
    table2 = data.get('table2', [])

    pF = pd.DataFrame(table1)  # concentrated forces
    dF = pd.DataFrame(table2)  # distributed forces
    print(pF)
    print(dF)
    
    return render_template('output.html')









if __name__ == "__main__":
    app.run(debug=True)

