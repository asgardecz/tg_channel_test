import os.path
from datetime import datetime
import json
class Company:
    def __init__(self):
        self.notes = [] # Общий список выполненных работ для конкретной компании

class Parametr:
    def __init__(self, place, work): #что я делал
        self.date = datetime.now()  # Дата создания записи
        self.place = place  # Место работы
        self.work = work           # Описание выполненных работ

class NoteManager:
    def __init__(self):
        self.companys = {}  # словарь компаний

    def add_company(self, name_company):
        if name_company in self.companys:
            name_company = name_company
        self.companys[name_company] = Company()

    def add_work(self, name_company, place, work):
        task = Parametr(place, work)
        self.companys[name_company].notes.append(task)

    def get_notes_from_date(self, name_company):
        if name_company not in self.companys:
            raise ValueError(f"Компания '{name_company}' не найдена.")
        return self.companys[name_company].notes

    def get_ready_report_for_company(self, company_name):
        if company_name not in self.companys:
            raise ValueError(f"Компания '{name_company}' не найдена.")
        else:
            print('Ваш табель:')
            for company_name, company in manager.companys.items():
                print(f"Компания: {company_name}")
                for note in company.notes:
                    formatted_date = note.date.strftime("%d.%m")
                    print(formatted_date, ' - ', note.place, ' - ', note.work)


    def get_all_companies(self):
            if not self.companys:
                return "Нет добавленных компаний."
            return list(self.companys.keys())

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            self.companys = {}
            return

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                #content = file.read()
                #if not content.strip():
                    #self.companys = {}
                    #return

                data = json.load(file)
                print(data)
                for name, notes in data.items():
                    company = Company()
                    for note_data in notes:
                        note = Parametr(note_data['place'], note_data['work'])
                        note.date = datetime.strptime(note_data['date'], "%Y-%m-%d %H:%M:%S.%f")
                        company.notes.append(note)
                    self.companys[name] = company
        except FileNotFoundError:
            return




    def save_to_file(self, filename):
        folder = os.path.dirname(filename)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)


        with open(filename, 'w', encoding='utf-8') as file:
            data = {
                name: [
                    {
                        "date": note.date.strftime("%Y-%m-%d %H:%M:%S.%f"),
                        "place": note.place,
                        "work": note.work
                    }
                    for note in company.notes
                ]
                for name, company in self.companys.items()
            }
            print(data)
            json.dump(data, file, ensure_ascii=False, indent=4)






if __name__ == '__main__':
    manager = NoteManager()
    manager.load_from_file("data/allReport.json")

    name_company = input('Введите название компании - ')
    manager.add_company(name_company)


    place = input('Место работы - ')
    work = input('Что было сделано - ')
    manager.add_work(name_company, place, work)   #всегда ссылайся сначала на класс, затем на функцию

    manager.get_ready_report_for_company(name_company)
    manager.save_to_file("data/allReport.json")