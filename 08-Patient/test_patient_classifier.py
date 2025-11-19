import pytest
import openpyxl
from patient_classifier_gemini import classify_patient

# Load Excel dataset


def load_data():
    wb = openpyxl.load_workbook("./Data/sample_patient_data_50.xlsx")
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))[1:]  # skip header
    return rows


@pytest.mark.parametrize("patient_row", load_data())
def test_classification_runs(patient_row):
    """Ensure classifier returns valid JSON structure"""

    patient = {
        "PatientID": patient_row[0],
        "Age": patient_row[1],
        "Condition": patient_row[2],
        "BloodPressure": patient_row[3],
        "Pulse": patient_row[4],
        "Notes": patient_row[5]
    }

    output = classify_patient(patient)

    assert "category" in output.lower()
    assert "reason" in output.lower()


def test_critical_rule():
    """Known CRITICAL test case"""
    patient = {
        "Age": 72,
        "Condition": "Severe chest pain",
        "BloodPressure": "85/55",
        "Pulse": 145,
        "Notes": "Emergency"
    }

    output = classify_patient(patient).lower()

    assert "critical" in output


def test_moderate_rule():
    """Known MODERATE test case"""
    patient = {
        "Age": 50,
        "Condition": "Post-operative recovery",
        "BloodPressure": "120/80",
        "Pulse": 90,
        "Notes": "Requires monitoring"
    }

    output = classify_patient(patient).lower()

    assert "moderate" in output


def test_stable_rule():
    """Known STABLE test case"""
    patient = {
        "Age": 30,
        "Condition": "Routine check-up",
        "BloodPressure": "118/78",
        "Pulse": 70,
        "Notes": "No issues"
    }

    output = classify_patient(patient).lower()

    assert "stable" in output


print(load_data())
