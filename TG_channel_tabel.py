from datetime import datetime
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

    def get_full_notes_for_company(self, company_name):
        if company_name not in self.companys:
            raise ValueError(f"Компания '{name_company}' не найдена.")
        else:
            company = manager.companys[company_name]  # получаем объект Company
            for note in company.notes: # перебираем работы компании
                formatted_date = note.date.strftime("%d.%m")
                print(f"{note.date} - {note.place} - {note.work}")


    def get_all_companies(self):
            if not self.companys:
                return "Нет добавленных компаний."
            return list(self.companys.keys())











manager = NoteManager()
name_company = input('Введите название компании - ')
manager.add_company(name_company)
place = input('Место работы - ')
work = input('Что было сделано - ')
manager.add_work(name_company, place, work)      #всегда ссылайся сначала на класс, затем на функцию
manager.get_full_notes_for_company(name_company)

#print('Ваш табель:')
#for company_name, company in manager.companys.items():
#    print(f"Компания: {company_name}")
#    for note in company.notes:
#        formatted_date = note.date.strftime("%d.%m")
#        print(formatted_date,' - ', note.place,' - ', note.work)