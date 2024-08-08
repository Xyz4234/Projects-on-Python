import streamlit as st

class Cancer:
    def __init__(self, title, stage):
        self.title = title
        self.stage = stage

    def curable_notcurable(self):
        if self.stage == 4:
            return f"{self.title} is highly unlikely to be cured with a 10-5% success rate."
        elif self.stage == 3:
            return f"{self.title} is unlikely to be cured with a 30-40% success rate."
        elif self.stage == 2:
            return f"{self.title} is moderately likely to be cured with a 60-80% success rate."
        elif self.stage == 1:
            return f"{self.title} is highly likely to be cured with a 90-100% success rate."

    def treatment_options(self):
        treatments = {
            1: "Surgery, Radiation Therapy",
            2: "Surgery, Radiation Therapy, Chemotherapy",
            3: "Radiation Therapy, Chemotherapy",
            4: "Chemotherapy, Palliative Care"
        }
        return f"Common treatment options for {self.title} at stage {self.stage}: {treatments.get(self.stage, 'Consult your oncologist for options.')}"
    
    def symptoms(self):
        return f"Common symptoms of {self.title} may include fatigue, weight loss, pain, and depending on the type, specific symptoms like persistent cough (lung cancer) or skin lesions (skin cancer). Consult a doctor for personalized information."

class BrainCancer(Cancer):
    pass

class LungCancer(Cancer):
    pass

class SkinCancer(Cancer):
    pass

class BreastCancer(Cancer):
    pass

def get_cancer_class(cancer_type, stage):
    cancers = {
        "Glioblastoma Multiforme (GBM)": BrainCancer("Glioblastoma Multiforme (GBM)", stage),
        "Astrocytoma": BrainCancer("Astrocytoma", stage),
        "Oligodendroglioma": BrainCancer("Oligodendroglioma", stage),
        "Ependymoma": BrainCancer("Ependymoma", stage),
        "Non-Small Cell Lung Cancer": LungCancer("Non-Small Cell Lung Cancer", stage),
        "Small Cell Lung Cancer": LungCancer("Small Cell Lung Cancer", stage),
        "Adenocarcinoma": LungCancer("Adenocarcinoma", stage),
        "Squamous Cell Carcinoma": LungCancer("Squamous Cell Carcinoma", stage),
        "Basal Cell Carcinoma": SkinCancer("Basal Cell Carcinoma", stage),
        "Squamous Cell Skin Cancer": SkinCancer("Squamous Cell Skin Cancer", stage),
        "Melanoma": SkinCancer("Melanoma", stage),
        "Ductal Carcinoma": BreastCancer("Ductal Carcinoma", stage),
        "Lobular Carcinoma": BreastCancer("Lobular Carcinoma", stage),
        "Inflammatory Breast Cancer": BreastCancer("Inflammatory Breast Cancer", stage),
        "Triple-negative Breast Cancer": BreastCancer("Triple-negative Breast Cancer", stage),
    }
    return cancers.get(cancer_type)

# Streamlit app
st.title("Cancer Information Assistant🧑‍⚕️🩻")
st.write("👋Hello, I am your medical assistant specialized in giving vital information about various types of Brain, Lung, Skin, and Breast Cancers, along with their overall survival rates.")

cancer_type = st.selectbox("Please select the type of cancer you would like to search for:", ["Select", "Brain Cancer", "Lung Cancer", "Skin Cancer", "Breast Cancer"])

if cancer_type != "Select":
    cancer_subtype = []
    if cancer_type == "Brain Cancer":
        cancer_subtype = ["Glioblastoma Multiforme (GBM)", "Astrocytoma", "Oligodendroglioma", "Ependymoma"]
    elif cancer_type == "Lung Cancer":
        cancer_subtype = ["Non-Small Cell Lung Cancer", "Small Cell Lung Cancer", "Adenocarcinoma", "Squamous Cell Carcinoma"]
    elif cancer_type == "Skin Cancer":
        cancer_subtype = ["Basal Cell Carcinoma", "Squamous Cell Skin Cancer", "Melanoma"]
    elif cancer_type == "Breast Cancer":
        cancer_subtype = ["Ductal Carcinoma", "Lobular Carcinoma", "Inflammatory Breast Cancer", "Triple-negative Breast Cancer"]

    selected_cancer = st.selectbox(f"Select the type of {cancer_type.lower()}:", ["Select"] + cancer_subtype)
    if selected_cancer != "Select":
        stage = st.slider("Enter the stage of the cancer (1-4):", 1, 4)
        if st.button("Get Information"):
            cancer_instance = get_cancer_class(selected_cancer, stage)
            if cancer_instance:
                st.write(f"**Selected Cancer:** {cancer_instance.title}")
                st.write(cancer_instance.curable_notcurable())
                st.write("⚠️ **Warning:** Information above is statistical and curing probabilities may vary from person to person.")
                
                st.subheader("Treatment Options")
                st.write(cancer_instance.treatment_options())
                
                st.subheader("Symptoms and Early Detection")
                st.write(cancer_instance.symptoms())
            else:
                st.write("Error: Cancer type not recognized.")
