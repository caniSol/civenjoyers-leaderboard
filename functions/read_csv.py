def read_csv(filepath: str) -> list[dict[str, int | str]]:
    output_list = []

    with open(filepath, "r") as file:
        split_file = file.read().split("\n")
        headline = split_file.pop(0).split(",")

        for entry in split_file:
            if entry == "":
                continue

            split_line = entry.split(",")

            line_dic = {}

            for i in range(len(headline)):
                try:
                    line_dic[headline[i]] = split_line[i]
                except IndexError:
                    continue

            output_list.append(line_dic)

    return output_list
