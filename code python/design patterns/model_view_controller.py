from model import person
import model_view

def show_all():
    #gets list of all Person objects
    people_in_db = person.get_all()

    #calls view
    return model_view.show_all_view(people_in_db)

def start():
    model_view.start_view()
    input=model_view.start_view()
    if input == 'y':
        return show_all()
    else:
        return model_view.end_view()

if __name__=="__main__":
    #running controller function
    start()        
                