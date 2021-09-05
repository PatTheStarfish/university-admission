class SortingAlgorithm:

    def __init__(self):
        self.applicants_list = []
        self.departments = ["Mathematics", "Physics", "Biotech", "Chemistry", "Engineering"]
        self.departments_ranking = {}
        self.num_applicants = 0
        self.vacancies = {}
        self.accepted = {}

    def get_input(self):
        dept_capacity = int(input())
        file = open("applicants.txt", "r")
        for line in file:
            self.applicants_list.append(line.split())
        file.close()
        self.vacancies = dict.fromkeys(self.departments, dept_capacity)
        self.departments_ranking = dict.fromkeys(self.departments, [])
        self.accepted = dict.fromkeys(self.departments, [])

    def create_rankings(self, priority):
        self.num_applicants = len(self.applicants_list)
        for i in range(self.num_applicants):
            temp = self.applicants_list[i]
            if temp[priority + 6] in self.departments:
                self.departments_ranking[temp[priority + 6]] = self.departments_ranking[temp[priority + 6]] + [temp]

        for i in self.departments:
            if i == "Mathematics":
                self.departments_ranking[i] = sorted(self.departments_ranking[i],
                                                     key=lambda x: (-max(float(x[4]), float(x[6])), x[0], x[1]))
            elif i == "Physics":
                self.departments_ranking[i] = sorted(self.departments_ranking[i],
                                                     key=lambda x: (-max(((float(x[2]) + float(x[4])) / 2),
                                                                         float(x[6])), x[0], x[1]))
            elif i == "Engineering":
                self.departments_ranking[i] = sorted(self.departments_ranking[i],
                                                     key=lambda x: (-max(((float(x[5]) + float(x[4])) / 2),
                                                                         float(x[6])), x[0], x[1]))
            elif i == "Chemistry":
                self.departments_ranking[i] = sorted(self.departments_ranking[i],
                                                     key=lambda x: (-max(float(x[3]), float(x[6])), x[0], x[1]))
            else:
                self.departments_ranking[i] = sorted(self.departments_ranking[i],
                                                     key=lambda x: (-max(((float(x[3]) + float(x[2])) / 2),
                                                                         float(x[6])), x[0], x[1]))

    def assign_rankings(self):
        for i in self.departments:
            if self.vacancies[i] > 0:
                if len(self.departments_ranking[i]) >= self.vacancies[i]:
                    for j in range(self.vacancies[i]):
                        self.accepted[i] = self.accepted[i] + [self.departments_ranking[i][j]]
                        self.applicants_list.remove(self.departments_ranking[i][j])
                    self.vacancies[i] = 0
                else:
                    for j in range(len(self.departments_ranking[i])):
                        self.accepted[i] = self.accepted[i] + [self.departments_ranking[i][j]]
                        self.applicants_list.remove(self.departments_ranking[i][j])
                        self.vacancies[i] -= 1
        self.departments_ranking = dict.fromkeys(self.departments, [])

    def print_results(self):
        self.accepted["Mathematics"] = sorted(self.accepted["Mathematics"], key=lambda x: (-float(x[4]), x[0], x[1]))
        self.accepted["Physics"] = sorted(self.accepted["Physics"], key=lambda x: (-float(x[2]), x[0], x[1]))
        self.accepted["Engineering"] = sorted(self.accepted["Engineering"], key=lambda x: (-float(x[5]), x[0], x[1]))
        self.accepted["Biotech"] = sorted(self.accepted["Biotech"], key=lambda x: (-float(x[3]), x[0], x[1]))
        self.accepted["Chemistry"] = sorted(self.accepted["Chemistry"], key=lambda x: (-float(x[3]), x[0], x[1]))
        for i in sorted(self.departments):
            print(i)

            for j in self.accepted[i]:
                if i == "Mathematics":
                    print(j[0], j[1], j[4])
                elif i == "Physics":
                    print(j[0], j[1], j[2])
                elif i == "Engineering":
                    print(j[0], j[1], j[5])
                else:
                    print(j[0], j[1], j[3])
            print()

    def print_to_file(self):
        self.accepted["Mathematics"] = sorted(self.accepted["Mathematics"],
                                              key=lambda x: (-max(float(x[4]), float(x[6])), x[0], x[1]))
        self.accepted["Physics"] = sorted(self.accepted["Physics"],
                                          key=lambda x: (-max((float(x[2]) + float(x[4])) / 2,
                                                              float(x[6])), x[0], x[1]))
        self.accepted["Engineering"] = sorted(self.accepted["Engineering"],
                                              key=lambda x: (-max((float(x[4]) + float(x[5])) / 2,
                                                                  float(x[6])), x[0], x[1]))
        self.accepted["Biotech"] = sorted(self.accepted["Biotech"],
                                          key=lambda x: (-max((float(x[2]) + float(x[3])) / 2,
                                                              float(x[6])), x[0], x[1]))
        self.accepted["Chemistry"] = sorted(self.accepted["Chemistry"],
                                            key=lambda x: (-max(float(x[3]), float(x[6])), x[0], x[1]))
        file = open("biotech.txt", "w")
        for line in self.accepted["Biotech"]:
            file.write(f"{line[0]} {line[1]}, {round(max((float(line[2]) + float(line[3]))/ 2, float(line[6])), 1)}\n")
        file.close()
        file = open("chemistry.txt", "w")
        for line in self.accepted["Chemistry"]:
            file.write(f"{line[0]} {line[1]}, {round(max(float(line[3]), float(line[6])), 1)}\n")
        file.close()
        file = open("engineering.txt", "w")
        for line in self.accepted["Engineering"]:
            file.write(f"{line[0]} {line[1]}, {round(max((float(line[4]) + float(line[5])) / 2, float(line[6])), 1)}\n")
        file.close()
        file = open("mathematics.txt", "w")
        for line in self.accepted["Mathematics"]:
            file.write(f"{line[0]} {line[1]}, {round(max(float(line[4]), float(line[6])), 1)}\n")
        file.close()
        file = open("physics.txt", "w")
        for line in self.accepted["Physics"]:
            file.write(f"{line[0]} {line[1]}, {round(max((float(line[2]) + float(line[4])) / 2, float(line[6])), 1)}\n")
        file.close()

    def perform_selection(self):
        self.get_input()
        self.create_rankings(1)
        self.assign_rankings()
        self.create_rankings(2)
        self.assign_rankings()
        self.create_rankings(3)
        self.assign_rankings()
        self.print_to_file()


procedure = SortingAlgorithm()
procedure.perform_selection()
