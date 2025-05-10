def tuple_to_list(input_tuple):
    output_list = list(input_tuple)
    return output_list

if __name__ == "__main__":
    personal_details_tuple = ("John", "Doe", 30, 180, 80, "Math")
    personal_details_list = tuple_to_list(personal_details_tuple)
    
    print("Tuple:", personal_details_tuple)
    print("List:", personal_details_list)