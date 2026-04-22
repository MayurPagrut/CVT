import os
from typing import Optional

import tensorflow as tf


class ModelLoader:
    """Singleton-like loader for the emotion model."""

    def __init__(self) -> None:
        self._model: Optional[tf.keras.Model] = None
        self._model_path = os.getenv("EMOTION_MODEL_PATH", "./models/emotion_model.h5")

    def load(self) -> None:
        if self._model is None:
            self._model = tf.keras.models.load_model(self._model_path)

    def get_model(self) -> tf.keras.Model:
        if self._model is None:
            raise RuntimeError("Model is not loaded. Ensure startup completed.")
        return self._model
