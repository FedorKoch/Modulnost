import view
import model

def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('Файл успешно открыт')
            case 2:
                model.save_file()
                view.show_message('Файл успешно сохранен')
            case 3:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')          
            case 4:
                contact = view.add_contact()
                model.add_contact(contact)
                view.show_message('Контакт добавлен')
            case 5:
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите номер изменяемого контакта: ')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message(f'Контакт {model.get_phone_book()[index-1].get("name")} успешно изменен')
            case 6:
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    name = view.input_name('Введите имя контакта: ')
                    view.show_contacts(model.find_contact(name), 'Таких контактов нет')
                    view.show_message(f'Найдено {len(model.find_contact(name))} контактa(ов)') 
            case 7:
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите номер удаляемого контакта: ')
                    model.pop_contact(index)
                    view.show_message('Контакт успешно удален')
            case 8:
                return


