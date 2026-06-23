import json
import random
from datetime import datetime, timedelta

random.seed(42)

DOCTORS = [
    "Dr. Suresh",
    "Dr. Sharma",
    "Dr. Gupta",
    "Dr. Verma",
    "Dr. Mehta"
]

CARDIAC_NOTES = [
    "Patient admitted with NSTEMI. Underwent PCI with drug-eluting stent placement in the LAD artery. Discharged on dual antiplatelet therapy.",
    "Presented with unstable angina and exertional chest pain. Coronary angiography performed. Medical management optimized.",
    "Developed atrial fibrillation during admission. Successfully cardioverted and discharged in sinus rhythm.",
    "Admitted with acute decompensated heart failure and pulmonary edema. Responded well to intravenous diuretics.",
    "Experienced ventricular tachycardia requiring ICU monitoring. Rhythm stabilized with antiarrhythmic therapy.",
    "Reported recurrent chest discomfort. Stress test revealed inducible ischemia.",
    "History of coronary artery disease with previous stent placement. Follow-up evaluation showed stable cardiac status.",
    "Presented with STEMI and underwent emergency PCI. Post-procedure recovery was uneventful.",
    "Diagnosed with congestive heart failure. Ejection fraction measured at 35 percent.",
    "Hospitalized for recurrent angina symptoms. Medication adherence reinforced during discharge counseling."
]
SPECIAL_PATIENT_NOTES = [
    "Patient admitted with NSTEMI and underwent PCI with drug-eluting stent placement in LAD artery.",
    "Follow-up admission for recurrent unstable angina. Medical therapy optimized with beta blocker and statin.",
    "Developed atrial fibrillation during hospitalization. Successfully cardioverted and discharged in sinus rhythm.",
    "Presented with acute decompensated heart failure and pulmonary edema. Improved after diuretic therapy.",
    "Stress test demonstrated inducible ischemia requiring further cardiac evaluation.",
    "History of ventricular tachycardia requiring ICU monitoring and antiarrhythmic treatment.",
    "Coronary angiography demonstrated multivessel coronary artery disease.",
    "Readmitted for recurrent chest pain and elevated troponin levels consistent with NSTEMI.",
    "Ejection fraction measured at 35 percent with chronic systolic dysfunction.",
    "Previous PCI site remained patent during follow-up angiography."
]
DIABETES_NOTES = [
    "Known case of type 2 diabetes mellitus. HbA1c measured at 8.7 percent. Medication adjusted.",
    "Presented with poor glycemic control and fasting glucose above target range.",
    "Diabetic neuropathy noted in both lower limbs. Lifestyle modifications discussed.",
    "Insulin regimen optimized during hospital stay."
]

RESPIRATORY_NOTES = [
    "Admitted with community-acquired pneumonia. Improved after antibiotic therapy.",
    "Presented with COPD exacerbation requiring bronchodilator treatment.",
    "Acute bronchitis managed conservatively with symptomatic treatment.",
    "Required supplemental oxygen during admission. Saturation improved before discharge."
]

GENERAL_NOTES = [
    "Patient admitted for routine evaluation. Clinical course remained stable.",
    "No significant complications observed during hospitalization.",
    "Discharged in stable condition with follow-up scheduled.",
    "Vital signs remained within normal limits throughout admission."
]


def random_date():
    start = datetime(2021, 1, 1)
    end = datetime(2026, 1, 1)

    delta = end - start
    days = random.randint(0, delta.days)

    return (start + timedelta(days=days)).strftime("%Y-%m-%d")


def create_record(patient_id, doctor_name, text):
    return {
        "text": text,
        "patient_id": patient_id,
        "doctor_name": doctor_name,
        "admission_date": random_date()
    }


records = []

for note in CARDIAC_NOTES:
    records.append(
        create_record(
            patient_id="PT-8829",
            doctor_name="Dr. Suresh",
            text=note
        )
    )
for note in SPECIAL_PATIENT_NOTES:
    records.append({
        "text": note,
        "patient_id": "PT-8829",
        "doctor_name": "Dr. Suresh",
        "admission_date": random_date()
    })

for patient_num in range(1000, 2000):

    patient_id = f"PT-{patient_num}"

    if patient_id == "PT-8829":
        continue

    admissions = random.randint(2, 6)

    for _ in range(admissions):

        category = random.choice(
            ["cardiac", "diabetes", "respiratory", "general"]
        )

        if category == "cardiac":
            note = random.choice(CARDIAC_NOTES)

        elif category == "diabetes":
            note = random.choice(DIABETES_NOTES)

        elif category == "respiratory":
            note = random.choice(RESPIRATORY_NOTES)

        else:
            note = random.choice(GENERAL_NOTES)

        records.append(
            create_record(
                patient_id=patient_id,
                doctor_name=random.choice(DOCTORS),
                text=note
            )
        )


with open("mock_patient_records.jsonl", "w") as f:

    for record in records:
        f.write(json.dumps(record) + "\n")

print(f"Generated {len(records)} records")