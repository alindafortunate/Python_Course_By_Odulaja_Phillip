# A sample program demonstrating how to work with the **kwargs


def process_data(**kwargs):

    for key, value in kwargs.items():
        print(f"{key} : {value}")


process_data(Name="John", Gender="Male", Age="27")
process_data(Language="Python", Framework="Django", Level="Intermediate")
