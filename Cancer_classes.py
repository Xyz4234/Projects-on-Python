class Brain_cancer:
    def __init__(self, title, stage):
        self.title = title
        self.stage = stage

    def curable_notcurable(self):
        if self.stage == 4:
            print(f"{self.title} is highly unlikely to be cured with a 5-10% success rate.")
        elif self.stage == 3:
            print(f"{self.title} is unlikely to be cured with a 30-40% success rate.")
        elif self.stage == 2:
            print(f"{self.title} is moderately likely to be cured with a 60-80% success rate.")
        elif self.stage == 1:
            print(f"{self.title} is highly likely to be cured with a 90-100% success rate.")
        else:
            print("Invalid stage")

class GBM(Brain_cancer):
    def __init__(self, stage):
        super().__init__("Glioblastoma Multiforme (GBM)", stage)

class Astrocytoma(Brain_cancer):
    def __init__(self, stage):
        super().__init__("Astrocytoma", stage)

class Oligodendroglioma(Brain_cancer):
    def __init__(self, stage):
        super().__init__("Oligodendroglioma", stage)

class Ependymoma(Brain_cancer):
    def __init__(self, stage):
        super().__init__("Ependymoma", stage)

class LungCancer:
    def __init__(self, title, stage):
        self.title = title
        self.stage = stage

    def curable_notcurable(self):
        if self.stage == 4:
            print(f"{self.title} is highly unlikely to be cured with a 5-10% success rate.")
        elif self.stage == 3:
            print(f"{self.title} is unlikely to be cured with a 13-36% success rate.")
        elif self.stage == 2:
            print(f"{self.title} is moderately likely to be cured with a 53-60% success rate.")
        elif self.stage == 1:
            print(f"{self.title} is highly likely to be cured with a 70-92% success rate.")
        else:
            print("Invalid stage")

class Non_Small_Cell_Lung_Cancer(LungCancer):
    def __init__(self, stage):
        super().__init__("Non-Small Cell Lung Cancer", stage)

class Small_Cell_Lung_Cancer(LungCancer):
    def __init__(self, stage):
        super().__init__("Small Cell Lung Cancer", stage)

class Adenocarcinoma(LungCancer):
    def __init__(self, stage):
        super().__init__("Adenocarcinoma", stage)

class Squamous_Cell_Carcinoma(LungCancer):
    def __init__(self, stage):
        super().__init__("Squamous Cell Carcinoma", stage)





