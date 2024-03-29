def remove_underlines(data : str) -> list:
    format_as_list = data.split("\n")[4:][:-3]
    clean_data = []
    for i in format_as_list:
        if i != "":
            clean_data.append(i)
    return clean_data

def get_formated_data(data : list[str], target : str):
    removed_underlines : list = remove_underlines(data)
    remove_instruction = []
    formated_data = []

    for i in removed_underlines:
        if i != f"•You can do the following to view {target}:":
            remove_instruction.append(i)
    
    r = remove_instruction
    for i in range(0, len(r) - 1, 2 ):
        status = extract_string(r[i],'[', ']')
        uuid = extract_string(r[i], "(" , ")")
        formated_data.append((r[i].replace(status, "").replace(uuid, "").strip(), status , uuid))
    return formated_data



def extract_string(target, start : str, end : str):
    start, end = target.index(start), target.find(end) + 1
    return target[start:end]


# Modules enum
class TopicFiles():
    Fundamentals = "Fundamentals"
    Object_Orientation = "Object_Orientation"
    Web_Development = "Web_Development"


class Data():
    @classmethod
    def read_file(cls, source):
        try:
            with open(source) as modules:
                return modules.read()
        except Exception as e:
            print(f"Oops! something went wrong! -, {e}")
            return ""
    @classmethod
    def get_modules(cls):
        source = "./data/modules.txt"
        return get_formated_data(cls.read_file(source), "topics")
    @classmethod
    def get_topics(cls, target : str):
        source = f"./data/topics/{target}.txt"
        return get_formated_data(cls.read_file(source), "problems")
    @classmethod
    def get_reviews(cls):
        soruce = "./data/topics.txt"
        return get_formated_data(cls.read_file(soruce), "")



# for i in Data.get_reviews():
#     print(i)