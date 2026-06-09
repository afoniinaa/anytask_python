Stat = dict[str, list[dict[str, str]]]


def make_stat(filename):
    with open(filename, "rb") as handle:
        text = handle.read().decode("cp1251")

    text = text[text.find("border=0>"):text.find('</table>')]
    text = text.replace("border=0>", '')
    lines = text.split("</tr>")[:-1]
    current_year = ''
    stat = {}

    for current_line in lines:
        if "</h3>" in current_line:
            start = current_line.find("h3") + 3
            end = start + 4
            current_year = current_line[start:end]
            stat[current_year] = []
        elif "</a>" in current_line:
            current_line = current_line.split("/>")[-1]
            current_line = current_line.replace("</a></td>", "")
            full_name = current_line.split(" ")
            full_name = {"last": full_name[0], "first": full_name[1]}
            stat[current_year].append(full_name)

    return stat


def extract_years(stat: Stat):
    return sorted(stat.keys())


def extract_general(stat: Stat, year_presence: bool = False):
    def stat_to_list(mini_stat):
        return sorted(mini_stat.items(), key=lambda x: x[1], reverse=True)

    general_stat = {}
    year_stat = {}

    for year_value in stat:
        year = stat[year_value]
        year_general_stat = {}

        for full_name in year:
            first_name = full_name["first"]

            if first_name not in general_stat:
                general_stat[first_name] = 0

            if first_name not in year_general_stat:
                year_general_stat[first_name] = 0

            general_stat[first_name] += 1
            year_general_stat[first_name] += 1

        year_stat[year_value] = stat_to_list(year_general_stat)

    if not year_presence:
        return stat_to_list(general_stat)
    else:
        return year_stat


def extract_general_gender(stat: Stat, gender: str, year: str = None):
    if year is None:
        stat = extract_general(stat, False)
    else:
        stat = extract_year(stat, year)

    gender_stat = []

    for full_name in stat:
        cond_first = full_name[0][-1] in 'аяь'
        cond_second = full_name[0] in ['Лёва', 'Игорь', 'Илья', 'Никита']

        if gender == 'male':
            if not cond_first or cond_second:
                gender_stat.append(full_name)
        elif gender == 'female':
            if cond_first and not cond_second:
                gender_stat.append(full_name)

    return gender_stat


def extract_general_male(stat: Stat, year: str = None):
    return extract_general_gender(stat, 'male', year)


def extract_general_female(stat: Stat, year: str = None):
    return extract_general_gender(stat, 'female', year)


def extract_year(stat: Stat, year):
    year_stat = extract_general(stat, True)

    return year_stat[year]


def extract_year_male(stat: Stat, year):
    return extract_general_male(stat, year)


def extract_year_female(stat: Stat, year):
    return extract_general_female(stat, year)


if __name__ == "__main__":
    make_stat('../new.html')
