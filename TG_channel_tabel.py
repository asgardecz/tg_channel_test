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
            raise ValueError("Компания с таким названием уже существует.")
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

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            data = {
                name: [vars(note) for note in company.notes]
                for name, company in self.companys.items()
            }
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for name, notes in data.items():
                    company = Company()
                    for note_data in notes:
                        note = Parametr(note_data['place'], note_data['work'])
                        note.date = datetime.strptime(note_data['date'], "%Y-%m-%d %H:%M:%S.%f")
                        company.notes.append(note)
                    self.companys[name] = company
        except FileNotFoundError:
            print("Файл с данными не найден. Начинаем с пустого списка.")














if __name__ == '__main__':

    manager = NoteManager()
name_company = input('Введите название компании - ')
manager.add_company(name_company)

place = input('Место работы - ')
work = input('Что было сделано - ')
manager.add_work(name_company, place, work)   #всегда ссылайся сначала на класс, затем на функцию

manager.get_ready_report_for_company(name_company)
