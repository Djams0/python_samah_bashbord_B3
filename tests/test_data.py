from src.data_loader import load_data


def test_data_loading():
    df = load_data("data/sessions_dataset_320.csv")
    assert not df.empty

def test_columns_exist():
    df = load_data("data/sessions_dataset_320.csv")
    required_cols = [
        "session_id",
        "date",
        "service",
        "langue",
        "duree_minutes"
    ]
    for col in required_cols:
        assert col in df.columns

def test_no_negative_duration():
    df = load_data("data/sessions_dataset_320.csv")
    assert (df["duree_minutes"] >= 0).all()
