def input_valid_int(msg, start=0, end=None):
    while True:
        inp = input(msg)
        if not inp.isdecimal():
            print('Invalid input. Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')

            else:
                return int(inp)
        else:
            return int(inp)


class Patient:

    def __init__(self, name, status):
        self.name, self.status = name, status
    def __str__(self):
        status = ['Normal', 'Urgent', 'Super Urgent'][self.status]
        return f'Patient: {self.name} is {status}'

    def __repr__(self):
        return F'Patient(name="{self.name}", status={self.status})'

    def __lt__(self, other):  # see: def add_patient_smart
        return self.status > other.status  # given 2 patients: which one comes first? one with bigger status



class HospitalManager:
    def __init__(self, specializations_cnt):
        self.specializations = [[] for s in range(specializations_cnt)]
        self.MAX_QUEUE = 10
        self.NORMAL = 0
        self.URGENT = 1
        self.SUPER_URGENT = 2

    def can_add_more_patient(self, specialization):
        return len(self.specializations[specialization]) < self.MAX_QUEUE
    def add_patient_smart(self, specialization, name, status):
        spec = self.specializations[specialization]
        spec.append(Patient(name, status))
        spec.sort()
    def add_patient(self, specialization, name, status):
        spec = self.specializations[specialization]
        pat = Patient(name, status)
        if status == 0 or len(spec) == 0:
            spec.append(pat)
        elif status == 1:
            if spec[-1].status != self.NORMAL:
                spec.append(pat)
            else:
                for idx, patient in enumerate(spec):
                    if patient.status == self.NORMAL:
                        spec.insert(idx, pat)
                        break
        else:
            if spec[-1].status == self.SUPER_URGENT:
                spec.append(pat)
            else:
                for idx, patient in enumerate(spec):
                    if patient.status == self.NORMAL or patient.status == self.URGENT:
                        spec.insert(idx, pat)
                        break
    def get_printable_patients_info(self):
        result = []
        for idx, specialization in enumerate(self.specializations):
            if not specialization:
                continue
            cur_patients = []
            for patient in specialization:
                cur_patients.append(str(patient))
            result.append((idx, cur_patients))
        return result
    def get_next_patients(self, specialization):
        if len(self.specializations[specialization]) == 0:
            return None
        return self.specializations[specialization].pop(0)

    def remove_patient(self, specialization, name):
        spec = self.specializations[specialization]
        for idx, patient in enumerate(spec):
            if patient.name == name:
                del spec[idx]
                return True
        return False




class FrontEndManager:
    def __init__(self, specializations_cnt = 20):
        self.specializations_cnt = specializations_cnt
        self.hospital_manger = HospitalManager(self.specializations_cnt)
        self.add_dummy_data()

    def print_menu(self):
        print('\nProgram Options: ')
        massages = [
            'Add new patient',
            'Print all patients',
            'Get next patient',
            'Remove a leaving patient',
            'End the program'
        ]
        massages = [f'{idx+1}) {msg}' for idx, msg in enumerate(massages)]
        print('\n'.join(massages))
        msg = f'Enter yur choice(from 1 to {len(massages)}): '
        return input_valid_int(msg, 1, len(massages))

    def add_dummy_data(self):
        for i in range(10):
            self.hospital_manger.add_patient(2, 'Dummy' + str(i), i % 3)
        for i in range(4):
            self.hospital_manger.add_patient(5, 'AnotherDummy' + str(i), 0)
        for i in range(5):
            self.hospital_manger.add_patient(8, 'ThirdDummy' + str(i), 1)
        for i in range(3):
            self.hospital_manger.add_patient(12, 'ForthDummy' + str(i), 2)
        for i in range(3):
            self.hospital_manger.add_patient(13, 'FifthDummy' + str(i), 1)
            self.hospital_manger.add_patient(13, 'FifthDummy' + str(i + 5), 2)

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                specialization = input_valid_int('Enter specialization: ', 1, self.specializations_cnt) - 1
                if self.hospital_manger.can_add_more_patient(specialization):
                    name = input('Enter patient name: ')
                    status = input_valid_int('Enter status (0 normal / 1 urgent / 2 super urgent): ', 0, 2)
                    self.hospital_manger.add_patient(specialization, name, status)
                else:
                    print("Sorry we can't add more patients for this specialization at the moment.")
            elif choice == 2:
                result = self.hospital_manger.get_printable_patients_info()
                if not result:
                    print('No patients at the moment')
                else:
                    for idx, patients_info in result:
                        print(f'Specialization {idx + 1}: There are {len(patients_info)} patients.')
                        print('\n'.join(patients_info))
            elif choice == 3:
                specialization = input_valid_int('Enter specialization', 1, self.specializations_cnt) - 1
                patient = self.hospital_manger.get_next_patients(specialization)
                if patient is None:
                    print('No patients at the moment. Have rest, Dr')
                else:
                    print(f'{patient.name}, Please go with the Dr')
            elif choice == 4:
                specialization = input_valid_int('Enter specialization:', 1, self.specializations_cnt) - 1
                name = input('Enter patient name:')
                if not self.hospital_manger.remove_patient(specialization, name):
                    print('No patient with such a name in this specialization!')
            else:
                break

if __name__ == '__main__':
    app = FrontEndManager()
    app.run()