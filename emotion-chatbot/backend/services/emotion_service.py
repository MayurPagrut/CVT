"""
Emotion Detection Service
-------------------------
Currently: Simulated random emotion output for demo purposes.

FUTURE ML INTEGRATION:
    To replace with a real ML model:
    1. Load your TensorFlow .h5 model here
    2. Accept frame data (base64 image) as input
    3. Run OpenCV preprocessing on the frame
    4. Pass through model and return predicted class
    5. The API contract (emotion + confidence) stays IDENTICAL.

    Example future implementation:
        import tensorflow as tf
        import cv2, numpy as np

        model = tf.keras.models.load_model("emotion_model.h5")
        LABELS = ["angry", "happy", "neutral", "sad"]

        def predict_emotion(frame_base64: str = None):
            img = decode_and_preprocess(frame_base64)
            preds = model.predict(img)
            idx = np.argmax(preds)
            return LABELS[idx], float(preds[0][idx])
"""

import random

EMOTIONS = ["happy", "sad", "neutral", "angry"]

EMOTION_WEIGHTS = {
    "happy": 0.35,
    "neutral": 0.30,
    "sad": 0.20,
    "angry": 0.15,
}


def predict_emotion(frame_data: str = None) -> tuple[str, float]:
    """
    Predict emotion from webcam frame.

    Args:
        frame_data: Base64-encoded image frame (unused in simulation,
                    will be used in real ML integration).

    Returns:
        tuple: (emotion_label: str, confidence: float)
    """
    # --- SIMULATION LAYER ---
    # Replace this entire block with real ML inference in production
    weights = list(EMOTION_WEIGHTS.values())
    emotion = random.choices(EMOTIONS, weights=weights, k=1)[0]
    confidence = round(random.uniform(0.65, 0.98), 2)
    # --- END SIMULATION LAYER ---

    return emotion, confidence


def get_emotion_trend(emotions: list[str]) -> str:
    """
    Compute dominant emotion from recent history.

    Args:
        emotions: List of recent emotion labels (last N detections).

    Returns:
        str: The most frequently occurring emotion.
    """
    if not emotions:
        return "neutral"
    return max(set(emotions), key=emotions.count)
