from Cancer_classes import Brain_cancer, GBM, Astrocytoma, Oligodendroglioma, Ependymoma
from Cancer_classes import LungCancer, Non_Small_Cell_Lung_Cancer, Small_Cell_Lung_Cancer, Adenocarcinoma, Squamous_Cell_Carcinoma

print("Hello, I am your medical assistant specialized in giving vital information about various types of Brain Cancer and Lung Cancer and overall survival rates of each type")

def main():
    print("Please select which type of cancer you would like to search for:")
    print("1. Brain Cancer")
    print("2. Lung Cancer")
    
    choice_of_cancer_type = int(input("Enter the number of your choice: "))
    
    if choice_of_cancer_type == 1:
        print("Here are most wide-spread types of brain cancer")
        print("Select the type of brain cancer:")
        print("1. Glioblastoma Multiforme (GBM)")
        print("2. Astrocytoma")
        print("3. Oligodendroglioma")
        print("4. Ependymoma")
        
        choice = int(input("Enter the number of your choice: "))
        stage = int(input("Enter the stage of the cancer (1-4): "))
        
        if choice == 1:
            cancer = GBM(stage)
        elif choice == 2:
            cancer = Astrocytoma(stage)
        elif choice == 3:
            cancer = Oligodendroglioma(stage)
        elif choice == 4:
            cancer = Ependymoma(stage)
        else:
            print("Invalid choice")
            return
        
    elif choice_of_cancer_type == 2:
        print("Here are most wide spread types of lung cancer")
        print("Select the type of lung cancer:")
        print("1. Non-Small Cell Lung Cancer")
        print("2. Small Cell Lung Cancer")
        print("3. Adenocarcinoma")
        print("4. Squamous Cell Carcinoma")
        
        choice = int(input("Enter the number of your choice: "))
        stage = int(input("Enter the stage of the cancer (1-4): "))
        
        if choice == 1:
            cancer = Non_Small_Cell_Lung_Cancer(stage)
        elif choice == 2:
            cancer = Small_Cell_Lung_Cancer(stage)
        elif choice == 3:
            cancer = Adenocarcinoma(stage)
        elif choice == 4:
            cancer = Squamous_Cell_Carcinoma(stage)
        else:
            print("Invalid choice")
            return
        
    else:
        print("Invalid choice")
        return

    cancer.curable_notcurable()

if __name__ == "__main__":
    main()




