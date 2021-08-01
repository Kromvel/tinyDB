from flask import Flask, request
from tinydb import TinyDB, Query


# Server
app = Flask(__name__)

# Database
db = TinyDB('db.json')

Base = Query()
headers = {'content-type': 'application/json'}



@app.route('/', methods=['GET'])
def index():
    return 'Hello, world!'

@app.route('/form-example', methods=['POST'])
def form_example():
    try:
        #проверка на совпадение по дате
        if request.method == 'POST':
            date = request.args['date']
            base_Form = db.search(Base.date == date)
            len_base_Form = len(base_Form)
            
            if  base_Form != None:
                phone = request.args['phone']
                email = request.args['email']
                date = request.args['date']
                message = request.args['message']
                i=0
                name_list= []
                form_result = {}
                while i < len_base_Form:
                    base_Form_name = base_Form[i]['name']
                    base_Form_email = base_Form[i]['email']
                    base_Form_phone = base_Form[i]['phone']
                    base_Form_date = base_Form[i]['date']
                    base_Form_message = base_Form[i]['message']
                    # проверка на совпадение по всем опциям формы, а также проверка на количество всех форм, соответсвующим условиям
                    if base_Form_email == email and base_Form_phone == phone and base_Form_date == date and base_Form_message == message:
                        
                        name_list.append(base_Form_name)
                    i += 1
                if len(name_list) > 0:
                    form_result.update({'Form name':name_list})
                    return form_result
                else:
                    return "Запрашиваемая форма не найдена"
            else:
                return "Запрашиваемая форма не найдена"
        else:
            return "Запрашиваемая форма не найдена"
    except Exception as e:
        print(e)

if __name__ ==  '__main__':
    app.run(debug=False)

