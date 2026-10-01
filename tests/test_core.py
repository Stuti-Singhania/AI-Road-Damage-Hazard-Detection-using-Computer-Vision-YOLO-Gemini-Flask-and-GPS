import json

from backend import detectors
from backend import storage
from backend import verifier


def test_find_predictions_from_nested_workflow_response():
    payload = {
        "output": {
            "predictions": [
                {"confidence": 0.31, "x": 10},
                {"confidence": 0.87, "x": 20},
            ]
        }
    }

    predictions = detectors._find_predictions(payload)

    assert predictions is not None
    assert len(predictions) == 2
    assert detectors.best_prediction(predictions)["confidence"] == 0.87


def test_best_prediction_handles_empty_list():
    assert detectors.best_prediction([]) is None


def test_heuristic_verifier_uses_stricter_threshold(monkeypatch):
    monkeypatch.setenv("HEURISTIC_CONFIRM_THRESHOLD", "0.65")

    confirmed = verifier._heuristic_verify(0.70, "Pothole")
    rejected = verifier._heuristic_verify(0.60, "Pothole")

    assert confirmed["confirmed"] is True
    assert confirmed["method"] == "heuristic"
    assert rejected["confirmed"] is False


def test_storage_round_trip(tmp_path, monkeypatch):
    pins_file = tmp_path / "pins.json"

    monkeypatch.setattr(storage, "DATA_DIR", str(tmp_path))
    monkeypatch.setattr(storage, "PINS_FILE", str(pins_file))

    pin = storage.add_pin(
        detector="pothole",
        label="Pothole",
        lat=18.76,
        lon=73.85,
        confidence=0.91,
        reason="Test pin",
        image_path=None,
    )

    pins = storage.get_pins()

    assert pins_file.exists()
    assert len(pins) == 1
    assert pins[0]["id"] == pin["id"]
    assert pins[0]["label"] == "Pothole"
    assert json.loads(pins_file.read_text())[0]["confidence"] == 0.91
